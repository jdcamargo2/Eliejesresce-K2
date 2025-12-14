"""
Este programa visualiza una rotación de un estado cuántico sobre la esfera de Bloch,
mostrando el vector inicial, el eje de rotación, el vector transformado y la
trayectoria completa de la transformación.
"""

import os

os.environ.pop("MPLBACKEND", None)

import matplotlib

matplotlib.use("TkAgg", force=True)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# =============================
#  Funciones auxiliares
# =============================


def bloch_vector_from_angles(theta: float, phi: float) -> np.ndarray:
    """
    Convierte ángulos (theta, phi) en un vector 3D sobre la esfera de Bloch.

    theta: ángulo polar (0 a pi), medido desde el eje Z.
    phi:   ángulo azimutal (0 a 2*pi), alrededor del eje Z.
    """
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def rotation_matrix(axis: np.ndarray, angle: float) -> np.ndarray:
    """
    Matriz de rotación 3x3 usando la fórmula de Rodrigues.
    axis: vector de eje de rotación (3D).
    angle: ángulo en radianes.
    """
    axis = axis / np.linalg.norm(axis)
    ux, uy, uz = axis

    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    R = np.array(
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

    return R


def plot_bloch_sphere(ax):
    """
    Dibuja la esfera de Bloch (superficie y ejes cartesianos).
    """
    # Mallado de la esfera
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)

    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    # Superficie semitransparente
    ax.plot_surface(x, y, z, alpha=0.15, edgecolor="none", color="#9ec9ff")

    # Ejes X, Y, Z
    ax.quiver(0, 0, 0, 1, 0, 0, length=1, arrow_length_ratio=0.08, color="gray")
    ax.quiver(0, 0, 0, 0, 1, 0, length=1, arrow_length_ratio=0.08, color="gray")
    ax.quiver(0, 0, 0, 0, 0, 1, length=1, arrow_length_ratio=0.08, color="gray")

    ax.text(1.05, 0, 0, "X", color="black")
    ax.text(0, 1.05, 0, "Y", color="black")
    ax.text(0, 0, 1.05, "Z", color="black")

    # Límites y proporciones
    for axis in [ax.set_xlim, ax.set_ylim, ax.set_zlim]:
        axis([-1.1, 1.1])

    ax.set_box_aspect([1, 1, 1])  # Esfera no achatada
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# =============================
#  Script principal
# =============================


def main():
    # -------------------------
    # 1. Estado inicial en la esfera
    # -------------------------
    # Cambia estos ángulos para mover el vector inicial
    theta_0 = 0.0  # 60°
    phi_0 = 0.0  # 45°

    v_in = bloch_vector_from_angles(theta_0, phi_0)

    # -------------------------
    # 2. Transformación lineal = rotación
    # -------------------------
    # EJE de rotación (puedes cambiarlo)
    axis = np.array([0, 0, 1])
    # ÁNGULO de rotación
    angle = np.pi / 2  # 90°

    R = rotation_matrix(axis, angle)
    v_out = R @ v_in
    v_out = v_out / np.linalg.norm(v_out)

    # Trayectoria: aplicamos rotaciones intermedias
    num_steps = 80
    ts = np.linspace(0, 1, num_steps)
    traj = np.array([rotation_matrix(axis, t * angle) @ v_in for t in ts])

    # -------------------------
    # 3. Graficar
    # -------------------------
    fig = plt.figure(figsize=(9, 8))
    ax = fig.add_subplot(111, projection="3d")

    plot_bloch_sphere(ax)

    # Eje de rotación (flecha gruesa en negro)
    axis_unit = axis / np.linalg.norm(axis)
    axis_len = 1.0
    ax.quiver(
        0,
        0,
        0,
        axis_unit[0] * axis_len,
        axis_unit[1] * axis_len,
        axis_unit[2] * axis_len,
        color="black",
        linewidth=2.5,
        arrow_length_ratio=0.15,
        label="Eje de rotación",
    )

    # Vector inicial (rojo)
    ax.quiver(
        0,
        0,
        0,
        v_in[0],
        v_in[1],
        v_in[2],
        color="red",
        linewidth=2.5,
        arrow_length_ratio=0.18,
        label="Estado inicial",
    )
    ax.scatter(*v_in, color="red")

    # Vector transformado (azul)
    ax.quiver(
        0,
        0,
        0,
        v_out[0],
        v_out[1],
        v_out[2],
        color="blue",
        linewidth=2.5,
        arrow_length_ratio=0.18,
        label="Estado transformado",
    )
    ax.scatter(*v_out, color="blue")

    # Trayectoria (arco morado entre inicial y final)
    ax.plot(
        traj[:, 0],
        traj[:, 1],
        traj[:, 2],
        linestyle="--",
        linewidth=2,
        color="purple",
        label="Trayectoria de la rotación",
    )

    # Ajustar vista para que se vea bien el arco
    ax.view_init(elev=20, azim=40)

    ax.set_title("Esfera de Bloch – Vector, Eje y Trayectoria de la Transformación")
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
