"""
Implementa el protocolo de teleportación cuántica de un qubit |ψ> usando un par
entrelazado, Bell measurement y correcciones clásicas sobre el qubit de Bob.
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

sim = AerSimulator()
# Contiene
# q0: |psi> (Qubit desconocido)
# q1: Alice en bell
# q2: Bob en bell
q = QuantumRegister(3, "q")
c0 = ClassicalRegister(1, "c0")  # mide q0
c1 = ClassicalRegister(1, "c1")  # mide q1
cb = ClassicalRegister(1, "cb")  # mide bob
qc = QuantumCircuit(q, c0, c1, cb)

# Paso 1, preparamos |psi> (Qubit desconocido)
# Si no hay nada es |0>
# Para el estado |1> usamos X
# Para |+> usamos H
# Para |-> usamos H y Z o X y H
# Para |i+> usamos H y S
# Para |i-> usamos H y S y X
qc.h(0)


# Paso 2, creamos el phi+ entre q1 y q2
qc.h(1)
qc.cx(1, 2)

# Paso 3, creamos Bell Measurement entre q0 y q1
qc.cx(0, 1)
qc.h(0)

# Paso 4, medimos los qubits de Alice
qc.measure(0, c0[0])
qc.measure(1, c1[0])

# Paso 5, hacemos correciones en Bob
with qc.if_test((c1, 1)):
    qc.x(2)
with qc.if_test((c0, 1)):
    qc.z(2)

# Paso 6, medimos en Bob

# ===================== MEDICIÓN EN DIFERENTES BASES (para verificar estados) =====================
# Qiskit mide SIEMPRE en la base computacional Z: {|0>, |1>}.
# Para "medir en otra base", NO cambias la medición: rotas el qubit ANTES de medirlo,
# para que esa base se convierta en Z.
#
# --- Medir en base Z (computacional) ---
# Útil para verificar estados tipo |0> y |1>.
#   (no aplicar nada)
#   qc.measure(qb, cb)
#
# --- Medir en base X (Hadamard / estados |+>, |->) ---
# Base X = {|+>, |->}.  H mapea: |+> -> |0>, |-> -> |1>.
# Útil para verificar estados:
#   |+>  (debería dar 0 casi siempre)
#   |->  (debería dar 1 casi siempre)
#   qc.h(qb)
#   qc.measure(qb, cb)
#
# --- Medir en base Y (fase / estados |i+>, |i->) ---
# Base Y = {|i+>, |i->}.  S† y luego H mapean:
#   |i+> -> |0>, |i-> -> |1>.
# Útil para verificar estados:
#   |i+> (debería dar 0 casi siempre)
#   |i-> (debería dar 1 casi siempre)
#   qc.sdg(qb)   # S-dagger
#   qc.h(qb)
#   qc.measure(qb, cb)
#
# NOTA IMPORTANTE EN TELEPORTACIÓN:
# - Primero: medir Alice (c0,c1)
# - Luego: aplicar correcciones en Bob (X/Z condicionadas)
# - Luego: (opcional) cambio de base para verificación (H o Sdg+H)
# - Finalmente: medir Bob
# ================================================================================================

qc.h(2)
qc.measure(2, cb[0])

result = sim.run(qc, shots=4000).result()
counts = result.get_counts()
print("Teleportación de |psi>:", counts)
print(qc.draw())
