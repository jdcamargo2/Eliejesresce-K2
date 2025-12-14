"""
Este programa crea un circuito cuántico de un solo qubit, aplica una rotación RX de π/2,
obtiene el vector de estado resultante y lo representa visualmente en la esfera de Bloch.
"""

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
import matplotlib.pyplot as plt

# 1. Creamos un circuito con 1 qubit
qc = QuantumCircuit(1)

# 2. Aplicamos la compuerta RX con ángulo Pi/2
# El estado inicial es por defecto |0>
qc.rx(np.pi / 2, 0)

# 3. Obtenemos el vector de estado resultante (la matemática pura)
estado = Statevector.from_instruction(qc)

# 4. Imprimimos los valores
print("Vector de estado resultante:")
print(estado)

# 5. Visualizamos en la esfera de Bloch
plot_bloch_multivector(estado)
