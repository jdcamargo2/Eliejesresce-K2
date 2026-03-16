"""
Simula la acción de un operador cuántico sobre un qubit y anima su evolución
en la esfera de Bloch junto con sus probabilidades de medición en una base elegida.
La visualización muestra el estado, su trayectoria, las probabilidades observadas
y los eigenvalores del operador para conectar geometría, medición y evolución.
"""

import os
os.environ.pop("MPLBACKEND", None)

import matplotlib
matplotlib.use("TkAgg", force=True)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# =============================
# Parámetros que puedes tocar
# =============================
INITIAL_STATE_LABEL = "0"          # opciones: "0", "1", "+", "-", "+i", "-i"
OPERATOR_LABEL = "H"              # opciones: "X", "Y", "Z", "H", "S", "T", "RX", "RY", "RZ"
MEASUREMENT_BASIS = "X"            # opciones: "X", "Y", "Z"
TOTAL_FRAMES = 180
INTERVAL_MS = 40
ROTATION_ANGLE = np.pi              # usado para RX, RY, RZ
TRAIL_LENGTH = 500                  # puntos máximos de la trayectoria

# =============================
# Utilidades de espacio de Hilbert
# =============================

def ket0() -> np.ndarray:
    return np.array([[1.0 + 0.0j], [0.0 + 0.0j]])


def ket1() -> np.ndarray:
    return np.array([[0.0 + 0.0j], [1.0 + 0.0j]])


def normalize(state: np.ndarray) -> np.ndarray:
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("El estado no puede tener norma cero.")
    return state / norm


def global_phase_fix(state: np.ndarray) -> np.ndarray:
    """
    Ajusta una fase global para representación más estable de α y β.
    No cambia la física, solo la forma de imprimir el estado.
    """
    state = state.copy()
    for idx in range(len(state)):
        value = state[idx, 0]
        if abs(value) > 1e-12:
            phase = np.angle(value)
            return state * np.exp(-1j * phase)
    return state


STATE_LIBRARY = {
    "0": ket0(),
    "1": ket1(),
    "+": normalize((ket0() + ket1())),
    "-": normalize((ket0() - ket1())),
    "+i": normalize((ket0() + 1j * ket1())),
    "-i": normalize((ket0() - 1j * ket1())),
}


def pauli_x() -> np.ndarray:
    return np.array([[0, 1], [1, 0]], dtype=complex)


def pauli_y() -> np.ndarray:
    return np.array([[0, -1j], [1j, 0]], dtype=complex)


def pauli_z() -> np.ndarray:
    return np.array([[1, 0], [0, -1]], dtype=complex)


def hadamard() -> np.ndarray:
    return (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)


def phase_s() -> np.ndarray:
    return np.array([[1, 0], [0, 1j]], dtype=complex)


def phase_t() -> np.ndarray:
    return np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)


def rx(theta: float) -> np.ndarray:
    return np.cos(theta / 2) * np.eye(2, dtype=complex) - 1j * np.sin(theta / 2) * pauli_x()


def ry(theta: float) -> np.ndarray:
    return np.cos(theta / 2) * np.eye(2, dtype=complex) - 1j * np.sin(theta / 2) * pauli_y()


def rz(theta: float) -> np.ndarray:
    return np.cos(theta / 2) * np.eye(2, dtype=complex) - 1j * np.sin(theta / 2) * pauli_z()


def get_operator(label: str, angle: float) -> np.ndarray:
    label = label.upper()
    operators = {
        "X": pauli_x(),
        "Y": pauli_y(),
        "Z": pauli_z(),
        "H": hadamard(),
        "S": phase_s(),
        "T": phase_t(),
        "RX": rx(angle),
        "RY": ry(angle),
        "RZ": rz(angle),
    }
    if label not in operators:
        raise ValueError(f"Operador no soportado: {label}")
    return operators[label]


def dagger(matrix: np.ndarray) -> np.ndarray:
    return np.conjugate(matrix.T)


def bloch_coordinates(state: np.ndarray) -> tuple[float, float, float]:
    state = normalize(state)
    a = state[0, 0]
    b = state[1, 0]
    x = 2 * np.real(np.conjugate(a) * b)
    y = 2 * np.imag(np.conjugate(b) * a)
    z = np.abs(a) ** 2 - np.abs(b) ** 2
    return float(x), float(y), float(z)


