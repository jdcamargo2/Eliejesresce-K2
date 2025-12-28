"""
Implementación del algoritmo de Deutsch–Jozsa en Qiskit para distinguir
funciones constantes y balanceadas mediante interferencia cuántica.
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np


def oraculo_constante(qubits: int, valor: int = 0) -> QuantumCircuit:
    """
    Oráculo constante:
      f(x) = 0  -> no hace nada
      f(x) = 1  -> hace X al qubit auxiliar (flip siempre)
    Implementa Uf: |x>|y> -> |x>|y XOR f(x)>
    """
    qc = QuantumCircuit(qubits + 1)  # + 1 es para el qubit auxiliar
    qubit_aux = qubits

    if valor == 1:
        qc.x(qubit_aux)

    return qc


def oraculo_balanceado(qubits: int) -> QuantumCircuit:
    """
    Oráculo balanceado:
      f(x) = x0 XOR x1 XOR ... XOR x_{n-1}
    Implementación:
      aplicar CNOT desde cada qubit de entrada hacia el qubit auxiliar
    """

    qc = QuantumCircuit(qubits + 1)  # +1 para el qubit auxiliar
    qubit_aux = qubits

    qc.cx(0, qubit_aux)

    return qc


def dj_algoritmo(qubits: int, oraculo: QuantumCircuit) -> QuantumCircuit:

    qc = QuantumCircuit(qubits + 1, qubits)  # +1 para el qubit auxiliar
    qubit_aux = qubits

    # Preparamos el qubit auxiliar en |1>
    qc.x(qubit_aux)

    # Creamos el estado de superposición para todos los qubits
    qc.h(range(qubits + 1))

    # Aplicamos el oráculo
    qc.compose(oraculo, inplace=True)

    # Aplicamos Hadamard nuevamente a los qubits de entrada
    # Ya no aplicamos al qubit auxiliar
    # qc.h(range(qubits))

    # Medimos los qubits de entrada
    qc.measure(range(qubits), range(qubits))

    return qc


def ejecutar_dj(qc: QuantumCircuit, shots: int = 1024):

    sim = AerSimulator()
    circuito_t = transpile(qc, sim)
    resultado = sim.run(circuito_t, shots=shots, memor=True).result()
    counts = resultado.get_counts()
    return counts


def clasificar(counts: dict, n: int) -> str:

    top = max(counts, key=counts.get)
    return "Constante" if top == "0" * n else "Balanceada"


if __name__ == "__main__":

    n = 3

    # Caso A: Oráculo constante f(x) = 0
    oraculo_c = oraculo_constante(n, valor=0)
    circuito_c = dj_algoritmo(n, oraculo_c)
    resultados_c = ejecutar_dj(circuito_c)
    print("Caso Constante f(x)=0:", resultados_c, "->", clasificar(resultados_c, n))

    # Caso B: Oráculo constante f(x) = 1
    oraculo_c1 = oraculo_constante(n, valor=1)
    circuito_c1 = dj_algoritmo(n, oraculo_c1)
    resultados_c1 = ejecutar_dj(circuito_c1)
    print("Caso Constante f(x)=1:", resultados_c1, "->", clasificar(resultados_c1, n))

    # Caso C: Oráculo balanceado
    oraculo_b = oraculo_balanceado(n)
    circuito_b = dj_algoritmo(n, oraculo_b)
    resultados_b = ejecutar_dj(circuito_b)
    print("Caso Balanceada:", resultados_b, "->", clasificar(resultados_b, n))
