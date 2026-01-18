import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# ==========================================================
# Utilidades: validación, etiquetas, impresión de amplitudes
# ==========================================================

def validar_marked(marked: str, n: int):
    if len(marked) != n or any(c not in "01" for c in marked):
        raise ValueError(f"marked debe tener {n} bits (solo 0/1). Ej: {'0'*n}")

def etiqueta(i: int, n: int) -> str:
    return format(i, f"0{n}b")

def imprimir_amplitudes(psi: np.ndarray, n: int, marked: str, titulo: str, max_print: int = 16):
    """Imprime amplitudes (todas si N<=max_print, si no: marked + top por |a|)."""
    N = 2**n
    idx_marked = int(marked, 2)

    print("\n" + "="*90)
    print(titulo)
    print(f"n={n}  N={N}  marked=|{marked}>  idx={idx_marked}")
    avg = np.mean(psi)
    print(f"avg(amplitudes) = {avg.real:+.6f}{avg.imag:+.6f}j")
    print("-"*90)

    if N <= max_print:
        idxs = list(range(N))
    else:
        top = np.argsort(-np.abs(psi))[:max_print]
        idxs = sorted(set(top).union({idx_marked}))

    for i in idxs:
        a = psi[i]
        lab = etiqueta(i, n)
        tag = "  <== MARKED" if i == idx_marked else ""
        print(f"|{lab}>  a={a.real:+.6f}{a.imag:+.6f}j  |a|={np.abs(a):.6f}  phase={np.angle(a):+.6f}{tag}")
    print("="*90)


# ==========================================================
# Grover: estado inicial, oráculo (phase flip), difusión
# ==========================================================

def preparar_superposicion(qc: QuantumCircuit):
    """|s> = H^n |0...0>"""
    qc.h(range(qc.num_qubits))

def oracle_phase_flip(qc: QuantumCircuit, marked: str):
    """
    Oráculo de fase para UN estado marcado:
      |marked> -> -|marked>
    Convención: marked="b_{n-1}...b_0" representa |q_{n-1}...q_0>.
    Implementación:
      - X en qubits donde marked tiene 0 (para mapear |marked> -> |11..1>)
      - mcp(pi) (o cp(pi) si n=2) para dar fase -1 a |11..1>
      - deshacer X
    """
    n = qc.num_qubits
    validar_marked(marked, n)

    # Mapear |marked> -> |11..1>
    for q in range(n):
        # q=0 es el qubit menos significativo; marked[n-1-q] corresponde a ese qubit
        if marked[n - 1 - q] == "0":
            qc.x(q)

    # Aplicar fase -1 al estado |11..1>
    if n == 1:
        qc.p(np.pi, 0)
    elif n == 2:
        qc.cp(np.pi, 0, 1)
    else:
        controls = list(range(n - 1))
        target = n - 1
        qc.mcp(np.pi, controls, target)

    # Deshacer mapeo
    for q in range(n):
        if marked[n - 1 - q] == "0":
            qc.x(q)

def diffusion(qc: QuantumCircuit):
    """
    Difusión estándar:
      D = 2|s><s| - I
    Circuito: H^n X^n (fase -1 en |11..1>) X^n H^n
    """
    n = qc.num_qubits
    qc.h(range(n))
    qc.x(range(n))

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


# ==========================================================
# Demo: correr k iteraciones y ver probabilidad de éxito
# ==========================================================

def prob_marked(psi: np.ndarray, marked: str) -> float:
    idx = int(marked, 2)
    return float(np.abs(psi[idx])**2)

def grover_esencia(n: int, marked: str, k_max: int = None, verbose: bool = False):
    """
    Ejecuta Grover para n qubits y un estado marcado.
    - k_max: si None, usa el recomendado ~ pi/4 * sqrt(N)
    - verbose: imprime amplitudes en init/oracle/diffusion
    """
    validar_marked(marked, n)
    N = 2**n
    k_opt = int(round((np.pi/4) * np.sqrt(N)))
    if k_max is None:
        k_max = max(1, k_opt)

    qc = QuantumCircuit(n)
    preparar_superposicion(qc)

    sv = Statevector.from_instruction(qc)
    if verbose:
        imprimir_amplitudes(sv.data, n, marked, "Estado inicial |s>")

    print(f"\nGrover esencia — n={n}, N={N}, marked=|{marked}>")
    print(f"k recomendado ≈ round(pi/4*sqrt(N)) = {k_opt}\n")

    # k=0
    print(f"k=0  P(marked) = {prob_marked(sv.data, marked):.6f}")

    # Iteraciones
    for k in range(1, k_max + 1):
        oracle_phase_flip(qc, marked)
        sv_or = Statevector.from_instruction(qc)
        if verbose:
            imprimir_amplitudes(sv_or.data, n, marked, f"k={k} después de ORÁCULO")

        diffusion(qc)
        sv = Statevector.from_instruction(qc)

        p = prob_marked(sv.data, marked)
        print(f"k={k}  P(marked) = {p:.6f}")

        if verbose:
            imprimir_amplitudes(sv.data, n, marked, f"k={k} después de DIFUSIÓN  (P={p:.6f})")


if __name__ == "__main__":
    n = 2
    marked = "00"     # estado objetivo |w>
    # k_max = None -> usa el recomendado
    grover_esencia(n=n, marked=marked, k_max=None, verbose=False)

    # Si quieres verlo “con ojos”, activa verbose=True:
    # grover_esencia(n=n, marked=marked, k_max=3, verbose=True)
