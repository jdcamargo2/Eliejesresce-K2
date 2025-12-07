"""
Este programa crea un circuito cuántico de un solo qubit, aplica dos compuertas Hadamard,
ejecuta una simulación con 1000 repeticiones y muestra la distribución de resultados
obtenidos al medir el qubit.
"""

from qiskit import QuantumCircuit  # Circuito cuántico
from qiskit_aer import AerSimulator  # Simulador AER

# Crear un cicuito cuántico
qc = QuantumCircuit(1, 1)

# Aplicar una compuerta cuántica
qc.h(0)
qc.h(0)

# Medir el qubit
qc.measure(0, 0)

# Configurar el simulador AER
sim = AerSimulator()

# Ejecutar un trabajo en el simulador
job = sim.run(qc, shots=1000)

# Obtener los resultados
result = job.result()

# Obtener el conteo de los resultados
counts = result.get_counts(qc)

# Imprimir el resultado
print(result.get_counts())
