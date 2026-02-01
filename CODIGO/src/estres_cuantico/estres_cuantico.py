"""
Este script prueba el límite práctico de una PC al simular estados cuánticos.
Construye un estado GHZ con un número creciente de qubits y mide
cuándo la simulación por statevector deja de ser viable por recursos.
"""

import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import time


def test_quantum_limit(n_qubits):
    """
    Crea y simula un circuito GHZ de n_qubits usando simulación por statevector.
    Mide el tiempo de ejecución y detecta fallos por límite de memoria o CPU.
    """

    # 1. Crear el circuito cuántico
    #    Estado GHZ: superposición global y entrelazamiento completo
    qc = QuantumCircuit(n_qubits)
    qc.h(0)  # Pone el primer qubit en superposición

    # Encadena compuertas CNOT para entrelazar todos los qubits
    for i in range(n_qubits - 1):
        qc.cx(i, i + 1)

    # Medición de todos los qubits
    qc.measure_all()

    # 2. Configurar el simulador
    #    Se fuerza el método 'statevector', que consume 2^n amplitudes en RAM
    simulator = AerSimulator(method='statevector')

    print(f"\n--- Probando con {n_qubits} qubits ---")
    start_time = time.time()

    try:
        # 3. Transpilación del circuito para el backend seleccionado
        t_qc = transpile(qc, simulator)

        # 4. Ejecución del circuito
        #    Un solo shot es suficiente; el costo real está en el statevector
        result = simulator.run(t_qc, shots=1).result()

        end_time = time.time()
        print(f"Éxito ✔ | Tiempo de ejecución: {end_time - start_time:.2f} segundos")

    except Exception as e:
        # Captura errores típicos de falta de memoria o recursos del sistema
        print("FALLO ✖ | Límite de hardware alcanzado")
        print(f"Detalle del error: {e}")


# 5. Barrido de número de qubits
#    Aumenta progresivamente hasta que el sistema no pueda sostener la simulación
for n in range(24, 35):
    test_quantum_limit(n)
