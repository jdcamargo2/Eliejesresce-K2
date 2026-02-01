"""
Este script demuestra cómo el método Matrix Product State (MPS)
permite simular circuitos cuánticos con muchos qubits,
evitando el consumo exponencial de memoria del statevector.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


# 1. Definición del circuito
#    Se construye un estado GHZ con un número grande de qubits
n_qubits = 50
qc = QuantumCircuit(n_qubits)

# Superposición inicial
qc.h(0)

# Entrelazamiento en cadena (GHZ)
for i in range(n_qubits - 1):
    qc.cx(i, i + 1)

# Medición de todos los qubits
qc.measure_all()


# 2. Configuración del simulador
#    Método MPS: eficiente para estados con bajo entrelazamiento local
simulator_mps = AerSimulator(method='matrix_product_state')

print(f"Simulando {n_qubits} qubits usando el método Matrix Product State (MPS)...")

# 3. Transpilación del circuito para el backend MPS
t_qc = transpile(qc, simulator_mps)

# 4. Ejecución del circuito
#    Aquí el costo principal no es la memoria exponencial,
#    sino la complejidad del entrelazamiento del estado
job = simulator_mps.run(t_qc, shots=1024)
result = job.result()

# 5. Resultados
print("Simulación completada con éxito ✔")
print(f"Conteos de medición: {result.get_counts()}")
