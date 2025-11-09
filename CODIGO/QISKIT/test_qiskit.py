from qiskit import QuantumCircuit

# Creamos un circuito cuántico de 2 qubits
qc = QuantumCircuit(2)

# Le aplicamos Hadamard al qubit 0 para ponerlo en superposición
qc.h(0)

# Aplicamos una compuerta CX (control en q0, objetivo q1) para entrelazar
qc.cx(0, 1)

# Imprimimos el diagrama del circuito en texto
print(qc.draw('text'))
