"""
Muestra de forma explícita cuatro postulados cuánticos con un solo qubit.
Se representa el estado como vector normalizado, se lo prepara mediante
evolución unitaria, se relaciona esa evolución con la ecuación de Schrödinger
y se compara la medición teórica con la observada en base Z y base X.
"""

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator


# =====================================================================
# UTILIDAD DE PRESENTACIÓN
# =====================================================================

def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# =====================================================================
# POSTULADO I
# El estado cuántico está representado por un vector normalizado
# en un espacio de Hilbert complejo.
# =====================================================================

def show_postulate_I(circuit: QuantumCircuit) -> Statevector:
    sv = Statevector.from_instruction(circuit)

    print_separator("POSTULADO I — ESTADO CUÁNTICO")
    print("Circuito de preparación:")
    print(circuit.draw(output="text"))

    print("Vector de estado |ψ⟩:")
    print(sv)

    alpha, beta = sv.data
    norm = abs(alpha) ** 2 + abs(beta) ** 2

    print("\nAmplitudes complejas:")
    print(f"α (amplitud de |0⟩) = {alpha}")
    print(f"β (amplitud de |1⟩) = {beta}")

    print(f"\nNorma del estado = {norm:.6f}")
    print("Interpretación: si la norma es 1, el estado representa un estado físico válido.")

    return sv


# =====================================================================
# POSTULADO II
# La evolución del sistema cerrado se representa mediante operadores
# unitarios.
# =====================================================================

def show_postulate_II() -> None:
    print_separator("POSTULADO II — EVOLUCIÓN UNITARIA")
    print("Las compuertas cuánticas ideales transforman el estado mediante")
    print("operadores unitarios. En este ejemplo, el estado se prepara con:")
    print("H seguido de S")
    print("\nEso significa que:")
    print("|ψ⟩ = S H |0⟩")
    print("\nCondición de unitariedad:")
    print("U†U = I")
    print("\nInterpretación:")
    print("La evolución conserva la norma del estado y, por tanto, preserva")
    print("la estructura probabilística del sistema.")


# =====================================================================
# POSTULADO IV
# La evolución temporal está gobernada por la ecuación de Schrödinger.
# =====================================================================

def show_postulate_IV() -> None:
    print_separator("POSTULADO IV — ECUACIÓN DE SCHRÖDINGER")
    print("La evolución temporal de un sistema cuántico cerrado obedece:")
    print("iħ ∂|ψ(t)⟩/∂t = H|ψ(t)⟩")

    print("\nSu solución formal puede escribirse como:")
    print("U(t) = exp(-iHt/ħ)")

    print("\nInterpretación:")
    print("Las compuertas cuánticas ideales pueden verse como evoluciones")
    print("unitarias discretas generadas por un Hamiltoniano durante cierto tiempo.")
    print("Por eso, en el código no resolvemos explícitamente Schrödinger,")
    print("pero sí usamos su consecuencia operacional: los operadores unitarios.")


# =====================================================================
# POSTULADO III
# La medición produce resultados según la regla de Born y el estado
# colapsa a un eigenestado compatible con el resultado observado.
# =====================================================================

def theoretical_probabilities(state: Statevector, basis: str) -> dict:
    if basis.upper() == "Z":
        return state.probabilities_dict()

    if basis.upper() == "X":
        qc_h = QuantumCircuit(1)
        qc_h.h(0)
        rotated_state = state.evolve(qc_h)
        return rotated_state.probabilities_dict()

    raise ValueError("La base debe ser 'Z' o 'X'.")


def measure_counts(circuit: QuantumCircuit, basis: str, shots: int = 4096) -> dict:
    qc = circuit.copy()

    if basis.upper() == "X":
        qc.h(0)
    elif basis.upper() != "Z":
        raise ValueError("La base debe ser 'Z' o 'X'.")

    qc.measure_all()

    simulator = AerSimulator()
    result = simulator.run(qc, shots=shots).result()
    return result.get_counts()


def show_measurement_analysis(circuit: QuantumCircuit, state: Statevector, basis: str, shots: int = 4096) -> None:
    print_separator(f"POSTULADO III — MEDICIÓN EN BASE {basis.upper()}")

    counts = measure_counts(circuit, basis, shots)
    probs_theory = theoretical_probabilities(state, basis)

    print("Probabilidades teóricas (regla de Born):")
    for outcome, prob in sorted(probs_theory.items()):
        print(f"P_teórica({outcome}) = {prob:.6f}")

    print("\nFrecuencias observadas:")
    for outcome, count in sorted(counts.items()):
        print(f"P_observada({outcome}) = {count / shots:.6f}")

    print("\nInterpretación:")
    print("Las frecuencias observadas se aproximan a las probabilidades teóricas")
    print("cuando el número de mediciones es suficientemente grande.")


def show_collapse(state: Statevector, basis: str) -> None:
    print_separator(f"POSTULADO III — COLAPSO EN BASE {basis.upper()}")

    if basis.upper() == "Z":
        outcome, collapsed_state = state.measure()

    elif basis.upper() == "X":
        qc_h = QuantumCircuit(1)
        qc_h.h(0)

        rotated_state = state.evolve(qc_h)
        outcome, collapsed_rotated = rotated_state.measure()
        collapsed_state = collapsed_rotated.evolve(qc_h)

    else:
        raise ValueError("La base debe ser 'Z' o 'X'.")

    print(f"Resultado individual obtenido: {outcome}")
    print("Estado después de la medición:")
    print(collapsed_state)

    print("\nInterpretación:")
    print("Después de medir, la superposición original deja de describir al sistema.")
    print("El estado colapsa a un eigenestado compatible con el resultado observado.")


# =====================================================================
# PROGRAMA PRINCIPAL
# Un único experimento: preparar |ψ⟩ = (|0⟩ + i|1⟩)/√2 = S H |0⟩
# =====================================================================

print_separator("EXPERIMENTO ÚNICO — EXPLORACIÓN DE LOS POSTULADOS")

# Estado inicial |0⟩ y evolución unitaria H seguido de S
qc = QuantumCircuit(1)
qc.h(0)
qc.s(0)

# Postulado II
show_postulate_II()

# Postulado IV
show_postulate_IV()

# Postulado I
state = show_postulate_I(qc)

print("\nEstado preparado:")
print("|ψ⟩ = S H |0⟩ = (|0⟩ + i|1⟩) / √2")

# Postulado III en base Z
show_measurement_analysis(qc, state, "Z")
show_collapse(state, "Z")

# Postulado III en base X
show_measurement_analysis(qc, state, "X")
show_collapse(state, "X")