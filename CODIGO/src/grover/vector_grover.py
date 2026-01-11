"""
Grover n qubits - Animación REAL (saltos) + círculo guía + vectores base visibles
Soporta:
  - n_qubits >= 2
  - uno o varios estados marcados (marked_states)
  - muestra pasos reales: init -> oracle -> diffusion -> oracle -> diffusion ...
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# =========================
# Helpers de bits / índices
# =========================

def validar_bitstring(s: str, n: int):
    if len(s) != n or any(c not in "01" for c in s):
        raise ValueError(f"Cada estado marcado debe ser string de {n} bits, ej: {'0'*n}.")

def bitstring_a_index(s: str) -> int:
    return int(s, 2)

def etiquetas_estados(n: int):
    return [format(i, f"0{n}b") for i in range(2**n)]


# =========================
# Oráculo general: flip de fase para estados marcados
# =========================

def phase_flip_state(qc: QuantumCircuit, marked: str):
    """
    Aplica un flip de fase (-1) SOLO al estado computacional |marked>.
    Implementación:
      - X en qubits donde marked tenga 0 para mapear |marked> -> |11..1>
      - mcp(pi) con controles en 0..n-2 y target en n-1
      - deshacer X
    Interpretación de bitstring: marked="b_{n-1}...b_0" = |q_{n-1} ... q_0>.
    """
    n = qc.num_qubits
    validar_bitstring(marked, n)

    # Mapear marked -> all-ones
    for q in range(n):
        if marked[n - 1 - q] == "0":
            # cuidado: marked[0] corresponde a q_{n-1}
            # marked[n-1] corresponde a q_0
            qc.x(q)

    # Fase en |11..1> usando multi-controlled phase pi
    if n == 1:
        qc.p(np.pi, 0)
    elif n == 2:
        qc.cp(np.pi, 0, 1)  # fase si |11>
    else:
        controls = list(range(n - 1))
        target = n - 1
        qc.mcp(np.pi, controls, target)

    # Deshacer mapeo
    for q in range(n):
        if marked[n - 1 - q] == "0":
            qc.x(q)


def oraculo_fase_marcados(qc: QuantumCircuit, marked_states):
    """Aplica flip de fase a cada estado en marked_states."""
    for m in marked_states:
        phase_flip_state(qc, m)


# =========================
# Difusión general n-qubits
# =========================

def difusion_nq(qc: QuantumCircuit):
    """
    Difusión estándar:
      D = H^n X^n (I - 2|11..1><11..1|) X^n H^n
    Usamos mcp(pi) para flip de fase en |11..1>.
    """
    n = qc.num_qubits
    qc.h(range(n))
    qc.x(range(n))

    # flip fase en |11..1>
    if n == 1:
        qc.p(np.pi, 0)
    elif n == 2:
        qc.cp(np.pi, 0, 1)
    else:
        controls = list(range(n - 1))
        target = n - 1
        qc.mcp(np.pi, controls, target)

    qc.x(range(n))
    qc.h(range(n))


# =========================
# Base geométrica: |w>, |w_perp>, |s>
# =========================

def construir_base_w_wperp(n_qubits: int, marked_states):
    """
    |w> = superposición uniforme sobre good (marcados), normalizada
    |s> = superposición uniforme sobre todos los estados, normalizada
    |w_perp> = componente de |s> ortogonal a |w>, normalizada
    """
    N = 2 ** n_qubits

    # vector |w>
    w = np.zeros(N, dtype=complex)
    for m in marked_states:
        validar_bitstring(m, n_qubits)
        w[bitstring_a_index(m)] = 1.0

    M = int(np.count_nonzero(w))
    if M == 0:
        raise ValueError("marked_states no puede estar vacío.")
    w /= np.sqrt(M)

    # |s>
    s = np.ones(N, dtype=complex) / np.sqrt(N)

    # |w_perp>
    overlap = np.vdot(w, s)         # <w|s>
    w_perp = s - overlap * w
    norm = np.linalg.norm(w_perp)
    if norm < 1e-12:
        # Caso degenerado (por ejemplo M=N): no hay w_perp
        w_perp = np.zeros(N, dtype=complex)
    else:
        w_perp /= norm

    return w, w_perp, s


def coords_en_plano(psi: np.ndarray, w: np.ndarray, w_perp: np.ndarray):
    a = np.vdot(w, psi)        # <w|psi>
    b = np.vdot(w_perp, psi)   # <w_perp|psi>
    return a, b


def residuo_fuera_del_plano(psi: np.ndarray, w: np.ndarray, w_perp: np.ndarray):
    a, b = coords_en_plano(psi, w, w_perp)
    proj = a * w + b * w_perp
    return np.linalg.norm(psi - proj)


# =========================
# Debug: amplitudes / fases / promedio
# =========================

def promedio_amplitudes(psi: np.ndarray):
    return np.mean(psi)

def imprimir_resumen(psi: np.ndarray, marked_states, titulo: str, n_qubits: int, max_print=16):
    """
    Para n grande, imprimir todo es demasiada salida.
    - Si N <= max_print, imprime todos.
    - Si no, imprime: estados marcados + top amplitudes por |a|.
    """
    N = 2**n_qubits
    labels = etiquetas_estados(n_qubits)
    avg = promedio_amplitudes(psi)

    print("\n" + "="*90)
    print(titulo)
    print(f"n={n_qubits}  N={N}  marcados={marked_states}")
    print(f"avg amplitudes = {avg.real:+.6f}{avg.imag:+.6f}j")
    print("-"*90)

    if N <= max_print:
        idxs = list(range(N))
    else:
        marked_idxs = set(bitstring_a_index(m) for m in marked_states)
        top = np.argsort(-np.abs(psi))[:max_print]
        idxs = sorted(marked_idxs.union(set(top)))

    for i in idxs:
        a = psi[i]
        mag = np.abs(a)
        ph = np.angle(a)
        lab = labels[i]
        tag = "  <== good" if lab in marked_states else ""
        print(f"|{lab}>  a={a.real:+.6f}{a.imag:+.6f}j  |a|={mag:.6f}  phase={ph:+.6f} {tag}")

    print("="*90)


# =========================
# Estados Grover con subpasos reales
# =========================

def estado_inicial_uniforme(n_qubits: int):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    return qc


def estados_grover_con_subpasos(n_qubits: int, marked_states, k_max: int):
    """
    Devuelve lista de tuplas (k, etapa, Statevector):
      (0, "init", |s>)
      por k=1..k_max:
        (k, "oracle",    estado tras oráculo)
        (k, "diffusion", estado tras difusión)
    """
    qc = estado_inicial_uniforme(n_qubits)
    out = [(0, "init", Statevector.from_instruction(qc))]

    for k in range(1, k_max + 1):
        oraculo_fase_marcados(qc, marked_states)
        out.append((k, "oracle", Statevector.from_instruction(qc)))

        difusion_nq(qc)
        out.append((k, "diffusion", Statevector.from_instruction(qc)))

    return out


# =========================
# Animación REAL (saltos)
# =========================

def animar_grover_real(
    n_qubits=3,
    marked_states=("101",),
    k_max=8,
    fps=2,
    debug=True,
    mostrar_residuo=True
):
    marked_states = list(marked_states)
    for m in marked_states:
        validar_bitstring(m, n_qubits)

    w, w_perp, s = construir_base_w_wperp(n_qubits, marked_states)
    seq = estados_grover_con_subpasos(n_qubits, marked_states, k_max=k_max)

    # Coordenadas discretas en el plano
    xs, ys = [], []
    meta = []           # (k, etapa)
    p_good = []         # P(good) después de difusión por iteración

    for (k, etapa, sv) in seq:
        psi = sv.data
        a, b = coords_en_plano(psi, w, w_perp)

        # Para visualizar, tomamos parte real (la fase global puede existir)
        xs.append(np.real(b))
        ys.append(np.real(a))
        meta.append((k, etapa))

        if etapa == "diffusion":
            p_good.append(float(np.abs(a) ** 2))  # prob en subespacio good

    # Debug prints
    if debug:
        imprimir_resumen(seq[0][2].data, marked_states, "Estado inicial |s> (k=0)", n_qubits)
        # Mostrar k=1 oracle y diffusion
        for (k, etapa, sv) in seq:
            if k == 1 and etapa in ("oracle", "diffusion"):
                imprimir_resumen(sv.data, marked_states, f"k=1 después de {etapa}", n_qubits)

    if mostrar_residuo:
        print("\nResiduo fuera del plano ||psi - (a|w>+b|w_perp>)|| (ideal ~ 0):")
        for idx, (k, etapa, sv) in enumerate(seq[:min(len(seq), 10)]):
            r = residuo_fuera_del_plano(sv.data, w, w_perp)
            print(f"  idx={idx:2d}  k={k} etapa={etapa:9s}  residuo={r:.3e}")

    # Figura
    fig = plt.figure(figsize=(10.8, 5.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[1.2, 1.0])
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])

    # Círculo guía
    t = np.linspace(0, 2*np.pi, 600)
    ax0.plot(np.cos(t), np.sin(t), linewidth=1.5, alpha=0.30)

    ax0.axhline(0, linewidth=1, alpha=0.25)
    ax0.axvline(0, linewidth=1, alpha=0.25)
    ax0.set_aspect("equal", "box")
    ax0.set_xlim(-1.05, 1.05)
    ax0.set_ylim(-1.05, 1.05)
    ax0.set_xlabel(r"Componente sobre $|w_\perp\rangle$")
    ax0.set_ylabel(r"Componente sobre $|w\rangle$")
    ax0.set_title(f"Grover REAL (saltos) — n={n_qubits}  M={len(marked_states)}")

    # Vectores base visibles
    ax0.quiver(0, 0, 1, 0, angles="xy", scale_units="xy", scale=1, alpha=0.6)
    ax0.quiver(0, 0, 0, 1, angles="xy", scale_units="xy", scale=1, alpha=0.6)
    ax0.text(0.92, -0.08, r"$|w_\perp\rangle$", fontsize=11, ha="right")
    ax0.text(0.06, 0.92, r"$|w\rangle$", fontsize=11, va="top")

    # Elementos animados
    vec = ax0.quiver(0, 0, xs[0], ys[0], angles="xy", scale_units="xy", scale=1)
    traj, = ax0.plot([], [], linewidth=2, alpha=0.8)
    dot, = ax0.plot([], [], marker="o", markersize=7)
    txt = ax0.text(-1.02, 1.02, "", fontsize=11, va="top")

    # Panel derecha: P(good) después de difusión
    ax1.set_xlim(0, k_max)
    ax1.set_ylim(0, 1.0)
    ax1.set_xlabel("Iteraciones Grover (k)")
    ax1.set_ylabel(r"$P(\mathrm{good})$")
    ax1.set_title("Probabilidad de éxito (después de difusión)")
    ax1.grid(True, alpha=0.25)

    prob_line, = ax1.plot([], [], marker="o", linewidth=2)
    prob_dot, = ax1.plot([], [], marker="o", markersize=10)

    def init():
        traj.set_data([], [])
        dot.set_data([], [])
        prob_line.set_data([], [])
        prob_dot.set_data([], [])
        txt.set_text("")
        return vec, traj, dot, prob_line, prob_dot, txt

    def update(frame):
        vec.set_UVC(xs[frame], ys[frame])
        traj.set_data(xs[:frame+1], ys[:frame+1])
        dot.set_data([xs[frame]], [ys[frame]])

        k, etapa = meta[frame]
        txt.set_text(f"k={k}  etapa={etapa}  marcados={marked_states}")

        # Actualizar curva de éxito solo cuando se completa difusión de k
        if etapa == "diffusion":
            idx = k - 1  # p_good index
            ks = list(range(1, k + 1))
            prob_line.set_data(ks, p_good[:idx+1])
            prob_dot.set_data([k], [p_good[idx]])

        return vec, traj, dot, prob_line, prob_dot, txt

    interval_ms = int(1000 / max(1, fps))
    anim = FuncAnimation(fig, update, frames=len(xs),
                         init_func=init, interval=interval_ms, blit=True, repeat=True)

    plt.tight_layout()
    plt.show()
    return anim


if __name__ == "__main__":
    # ====== CONFIG REALISTA PARA APRENDER ======
    # 2 qubits (N=4) es demasiado “perfecto”. Usa 3 o 4 para ver la amplificación gradual.
    n_qubits = 3

    # Un marcado (M=1): ejemplo
    marked_states = ("101",)

    # Si quieres ver M>1 (cambia el ángulo):
    # marked_states = ("101", "110")

    animar_grover_real(
        n_qubits=n_qubits,
        marked_states=marked_states,
        k_max=10,
        fps=2,
        debug=True,
        mostrar_residuo=True
    )
