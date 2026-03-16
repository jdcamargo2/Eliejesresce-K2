"""
Construye estados GHZ de tamaño creciente en Qiskit y fuerza al simulador
a generar el statevector completo para medir hasta qué número de qubits
puede sostener la simulación clásica. El resultado se valida observando
si el cálculo termina con éxito, su tiempo de ejecución y la dimensión del vector.
"""

import time
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np


def test_quantum_limit(n_qubits):
    qc = QuantumCircuit(n_qubits)
    qc.h(0)

    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)

    # Forzar al simulador a construir y guardar el statevector
    qc.save_statevector()

    simulator = AerSimulator(method="statevector")

    print(f"\n--- Probando con {n_qubits} qubits ---")
    start_time = time.time()

    try:
        result = simulator.run(qc).result()
        statevector = result.data(0)["statevector"]  # fuerza acceso real al vector
        end_time = time.time()

        print(f"Éxito ✔ | Tiempo: {end_time - start_time:.4f} s")
        print(f"Dimensión del statevector: {len(np.asarray(statevector))}")

    except Exception as e:
        print("FALLO ✖")
        print(f"Detalle: {e}")


for n in range(24, 35):
    test_quantum_limit(n)