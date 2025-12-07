"""
Este programa crea un estado entrelazado de dos qubits tipo |Φ+> usando H y CNOT,
calcula su vector de estado con un simulador cuántico y luego simula mediciones
para comprobar que solo aparecen los resultados 00 y 11.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator, StatevectorSimulator
import numpy as np


def main():
    # 1) Creamos el circuito de 2 qubits
    qc = QuantumCircuit(2, 2)

    # Hadamard en el primer qubit
    qc.h(0)

    # CNOT: control=0, target=1
    qc.cx(0, 1)

    print("Circuito que genera |Φ+>:\n")
    print(qc.draw())

    # 2) Simulador de vectores de estado (nuevo API)
    sv_sim = StatevectorSimulator()
    sv_job = sv_sim.run(qc)
    statevector = sv_job.result().get_statevector()

    print("\nStatevector del circuito:")
    print(statevector)

    # 3) Simulación con mediciones para ver 00 y 11
    meas = qc.copy()
    meas.measure(0, 0)
    meas.measure(1, 1)

    sim = AerSimulator()
    job = sim.run(meas, shots=1024)
    counts = job.result().get_counts()

    print("\nResultados de medición:")
    print(counts)


if __name__ == "__main__":
    main()