def measurement_basis_states(axis: str) -> tuple[np.ndarray, np.ndarray, str, str]:
    axis = axis.upper()
    if axis == "Z":
        return ket0(), ket1(), "|0⟩", "|1⟩"
    if axis == "X":
        plus = normalize(ket0() + ket1())
        minus = normalize(ket0() - ket1())
        return plus, minus, "|+⟩", "|-⟩"
    if axis == "Y":
        plus_i = normalize(ket0() + 1j * ket1())
        minus_i = normalize(ket0() - 1j * ket1())
        return plus_i, minus_i, "|+i⟩", "|-i⟩"
    raise ValueError(f"Base de medición no soportada: {axis}")


def measurement_probabilities(state: np.ndarray, axis: str) -> tuple[float, float, str, str]:
    b0, b1, label0, label1 = measurement_basis_states(axis)
    amp0 = (dagger(b0) @ state)[0, 0]
    amp1 = (dagger(b1) @ state)[0, 0]
    p0 = float(np.abs(amp0) ** 2)
    p1 = float(np.abs(amp1) ** 2)
    return p0, p1, label0, label1


def format_complex(z: complex, decimals: int = 3) -> str:
    re = np.real(z)
    im = np.imag(z)
    re = 0.0 if abs(re) < 1e-12 else re
    im = 0.0 if abs(im) < 1e-12 else im
    if im == 0:
        return f"{re:.{decimals}f}"
    if re == 0:
        return f"{im:.{decimals}f}i"
    sign = "+" if im >= 0 else "-"
    return f"{re:.{decimals}f} {sign} {abs(im):.{decimals}f}i"


def state_to_string(state: np.ndarray) -> str:
    pretty = global_phase_fix(normalize(state))
    alpha = pretty[0, 0]
    beta = pretty[1, 0]
    return f"|ψ⟩ = ({format_complex(alpha)})|0⟩ + ({format_complex(beta)})|1⟩"


def eigen_info(operator: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eig(operator)
    return values, vectors


def geodesic_states(initial: np.ndarray, final: np.ndarray, n_frames: int) -> list[np.ndarray]:
    """
    Interpolación suave entre dos estados normalizados en el espacio de Hilbert,
    corrigiendo fase relativa para que el camino sea corto y visualmente estable.
    """
    psi0 = normalize(initial)
    psi1 = normalize(final)

    overlap = (dagger(psi0) @ psi1)[0, 0]
    if abs(overlap) > 1e-12:
        psi1 = psi1 * np.exp(-1j * np.angle(overlap))

    states = []
    for t in np.linspace(0.0, 1.0, n_frames):
        psi_t = (1 - t) * psi0 + t * psi1
        states.append(normalize(psi_t))
    return states


# =============================
# Preparación de datos
# =============================
psi_initial = STATE_LIBRARY[INITIAL_STATE_LABEL]
operator = get_operator(OPERATOR_LABEL, ROTATION_ANGLE)
psi_final = normalize(operator @ psi_initial)
path_states = geodesic_states(psi_initial, psi_final, TOTAL_FRAMES)

bloch_path = np.array([bloch_coordinates(psi) for psi in path_states])

p0_all = []
p1_all = []
for psi in path_states:
    p0, p1, _, _ = measurement_probabilities(psi, MEASUREMENT_BASIS)
    p0_all.append(p0)
    p1_all.append(p1)

p0_all = np.array(p0_all)
p1_all = np.array(p1_all)

final_p0, final_p1, meas_label0, meas_label1 = measurement_probabilities(psi_final, MEASUREMENT_BASIS)
e_vals, e_vecs = eigen_info(operator)

# =============================
# Configuración de la figura
# =============================
fig = plt.figure(figsize=(15, 8))
fig.suptitle("Campamento de Anclaje — Acción de un operador sobre un qubit", fontsize=16)

ax_bloch = fig.add_subplot(1, 2, 1, projection="3d")
ax_prob = fig.add_subplot(1, 2, 2)

# --- Esfera de Bloch ---
u = np.linspace(0, 2 * np.pi, 80)
v = np.linspace(0, np.pi, 40)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))
ax_bloch.plot_surface(xs, ys, zs, alpha=0.08, linewidth=0)

# Ejes
ax_bloch.quiver(0, 0, 0, 1.15, 0, 0, arrow_length_ratio=0.08)
ax_bloch.quiver(0, 0, 0, 0, 1.15, 0, arrow_length_ratio=0.08)
ax_bloch.quiver(0, 0, 0, 0, 0, 1.15, arrow_length_ratio=0.08)
ax_bloch.text(1.22, 0, 0, "+X\n|+⟩", fontsize=10)
ax_bloch.text(-1.28, 0, 0, "-X\n|-⟩", fontsize=10)
ax_bloch.text(0, 1.22, 0, "+Y\n|+i⟩", fontsize=10)
ax_bloch.text(0, -1.3, 0, "-Y\n|-i⟩", fontsize=10)
ax_bloch.text(0, 0, 1.22, "+Z\n|0⟩", fontsize=10)
ax_bloch.text(0, 0, -1.3, "-Z\n|1⟩", fontsize=10)

