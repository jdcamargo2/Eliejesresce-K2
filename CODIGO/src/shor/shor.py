"""
Implementación IDEAL de Shor-21 mediante estimación de fase iterativa (IPE).
Aplica las unitarias controladas U^{2^j} sin ruido para verificar
la aparición correcta de picos en m/Q y extraer la periodicidad.
"""

from math import pi
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator


# -------------------------
# Parámetros del ejercicio (Día 57)
# -------------------------
N = 21
a = 2
n_control = 9          # Q = 2^9 = 512
n_work = 5             # Espacio suficiente para y < 21
Q = 2**n_control
SHOTS = 4096


def mul_mod_perm(k, n_work, N):
    """
    Permutación |y> → |k·y mod N>.
    Estados y ≥ N se dejan invariantes.
    """
    dim = 2**n_work
    perm = list(range(dim))
    for y in range(N):
        perm[y] = (k * y) % N
    return perm


# -------------------------
# Construcción del circuito (IPE)
# -------------------------
work = QuantumRegister(n_work, "w")
ctrl = QuantumRegister(1, "c")
c_out = ClassicalRegister(n_control, "m")
qc = QuantumCircuit(ctrl, work, c_out)

# Registro de trabajo en |1>
qc.x(work[0])

for j in range(n_control):
    # Superposición del qubit de control
    qc.h(ctrl[0])

    # U^{2^j} controlada
    k = pow(a, 2**j, N)
    perm = mul_mod_perm(k, n_work, N)

    dim = 2**n_work
    U = np.zeros((dim, dim), dtype=complex)
    for y, py in enumerate(perm):
        U[py, y] = 1.0

    inst = UnitaryGate(Operator(U)).control(1)
    qc.append(inst, [ctrl[0]] + list(work))

    # Correcciones de fase (feed-forward clásico)
    for i in range(j):
        angle = -pi / (2**(j - i))
        with qc.if_test((c_out[i], 1)):
            qc.p(angle, ctrl[0])

    # Conversión fase → bit
    qc.h(ctrl[0])
    qc.measure(ctrl[0], c_out[j])

    if j < n_control - 1:
        qc.reset(ctrl[0])


# -------------------------
# Simulación
# -------------------------
sim = AerSimulator()

tqc = transpile(qc, sim, optimization_level=0)

import time
print(f"\n--- Ejecutando Shor-21 ---")
start = time.time()

result = sim.run(tqc, shots=SHOTS).result()
counts = result.get_counts()

print(f"Tiempo: {time.time() - start:.2f}s")

# Resultados principales
top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:8]
for bits, ct in top:
    m = int(bits[::-1], 2)
    print(f"m: {m:3} | m/Q: {m/Q:.6f} | Prob: {ct/SHOTS:.2%}")
