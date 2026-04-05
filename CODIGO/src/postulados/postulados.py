"""
Explora los postulados cuánticos con un qubit en Qiskit.
Prepara estados, aplica evolución unitaria y compara las probabilidades
antes de medir con los resultados obtenidos al medir en base Z y en base X.
"""

from math import sqrt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def analyze_state(circuit: QuantumCircuit, label: str) -> Statevector:
    """Construye el estadovector asociado al circuito y muestra información útil."""
    sv = Statevector.from_instruction(circuit)

    print_separator(label)
    print("Circuito:")
    print(circuit.draw(output="text"))

    print("Estadovector:")
    print(sv)

    print("\nAmplitudes en la base computacional:")
    data = sv.data
    print(f"|0>: {data[0]}")
    print(f"|1>: {data[1]}")

    print("\nProbabilidades de medición en Z:")
    probs = sv.probabilities_dict()
    for basis_state, prob in probs.items():
        print(f"P({basis_state}) = {prob:.6f}")

    return sv


def simulate_measurement_in_z(circuit: QuantumCircuit) -> None:
    """Muestra cómo se vería la medición en la base computacional Z."""
    qc = circuit.copy()
    qc.measure_all()

    print_separator("MEDICIÓN EN Z")
    print(qc.draw(output="text"))
    print(
        "Interpretación: aquí el circuito termina proyectando el estado "
        "sobre |0> o |1>."
    )


def simulate_measurement_in_x(circuit: QuantumCircuit) -> None:
    """
    Mide 'en X' cambiando primero la base con una Hadamard.
    En práctica, medir en X equivale a aplicar H y luego medir en Z.
    """
    qc = circuit.copy()
    qc.h(0)
    qc.measure_all()

    print_separator("MEDICIÓN EN X (cambio de base con H antes de medir)")
    print(qc.draw(output="text"))
    print(
        "Interpretación: no existe una instrucción mágica 'measure_x'; "
        "se cambia la base y luego se mide en Z."
    )


# -------------------------------------------------------------------
# EXPERIMENTO 1: estado |+> = (|0> + |1>) / sqrt(2)
# -------------------------------------------------------------------

qc_plus = QuantumCircuit(1)
qc_plus.h(0)

analyze_state(qc_plus, "ESTADO |+> PREPARADO CON H|0>")
simulate_measurement_in_z(qc_plus)
simulate_measurement_in_x(qc_plus)

# -------------------------------------------------------------------
# EXPERIMENTO 2: estado |1>
# -------------------------------------------------------------------

qc_one = QuantumCircuit(1)
qc_one.x(0)

analyze_state(qc_one, "ESTADO |1> PREPARADO CON X|0>")
simulate_measurement_in_z(qc_one)
simulate_measurement_in_x(qc_one)

# -------------------------------------------------------------------
# EXPERIMENTO 3: estado arbitrario con fase
# |psi> = (|0> + i|1>) / sqrt(2)
# -------------------------------------------------------------------

qc_phase = QuantumCircuit(1)
qc_phase.initialize([1 / sqrt(2), 1j / sqrt(2)], 0)

analyze_state(qc_phase, "ESTADO CON FASE RELATIVA (|0> + i|1>) / sqrt(2)")
simulate_measurement_in_z(qc_phase)
simulate_measurement_in_x(qc_phase)

print_separator("LECTURA FÍSICA")
print(
    "1) El estado vive como vector complejo antes de medir.\n"
    "2) Las compuertas H y X actúan como operadores unitarios.\n"
    "3) La medición final obliga al sistema a dar un resultado en una base.\n"
    "4) Cambiar la base antes de medir cambia qué información puedes revelar."
)