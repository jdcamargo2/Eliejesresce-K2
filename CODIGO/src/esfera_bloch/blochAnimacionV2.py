"""
Este programa anima la evolución de un qubit en la esfera de Bloch para una secuencia
de compuertas cuánticas y permite simular el colapso del estado mediante azar al
presionar la tecla 'c'.
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
#  Presets de estados iniciales
# =============================

# Estados útiles:
# |0>   : (theta=0,      phi=0)
# |1>   : (theta=pi,     phi=0)
# |+>   : (theta=pi/2,   phi=0)
# |->   : (theta=pi/2,   phi=pi)
# |i+>  : (theta=pi/2,   phi=pi/2)
# |i->  : (theta=pi/2,   phi=-pi/2)

STATE_PRESETS = {
    "MANFO": (0.8, 0.8),
    "|0>": (0.0, 0.0),
    "|1>": (np.pi, 0.0),
    "|+>": (np.pi / 2, 0.0),
    "|->": (np.pi / 2, np.pi),
    "|i+>": (np.pi / 2, np.pi / 2),
    "|i->": (np.pi / 2, -np.pi / 2),
}

# Elige el estado inicial aquí:
INITIAL_STATE = "|0>"  # "|0>", "|1>", "|+>", "|->", "|i+>", "|i->"

theta_0, phi_0 = STATE_PRESETS[INITIAL_STATE]


# =============================
#  Parámetros de compuertas
# =============================

# Secuencia de compuertas (en orden)
# Soportadas: "I", "X", "Y", "Z", "H", "S", "T", "RX", "RY", "RZ"
# RX, RY, RZ aquí son rotaciones de pi/2 (90°) alrededor de cada eje.
GATE_SEQUENCE = [
    "Z",
]  # por ejemplo: ["I", "X", "Y", "Z", "H", "S", "T", "RX", "RY", "RZ]

# Suavidad de la animación (más frames = giro más suave)
FRAMES_PER_GATE = 60


# =============================
#  Funciones auxiliares
# =============================


def bloch_vector_from_angles(theta: float, phi: float) -> np.ndarray:
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    return np.array([x, y, z])


def rotation_matrix(axis: np.ndarray, angle: float) -> np.ndarray:
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
    TODO es SU(2)->SO(3) hasta fase global.

    Soportadas:
    - X  = Rx(pi)
    - Y  = Ry(pi)
    - Z  = Rz(pi)
    - H  = rotación de pi alrededor del eje (X+Z)/sqrt(2)
    - S  = Rz(pi/2)
    - T  = Rz(pi/4)
    - RX = Rx(pi/2)
    - RY = Ry(pi/2)
    - RZ = Rz(pi/2)
    - I  = identidad (ángulo 0)
    """
    gate_name = gate_name.upper()

    if gate_name == "I":
        axis = np.array([1, 0, 0])
        angle = 0.0

    elif gate_name == "X":
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
        angle = np.pi  # rotación de 180° alrededor de ese eje
        return axis, angle

    elif gate_name == "S":
        axis = np.array([0, 0, 1])
        angle = np.pi / 2  # Rz(pi/2)

    elif gate_name == "T":
        axis = np.array([0, 0, 1])
        angle = np.pi / 4  # Rz(pi/4)

    elif gate_name == "RX":
        axis = np.array([1, 0, 0])
        angle = np.pi / 2  # Rx(pi/2)

    elif gate_name == "RY":
        axis = np.array([0, 1, 0])
        angle = np.pi / 2  # Ry(pi/2)

    elif gate_name == "RZ":
        axis = np.array([0, 0, 1])
        angle = np.pi / 2  # Rz(pi/2)

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

    # ejes X, Y, Z
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
    Genera todos los vectores intermedios para UNA pasada de la secuencia de compuertas.
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
#  Animación en bucle + colapso
# =============================


def main():
    vectors, gate_labels = build_trajectory()
    n_frames = len(vectors)

    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, projection="3d")

    plot_bloch_sphere(ax)

    # vector inicial (rojo, fijo)
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

    # vector dinámico (azul)
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

    title = ax.set_title(f"Esfera de Bloch – Estado inicial {INITIAL_STATE}")

    ax.legend(loc="upper left")
    ax.view_init(elev=25, azim=40)
    plt.tight_layout()

    # estado compartido para animación y colapso
    state = {
        "arrow": arrow,
        "traj_x": traj_x,
        "traj_y": traj_y,
        "traj_z": traj_z,
        "traj_line": traj_line,
        "title": title,
        "current_v": v_init.copy(),  # último vector
        "collapsed": False,
    }

    def update(frame):
        if state["collapsed"]:
            # si ya colapsamos, no seguimos actualizando
            return state["arrow"], state["traj_line"], state["title"]

        idx = frame
        v = vectors[idx]
        gate = gate_labels[idx]

        # guardar último vector
        state["current_v"] = v.copy()

        if idx == 0:
            # Reinicio de ciclo: limpiar trayectoria
            state["traj_x"].clear()
            state["traj_y"].clear()
            state["traj_z"].clear()

        state["traj_x"].append(v[0])
        state["traj_y"].append(v[1])
        state["traj_z"].append(v[2])

        state["traj_line"].set_data(state["traj_x"], state["traj_y"])
        state["traj_line"].set_3d_properties(state["traj_z"])

        # Actualizar flecha azul
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
            f"Esfera de Bloch – Gate {gate} (frame {idx+1}/{n_frames})"
        )

        return state["arrow"], state["traj_line"], state["title"]

    anim = FuncAnimation(
        fig, update, frames=n_frames, interval=40, blit=False, repeat=True
    )

    # =============================
    #   Evento de teclado: colapso
    # =============================

    def on_key(event):
        # presiona 'c' para colapsar
        if event.key == "c" and not state["collapsed"]:
            v = state["current_v"]
            z = v[2]

            # Probabilidades cuánticas reales:
            # P(0) = (1+z)/2, P(1) = (1-z)/2
            p0 = (1.0 + z) / 2.0
            p0 = min(max(p0, 0.0), 1.0)  # por seguridad numérica
            p1 = 1.0 - p0

            r = np.random.rand()
            if r < p0:
                collapsed = np.array([0.0, 0.0, 1.0])
                estado = "|0>"
            else:
                collapsed = np.array([0.0, 0.0, -1.0])
                estado = "|1>"

            state["traj_x"].append(collapsed[0])
            state["traj_y"].append(collapsed[1])
            state["traj_z"].append(collapsed[2])
            state["traj_line"].set_data(state["traj_x"], state["traj_y"])
            state["traj_line"].set_3d_properties(state["traj_z"])

            # cambiar flecha a verde para indicar colapso
            state["arrow"].remove()
            state["arrow"] = ax.quiver(
                0,
                0,
                0,
                collapsed[0],
                collapsed[1],
                collapsed[2],
                color="green",
                linewidth=3,
                arrow_length_ratio=0.22,
            )

            state["title"].set_text(
                f"Colapso (azar cuántico): P(0)={p0:.2f}, P(1)={p1:.2f} → {estado}"
            )

            state["collapsed"] = True
            anim.event_source.stop()  # detener animación
            fig.canvas.draw_idle()

    fig.canvas.mpl_connect("key_press_event", on_key)

    plt.show()


if __name__ == "__main__":
    main()
