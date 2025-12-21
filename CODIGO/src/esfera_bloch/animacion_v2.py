"""
Este programa anima en tiempo real la evolución de un qubit sobre la esfera de Bloch,
aplicando una secuencia de compuertas cuánticas como rotaciones 3D y mostrando su
trayectoria completa.
"""

import os

os.environ.pop("MPLBACKEND", None)

import matplotlib

matplotlib.use("TkAgg", force=True)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# =============================
#  Parámetros que puedes tocar
# =============================

# Estado inicial en la esfera de Bloch:
# |0>  -> theta=0,  phi=0  (polo norte)
# |1>  -> theta=pi, phi=0  (polo sur)
theta_0 = 0.0
phi_0 = 0.0

# Secuencia de compuertas a aplicar (en orden)
# Opciones implementadas: "X", "Y", "Z", "H", "S", "T"
GATE_SEQUENCE = ["H", "Z"]  # cámbiala como quieras, por ejemplo ["X"] o ["H","H"]

FRAMES_PER_GATE = 80  # cuántos pasos para cada compuerta (más = giro más suave)


# =============================
#  Funciones auxiliares
# =============================


def bloch_vector_from_angles(theta: float, phi: float) -> np.ndarray:
    """Convierte (theta, phi) en un vector 3D sobre la esfera de Bloch."""
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def rotation_matrix(axis: np.ndarray, angle: float) -> np.ndarray:
    """Matriz de rotación 3x3 usando la fórmula de Rodrigues."""
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
        ]
    )


def get_gate_rotation(gate_name: str):
    """
    Devuelve (axis, angle) para una compuerta.
    Todas son rotaciones SU(2) -> SO(3) hasta fase global.
    """
    gate_name = gate_name.upper()

    if gate_name == "X":
        axis = np.array([1, 0, 0])
        angle = np.pi  # Rx(pi)
    elif gate_name == "Y":
        axis = np.array([0, 1, 0])
        angle = np.pi  # Ry(pi)
    elif gate_name == "Z":
        axis = np.array([0, 0, 1])
        angle = np.pi  # Rz(pi)
    elif gate_name == "H":
        axis = np.array([1, 0, 1])  # (X+Z)/sqrt(2)
        axis = axis / np.linalg.norm(axis)
        angle = np.pi
        return axis, angle
    elif gate_name == "S":
        axis = np.array([0, 0, 1])
        angle = np.pi / 2  # Rz(pi/2)
    elif gate_name == "T":
        axis = np.array([0, 0, 1])
        angle = np.pi / 4  # Rz(pi/4)
    else:
        raise ValueError(f"Compuerta no soportada: {gate_name}")

    axis = axis / np.linalg.norm(axis)
    return axis, angle


def plot_bloch_sphere(ax):
    """Dibuja la esfera de Bloch y los ejes."""
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z, alpha=0.12, color="#9ec9ff", edgecolor="none")

    # ejes cartesianos
    ax.quiver(0, 0, 0, 1, 0, 0, color="gray", arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 1, 0, color="gray", arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 0, 1, color="gray", arrow_length_ratio=0.08)

    ax.text(1.05, 0, 0, "X")
    ax.text(0, 1.05, 0, "Y")
    ax.text(0, 0, 1.05, "Z")

    for axis in [ax.set_xlim, ax.set_ylim, ax.set_zlim]:
        axis([-1.1, 1.1])

    ax.set_box_aspect([1, 1, 1])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# =============================
#  Precomputar trayectoria
# =============================


def build_trajectory():
    """
    Genera todos los vectores intermedios para la secuencia de compuertas.
    Devuelve:
        vectors: lista de vectores 3D
        gate_labels: lista del mismo largo con el nombre de la compuerta de ese tramo
    """
    v_start = bloch_vector_from_angles(theta_0, phi_0)
    vectors = []
    gate_labels = []

    for gate in GATE_SEQUENCE:
        axis, angle_total = get_gate_rotation(gate)

        for step in range(FRAMES_PER_GATE):
            t = step / (FRAMES_PER_GATE - 1)
            R = rotation_matrix(axis, t * angle_total)
            v_step = R @ v_start
            v_step = v_step / np.linalg.norm(v_step)
            vectors.append(v_step)
            gate_labels.append(gate)

        # actualizar estado para la siguiente compuerta
        R_full = rotation_matrix(axis, angle_total)
        v_start = R_full @ v_start
        v_start = v_start / np.linalg.norm(v_start)

    return np.array(vectors), gate_labels


# =============================
#  Animación
# =============================


def main():
    vectors, gate_labels = build_trajectory()

    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")

    plot_bloch_sphere(ax)

    # vector inicial (solo para contexto, en rojo)
    v0 = vectors[0]
    ax.quiver(
        0,
        0,
        0,
        v0[0],
        v0[1],
        v0[2],
        color="red",
        linewidth=2,
        arrow_length_ratio=0.15,
        label="Estado inicial",
    )

    # vector dinámico (azul), lo actualizamos en la animación
    v_init = vectors[0]
    arrow = ax.quiver(
        0,
        0,
        0,
        v_init[0],
        v_init[1],
        v_init[2],
        color="blue",
        linewidth=2.5,
        arrow_length_ratio=0.18,
        label="Estado actual",
    )

    # trayectoria (línea morada)
    traj_x = [v_init[0]]
    traj_y = [v_init[1]]
    traj_z = [v_init[2]]
    (traj_line,) = ax.plot(
        traj_x,
        traj_y,
        traj_z,
        linestyle="--",
        linewidth=2,
        color="purple",
        label="Trayectoria",
    )

    # texto con la compuerta actual
    title = ax.set_title("Esfera de Bloch – Animación")

    ax.legend(loc="upper left")

    state = {
        "arrow": arrow,
        "traj_x": traj_x,
        "traj_y": traj_y,
        "traj_z": traj_z,
        "traj_line": traj_line,
        "title": title,
    }

    def update(frame):
        v = vectors[frame]
        gate = gate_labels[frame]

        # actualizar trayectoria
        state["traj_x"].append(v[0])
        state["traj_y"].append(v[1])
        state["traj_z"].append(v[2])

        state["traj_line"].set_data(state["traj_x"], state["traj_y"])
        state["traj_line"].set_3d_properties(state["traj_z"])

        # actualizar flecha azul (remover y volver a crear)
        state["arrow"].remove()
        state["arrow"] = ax.quiver(
            0,
            0,
            0,
            v[0],
            v[1],
            v[2],
            color="blue",
            linewidth=2.5,
            arrow_length_ratio=0.18,
        )

        state["title"].set_text(
            f"Esfera de Bloch – Gate {gate} (frame {frame+1}/{len(vectors)})"
        )

        return state["arrow"], state["traj_line"], state["title"]

    anim = FuncAnimation(
        fig,
        update,
        frames=len(vectors),
        interval=40,  # ms entre frames (ajusta para más lento/rápido)
        blit=False,
    )

    # vista bonita para ver casi toda la esfera
    ax.view_init(elev=25, azim=40)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
