"""
Este programa simula la medición de un qubit usando su representación en la esfera de
Bloch, aplica una secuencia de compuertas, genera resultados probabilísticos tipo
Monte Carlo y guarda todas las mediciones en un archivo CSV para su análisis.
"""

import numpy as np
import csv

# =============================
#  Configuración del experimento
# =============================

# Ángulos iniciales del qubit en la esfera de Bloch
# (puedes cambiarlos libremente)
THETA_0 = 0.8
PHI_0 = 0.8

# Secuencia de compuertas (en orden)
# Soportadas: "I", "X", "Y", "Z", "H", "S", "T", "RX", "RY", "RZ"
GATE_SEQUENCE = ["I"]

# Número de mediciones (shots)
SHOTS = 10_000

# Nombre del archivo CSV de salida
CSV_FILENAME = "python/esferaBloch/mediciones/mediciones_experimento_I.csv"


# =============================
#  Funciones de Bloch / Rotación
# =============================


def bloch_vector_from_angles(theta: float, phi: float) -> np.ndarray:
    """
    Convierte (theta, phi) en un vector (x, y, z) en la esfera de Bloch.
    """
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z], dtype=float)


def rotation_matrix(axis: np.ndarray, angle: float) -> np.ndarray:
    """
    Matriz de rotación 3D alrededor de 'axis' con ángulo 'angle'.
    Eje: vector de 3 componentes.
    """
    axis = axis / np.linalg.norm(axis)
    ux, uy, uz = axis
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    return np.array(
        [
            [
                cos_a + ux**2 * (1 - cos_a),
                ux * uy * (1 - cos_a) - uz * sin_a,
                ux * uz * (1 - cos_a) + uy * sin_a,
            ],
            [
                uy * ux * (1 - cos_a) + uz * sin_a,
                cos_a + uy**2 * (1 - cos_a),
                uy * uz * (1 - cos_a) - ux * sin_a,
            ],
            [
                uz * ux * (1 - cos_a) - uy * sin_a,
                uz * uy * (1 - cos_a) + ux * sin_a,
                cos_a + uz**2 * (1 - cos_a),
            ],
        ],
        dtype=float,
    )


def get_gate_rotation(gate_name: str):
    """
    Devuelve (axis, angle) para una compuerta de un qubit.
    Modelamos SU(2) -> SO(3) (ignorando fase global).

    Soportadas:
    - I  = identidad (ángulo 0)
    - X  = Rx(pi)
    - Y  = Ry(pi)
    - Z  = Rz(pi)
    - H  = rotación pi alrededor de (X+Z)/sqrt(2)
    - S  = Rz(pi/2)
    - T  = Rz(pi/4)
    - RX = Rx(pi/2)
    - RY = Ry(pi/2)
    - RZ = Rz(pi/2)
    """
    gate_name = gate_name.upper()

    if gate_name == "I":
        axis = np.array([1.0, 0.0, 0.0])
        angle = 0.0

    elif gate_name == "X":
        axis = np.array([1.0, 0.0, 0.0])
        angle = np.pi

    elif gate_name == "Y":
        axis = np.array([0.0, 1.0, 0.0])
        angle = np.pi

    elif gate_name == "Z":
        axis = np.array([0.0, 0.0, 1.0])
        angle = np.pi

    elif gate_name == "H":
        axis = np.array([1.0, 0.0, 1.0])  # (X+Z)/sqrt(2)
        axis = axis / np.linalg.norm(axis)
        angle = np.pi

    elif gate_name == "S":
        axis = np.array([0.0, 0.0, 1.0])
        angle = np.pi / 2

    elif gate_name == "T":
        axis = np.array([0.0, 0.0, 1.0])
        angle = np.pi / 4

    elif gate_name == "RX":
        axis = np.array([1.0, 0.0, 0.0])
        angle = np.pi / 2

    elif gate_name == "RY":
        axis = np.array([0.0, 1.0, 0.0])
        angle = np.pi / 2

    elif gate_name == "RZ":
        axis = np.array([0.0, 0.0, 1.0])
        angle = np.pi / 2

    else:
        raise ValueError(f"Compuerta no soportada: {gate_name}")

    return axis, angle


def apply_gates_to_bloch(theta: float, phi: float, gate_sequence):
    """
    Aplica una secuencia de compuertas (modeladas como rotaciones)
    a un estado inicial definido por (theta, phi) en la esfera de Bloch.

    Devuelve el vector final (x, y, z).
    """
    v = bloch_vector_from_angles(theta, phi)

    for gate in gate_sequence:
        axis, angle = get_gate_rotation(gate)
        R = rotation_matrix(axis, angle)
        v = R @ v
        # normalizar por seguridad numérica
        v = v / np.linalg.norm(v)

    return v


# =============================
#  Medición y generación de CSV
# =============================


def sample_measurements_from_bloch(
    theta: float, phi: float, gate_sequence, shots=10_000
):
    """
    - Calcula el vector final en Bloch tras aplicar las compuertas.
    - Usa z_final para definir P(0), P(1).
    - Genera 'shots' mediciones.
    - Devuelve (resultados, z_final, P0, P1).
    """
    v_final = apply_gates_to_bloch(theta, phi, gate_sequence)
    z_final = float(v_final[2])

    # Probabilidades cuánticas reales en base Z
    p0 = (1.0 + z_final) / 2.0
    p0 = float(np.clip(p0, 0.0, 1.0))  # asegurar intervalo [0, 1]
    p1 = 1.0 - p0

    results = []
    for _ in range(shots):
        r = np.random.rand()
        if r < p0:
            results.append(0)
        else:
            results.append(1)

    return results, z_final, p0, p1


def main():
    results, z_final, p0, p1 = sample_measurements_from_bloch(
        THETA_0, PHI_0, GATE_SEQUENCE, shots=SHOTS
    )

    print(f"Vector final z = {z_final:.4f}")
    print(f"P(0) teórica = {p0:.4f},  P(1) teórica = {p1:.4f}")
    print(
        f"Tiros = {SHOTS},  conteo 0 = {results.count(0)},  conteo 1 = {results.count(1)}"
    )

    gate_str = " ".join(GATE_SEQUENCE)

    # Guardar en CSV
    with open(CSV_FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "theta",
                "phi",
                "z_final",
                "P0_teorica",
                "P1_teorica",
                "secuencia_gates",
                "resultado",
            ]
        )
        for r in results:
            writer.writerow([THETA_0, PHI_0, z_final, p0, p1, gate_str, r])


if __name__ == "__main__":
    main()
