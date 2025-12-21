"""
Implementa la teleportación cuántica de un qubit en un estado arbitrario |ψ(θ, φ)⟩
usando un par de Bell y correcciones clásicas. El estado teleportado se verifica
midiendo el qubit de Bob en las bases Z, X y Y, comparando las probabilidades
observadas con las expectativas teóricas del vector de Bloch.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
import numpy as np


def teleport_patiño_state(theta, phi, basis="Z", shots=4096):
    q = QuantumRegister(3, "q")
    m0 = ClassicalRegister(1, "m0")  # mide q0
    m1 = ClassicalRegister(1, "m1")  # mide q1
    cb = ClassicalRegister(1, "cb")  # mide Bob q2
    qc = QuantumCircuit(q, m0, m1, cb)

    # 1) Estado misterioso en q0
    qc.ry(theta, q[0])
    qc.rz(phi, q[0])

    # 2) Par de Bell entre q1 (Alice) y q2 (Bob)
    qc.h(q[1])
    qc.cx(q[1], q[2])

    # 3) Bell measurement en (q0, q1)
    qc.cx(q[0], q[1])
    qc.h(q[0])
    qc.measure(q[0], m0[0])
    qc.measure(q[1], m1[0])

    # 4) Correcciones clásicas en Bob
    with qc.if_test((m1, 1)):
        qc.x(q[2])
    with qc.if_test((m0, 1)):
        qc.z(q[2])

    # 5) Medición de Bob en base elegida
    basis = basis.upper()
    if basis == "X":
        qc.h(q[2])
    elif basis == "Y":
        qc.sdg(q[2])
        qc.h(q[2])
    elif basis == "Z":
        pass
    else:
        raise ValueError("basis debe ser 'Z', 'X' o 'Y'")

    qc.measure(q[2], cb[0])

    sim = AerSimulator()
    tqc = transpile(qc)
    result = sim.run(tqc, shots=shots).result()
    return qc, result.get_counts()


def validacion_bob(counts):
    total = sum(counts.values())
    zeros = 0
    for key, v in counts.items():
        # key típico: 'cb m1 m0' (con espacios)
        cb_bit = key.strip().split()[0]
        if cb_bit == "0":
            zeros += v
    return zeros / total


# Parámetros del estado
theta = np.pi / 3
phi = np.pi / 5
shots = 10000000

# Teoría esperada (CORRECTA)
Ez = np.cos(theta)
Ex = np.sin(theta) * np.cos(phi)
Ey = np.sin(theta) * np.sin(phi)

expected = {
    "Z": (1 + Ez) / 2,
    "X": (1 + Ex) / 2,
    "Y": (1 + Ey) / 2,
}

print("Esperados P(cb=0):", {k: float(round(v, 4)) for k, v in expected.items()})

# Experimento: medir a Bob en Z/X/Y
for basis in ["Z", "X", "Y"]:
    qc, counts = teleport_patiño_state(
        theta, phi, basis=basis, shots=shots
    )  # <- desempacado correcto
    p0 = validacion_bob(counts)
    print(f"\nBase {basis}")
    print(f"P(cb=0) observado ≈ {p0:.4f} | esperado ≈ {expected[basis]:.4f}")


"""
Resultados con 10.000.000 de shots:

Esperados P(cb=0): {'Z': 0.75, 'X': 0.8503, 'Y': 0.7545}

Base Z
P(cb=0) observado ≈ 0.7499 | esperado ≈ 0.7500

Base X
P(cb=0) observado ≈ 0.8502 | esperado ≈ 0.8503

Base Y
P(cb=0) observado ≈ 0.7545 | esperado ≈ 0.7545
"""
