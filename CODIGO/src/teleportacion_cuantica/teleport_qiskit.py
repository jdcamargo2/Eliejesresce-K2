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
qc.measure(2, cb[0])

result = sim.run(qc, shots=4000).result()
counts = result.get_counts()
print("Teleportación de |psi>:", counts)
print(qc.draw())
