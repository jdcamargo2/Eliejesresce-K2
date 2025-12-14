"""
Este programa crea un circuito cuántico con una compuerta X seguida de una H,
calcula el vector de estado resultante usando Statevector y muestra cómo cambian
los signos y amplitudes del estado cuántico.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector  # <--- ¡Esta es la herramienta clave!

# 1. Caso Destructivo (Con X -> H)
qc = QuantumCircuit(1)
qc.x(0)
qc.h(0)

# Calculo del estado matemático de este circuito por statevector.
vector = Statevector.from_instruction(qc)

print("El Vector de Estado (mira los signos):")
print(vector)
