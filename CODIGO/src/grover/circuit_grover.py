"""
Grover 2 qubits - Visualización geométrica (rotación en plano 2D)
Ahora puedes elegir el estado marcado |w> con la variable 'marked'.

Ejemplos:
  marked = "00"  o "01" o "10" o "11"
"""

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# =========================
# Oráculo general (fase -1 sobre |marked>)
# =========================

def oraculo_fase_marcado(qc: QuantumCircuit, marked: str):
    """
    Aplica un flip de fase (multiplica por -1) SOLO al estado |marked>.
    Para 2 qubits, se implementa como:
      - X en los qubits donde marked tiene '0' (para mapear |marked> -> |11>)
      - CZ
      - deshacer X
    """
    if len(marked) != 2 or any(c not in "01" for c in marked):
        raise ValueError("marked debe ser un string de 2 bits, ej: '10'.")

    # Qiskit usa orden |q1 q0> en el estado computacional.
    # Para trabajar de forma intuitiva con strings "b1b0",
    # tomamos:
    #   marked[0] -> qubit 1
    #   marked[1] -> qubit 0
    b1, b0 = marked[0], marked[1]

    # Mapear |marked> a |11> usando X donde haya 0
    if b0 == "0":
        qc.x(0)
    if b1 == "0":
        qc.x(1)

    # Flip de fase en |11>
    qc.cz(0, 1)

    # Deshacer mapeo
    if b0 == "0":
        qc.x(0)
    if b1 == "0":
        qc.x(1)


# =========================
# Difusión (2 qubits)
# =========================

def difusion_2q(qc: QuantumCircuit):
    """Difusión estándar para 2 qubits: D = 2|s><s| - I."""
    qc.h([0, 1])
    qc.x([0, 1])
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x([0, 1])
    qc.h([0, 1])


# =========================
# Base geométrica { |w>, |w_perp> }
# =========================

def construir_base_w_wperp(n_qubits: int, marked: str):
    """
    Construye:
      |w>      = estado marcado (computacional)
      |s>      = superposición uniforme
      |w_perp> = componente de |s> ortogonal a |w>, normalizada
    Retorna w, w_perp, s como np.ndarray de tamaño N.
    """
    N = 2 ** n_qubits
    w_index = int(marked, 2)

    w = np.zeros(N, dtype=complex)
    w[w_index] = 1.0

    s = np.ones(N, dtype=complex) / np.sqrt(N)

    overlap = np.vdot(w, s)  # <w|s>
    w_perp = s - overlap * w
    w_perp /= np.linalg.norm(w_perp)

    return w, w_perp, s


def coords_en_plano(psi: np.ndarray, w: np.ndarray, w_perp: np.ndarray):
    """Coordenadas: a=<w|psi>, b=<w_perp|psi>."""
    a = np.vdot(w, psi)
    b = np.vdot(w_perp, psi)
    return a, b


# =========================
# Estados por iteración
# =========================

def estado_inicial_uniforme(n_qubits=2):
    qc = QuantumCircuit(n_qubits)
    qc.h(list(range(n_qubits)))
    return qc


def ejecutar_k_iteraciones(marked: str, k_max=6):
    """
    Devuelve lista de Statevector para k = 0..k_max,
    donde cada iteración es (oráculo + difusión).
    """
    qc = estado_inicial_uniforme(2)
    estados = [Statevector.from_instruction(qc)]

    for _ in range(k_max):
        oraculo_fase_marcado(qc, marked)
        difusion_2q(qc)
        estados.append(Statevector.from_instruction(qc))

    return estados


# =========================
# Visualización
# =========================

def plot_grover_geometrico(marked="11", k_max=4):
    n_qubits = 2
    w, w_perp, _ = construir_base_w_wperp(n_qubits, marked)
    estados = ejecutar_k_iteraciones(marked, k_max=k_max)

    coords = []
    p_w = []
    for sv in estados:
        psi = sv.data
        a, b = coords_en_plano(psi, w, w_perp)
        coords.append((a, b))
        p_w.append(np.abs(a) ** 2)

    xs = [np.real(b) for (a, b) in coords]
    ys = [np.real(a) for (a, b) in coords]

    fig = plt.figure(figsize=(10, 4.2))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.1, 1.0])

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])

    # Plano 2D
    t = np.linspace(0, 2*np.pi, 400)
    ax0.plot(np.cos(t), np.sin(t), linewidth=1, alpha=0.5)
    ax0.plot(xs, ys, marker="o")
    for k, (x, y) in enumerate(zip(xs, ys)):
        ax0.text(x + 0.02, y + 0.02, f"k={k}", fontsize=9)

    ax0.axhline(0, linewidth=1, alpha=0.4)
    ax0.axvline(0, linewidth=1, alpha=0.4)
    ax0.set_aspect("equal", "box")
    ax0.set_xlim(-1.05, 1.05)
    ax0.set_ylim(-1.05, 1.05)
    ax0.set_xlabel(r"Componente sobre $|w_\perp\rangle$")
    ax0.set_ylabel(r"Componente sobre $|w\rangle$")
    ax0.set_title(f"Rotación en el plano 2D (marcado |w> = |{marked}>)")
    ax0.annotate(r"objetivo $|w\rangle$", xy=(0, 1.0), xytext=(0.15, 0.8),
                 arrowprops=dict(arrowstyle="->", lw=1))

    # Probabilidad vs iteraciones
    ax1.plot(range(len(p_w)), p_w, marker="o")
    ax1.set_ylim(0, 1.0)
    ax1.set_xlabel("Iteraciones Grover (k)")
    ax1.set_ylabel(r"$P(|w\rangle)$")
    ax1.set_title("Amplificación + overshoot")
    ax1.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # CAMBIA AQUÍ:
    marked = "11"   # <- prueba: "00", "01", "10", "11"
    plot_grover_geometrico(marked=marked, k_max=4)