# Trayectoria y estado actual
trail_line, = ax_bloch.plot([], [], [], lw=2)
state_point, = ax_bloch.plot([], [], [], marker="o", markersize=8)
state_vector = None

ax_bloch.set_xlim([-1.25, 1.25])
ax_bloch.set_ylim([-1.25, 1.25])
ax_bloch.set_zlim([-1.25, 1.25])
ax_bloch.set_xlabel("X")
ax_bloch.set_ylabel("Y")
ax_bloch.set_zlabel("Z")
ax_bloch.set_title("Esfera de Bloch")
ax_bloch.view_init(elev=22, azim=38)

# --- Probabilidades de medición ---
bars = ax_prob.bar([0, 1], [0.0, 0.0], width=0.55)
ax_prob.set_xticks([0, 1], [meas_label0, meas_label1])
ax_prob.set_ylim(0.0, 1.05)
ax_prob.set_ylabel("Probabilidad")
ax_prob.set_title(f"Medición en base {MEASUREMENT_BASIS}")
ax_prob.grid(axis="y", alpha=0.3)
prob_text = ax_prob.text(0.02, 0.95, "", transform=ax_prob.transAxes, va="top", fontsize=11)

# --- Caja de información textual ---
info_text = fig.text(0.06, 0.02, "", fontsize=10, family="monospace")


def build_info(frame_idx: int, psi: np.ndarray) -> str:
    x, y, z = bloch_coordinates(psi)
    p0, p1, label0, label1 = measurement_probabilities(psi, MEASUREMENT_BASIS)

    eig_lines = []
    for i, value in enumerate(e_vals):
        eig_lines.append(f"λ{i+1} = {format_complex(value)}")

    text = (
        f"Estado inicial: |{INITIAL_STATE_LABEL}⟩\n"
        f"Operador aplicado: {OPERATOR_LABEL}\n"
        f"Frame: {frame_idx + 1}/{TOTAL_FRAMES}\n"
        f"{state_to_string(psi)}\n"
        f"Bloch = ({x:+.3f}, {y:+.3f}, {z:+.3f})\n"
        f"P({label0}) = {p0:.3f}    P({label1}) = {p1:.3f}\n"
        f"Eigenvalores del operador: {' | '.join(eig_lines)}"
    )
    return text


def init_animation():
    global state_vector
    trail_line.set_data([], [])
    trail_line.set_3d_properties([])

    x0, y0, z0 = bloch_path[0]
    state_point.set_data([x0], [y0])
    state_point.set_3d_properties([z0])

    if state_vector is not None:
        state_vector.remove()
    state_vector = ax_bloch.quiver(0, 0, 0, x0, y0, z0, arrow_length_ratio=0.12)

    for bar in bars:
        bar.set_height(0.0)

    prob_text.set_text("")
    info_text.set_text(build_info(0, path_states[0]))
    return [trail_line, state_point, prob_text, info_text]


def update(frame: int):
    global state_vector

    start = max(0, frame - TRAIL_LENGTH)
    x = bloch_path[start:frame + 1, 0]
    y = bloch_path[start:frame + 1, 1]
    z = bloch_path[start:frame + 1, 2]

    trail_line.set_data(x, y)
    trail_line.set_3d_properties(z)

    x_now, y_now, z_now = bloch_path[frame]
    state_point.set_data([x_now], [y_now])
    state_point.set_3d_properties([z_now])

    if state_vector is not None:
        state_vector.remove()
    state_vector = ax_bloch.quiver(0, 0, 0, x_now, y_now, z_now, arrow_length_ratio=0.12)

    bars[0].set_height(p0_all[frame])
    bars[1].set_height(p1_all[frame])

    prob_text.set_text(
        f"P({meas_label0}) = {p0_all[frame]:.3f}\n"
        f"P({meas_label1}) = {p1_all[frame]:.3f}"
    )

    info_text.set_text(build_info(frame, path_states[frame]))
    return [trail_line, state_point, prob_text, info_text]


ani = FuncAnimation(
    fig,
    update,
    frames=TOTAL_FRAMES,
    init_func=init_animation,
    interval=INTERVAL_MS,
    blit=False,
    repeat=False,
)

plt.tight_layout(rect=[0, 0.08, 1, 0.95])
plt.show()
