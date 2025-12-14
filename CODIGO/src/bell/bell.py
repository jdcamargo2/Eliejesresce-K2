"""
Genera el estado de Bell |Ψ->, muestra su vector de estado y simula la medición
para observar las correlaciones propias del entrelazamiento.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


def main():
    # 1) Creamos el circuito de 2 qubits
    qc = QuantumCircuit(2, 2)

    # Hadamard en el primer qubit
    qc.h(0)  # H: qubit 0

    # CNOT: control=0, target=1
    qc.cx(0, 1)  # CNOT: qubit 0 -> qubit 1

    # X en el segundo qubit
    qc.x(1)  # X: Qubit 1

    # Z en el segundo qubit
    qc.z(1)  # Z: Qubit 1

    print("Circuito que genera |Ψ->:\n")
    print(qc.draw())

    statevector = Statevector.from_instruction(qc)

    print("\nStatevactor resultante:")
    print(statevector)

    meas = qc.copy()

    # Forma Controlada
    # meas.measure(0, 0)
    # meas.measure(1, 1)

    # Forma en tuplas
    meas.measure([0, 1], [0, 1])

    # Simulador
    sim = AerSimulator()
    # Ejecución del circuito medido
    job = sim.run(meas, shots=1000)
    result = job.result()
    counts = result.get_counts()

    print("\nConteos:")
    print(counts)


if __name__ == "__main__":
    main()
