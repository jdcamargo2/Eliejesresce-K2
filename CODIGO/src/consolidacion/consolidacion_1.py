"""
Muestra cómo un cambio de fase se vuelve observable
cuando se fuerza la interferencia.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

opcion = "A"

if opcion == "A":
    qc.h(0)

if opcion == "B":
    qc.h(0)
    qc.z(0)
    qc.h(0)

qc.measure(0, 0)

simulator = AerSimulator()
result = simulator.run(qc, shots=1).result()
counts = result.get_counts(qc)

print("Counts:", counts)
print(qc.draw())


""" 
Explicación de las mediciones en diferentes bases en Qiskit
=============================================================

En este código podemos ver dos estados y ejemplos de medición en diferentes bases.

En la opción A, preparamos a partir de un Hamadard un estado |+>, 
al medir tendremos una probabilidad del 50% de obtener |0> y 50% de 
obtener |1>.

En la opción B, preparamos un estado |-> al aplicar una puerta Z entre las
puertas Hamadard, esto provoca que exista un cambio de fase que genera una medición
distinta. Al aplicar el segundo hamadard forzamos al estado a ir hacía |1>, por tanto
al medir después de aplicar el segundo Hamadard, obtenemos solo |1> como resultado.
El estado |0> se cancelo por interferencia.

"""
