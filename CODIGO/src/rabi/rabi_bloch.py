"""
Simula el control físico de un qubit mediante oscilaciones de Rabi aplicando
pulsos electromagnéticos resonantes y desintonizados sobre un sistema de dos
niveles. El programa visualiza simultáneamente la evolución en la esfera de
Bloch, el Hamiltoniano efectivo y la probabilidad de transición entre |0⟩ y |1⟩.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import RadioButtons

# =========================
# Parámetros físicos
# =========================

dt = 0.01
omega_qubit = 8.0      # frecuencia natural del qubit, escala visual
Omega = 1.0            # frecuencia de Rabi / fuerza del drive

r0 = np.array([0.0, 0.0, 1.0])  # |0⟩ en Bloch

# =========================
# Utilidades de Bloch
# =========================

def rotate_vector(r, axis, angle):
    axis = np.array(axis, dtype=float)
    norm = np.linalg.norm(axis)

    if norm == 0:
        return r

    n = axis / norm

    return (
        r * np.cos(angle)
        + np.cross(n, r) * np.sin(angle)
        + n * np.dot(n, r) * (1 - np.cos(angle))
    )


def evolve_step(r, Omega, phase, Delta, dt):
    """
    Hamiltoniano efectivo:
    H_eff = 1/2 [Omega cos(phi) X + Omega sin(phi) Y + Delta Z]
    """

    axis = np.array([
        Omega * np.cos(phase),
        Omega * np.sin(phase),
        Delta
    ])

    omega_eff = np.linalg.norm(axis)
    angle = omega_eff * dt

    return rotate_vector(r, axis, angle), axis


# =========================
# Casos de estudio
# =========================

CASES = {
    "Rabi resonante": {
        "Omega": Omega,
        "Delta": 0.0,
        "phase": 0.0,
        "duration": 2 * np.pi / Omega,
        "description": "Oscilación completa |0⟩ ↔ |1⟩"
    },

    "Rabi desintonizado": {
        "Omega": Omega,
        "Delta": 2.0,
        "phase": 0.0,
        "duration": 2 * np.pi / Omega,
        "description": "Rabi con menor amplitud por detuning"
    },

    "Pulso π / Compuerta X": {
        "Omega": Omega,
        "Delta": 0.0,
        "phase": 0.0,
        "duration": np.pi / Omega,
        "description": "Pulso resonante que invierte |0⟩ → |1⟩"
    },

    "Pulso π/2 / Superposición": {
        "Omega": Omega,
        "Delta": 0.0,
        "phase": np.pi / 2,
        "duration": (np.pi / 2) / Omega,
        "description": "Pulso Ry(π/2): |0⟩ → |+⟩"
    }
}

current_case = "Rabi resonante"

# Estado dinámico
time = 0.0
r = r0.copy()
trajectory = []
prob_history = []
time_history = []

# =========================
# Dibujo de Bloch
# =========================

def draw_bloch(ax):
    ax.clear()

    u = np.linspace(0, 2 * np.pi, 80)
    v = np.linspace(0, np.pi, 40)

    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones_like(u), np.cos(v))

    ax.plot_wireframe(x, y, z, alpha=0.13, linewidth=0.5)

    ax.quiver(0, 0, 0, 1.2, 0, 0, arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 1.2, 0, arrow_length_ratio=0.08)
    ax.quiver(0, 0, 0, 0, 0, 1.2, arrow_length_ratio=0.08)

    ax.text(1.28, 0, 0, "X / |+⟩")
    ax.text(0, 1.28, 0, "Y")
    ax.text(0, 0, 1.28, "|0⟩")
    ax.text(0, 0, -1.28, "|1⟩")

    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.3)
    ax.set_zlim(-1.3, 1.3)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_box_aspect([1, 1, 1])


# =========================
# Reset
# =========================

def reset(label=None):
    global current_case, time, r, trajectory, prob_history, time_history

    if label is not None:
        current_case = label

    time = 0.0
    r = r0.copy()
    trajectory = [r.copy()]
    prob_history = [(1 - r[2]) / 2]
    time_history = [0.0]


# =========================
# Figura
# =========================

fig = plt.figure(figsize=(18, 10))

gs = fig.add_gridspec(
    3, 3,
    width_ratios=[2.2, 1, 1],
    height_ratios=[1, 1, 1]
)

ax_bloch = fig.add_subplot(gs[:, 0], projection="3d")
ax_lab = fig.add_subplot(gs[0, 1:])
ax_iq = fig.add_subplot(gs[1, 1:])
ax_prob = fig.add_subplot(gs[2, 1:])

plt.subplots_adjust(left=0.05, bottom=0.18, right=0.97, top=0.93, hspace=0.45)

plt.subplots_adjust(left=0.08, bottom=0.2, right=0.95, hspace=0.35)

radio_ax = plt.axes([0.08, 0.03, 0.33, 0.13])
selector = RadioButtons(radio_ax, list(CASES.keys()))
selector.on_clicked(reset)

reset(current_case)

# =========================
# Animación
# =========================

def update(frame):
    global time, r, trajectory, prob_history, time_history

    case = CASES[current_case]

    Omega_val = case["Omega"]
    Delta = case["Delta"]
    phase = case["phase"]
    duration = case["duration"]

    time += dt

    if time > duration:
        reset(current_case)
        return

    r, axis = evolve_step(r, Omega_val, phase, Delta, dt)

    trajectory.append(r.copy())
    prob_history.append((1 - r[2]) / 2)
    time_history.append(time)

    # =========================
    # Bloch
    # =========================

    draw_bloch(ax_bloch)

    traj = np.array(trajectory)

    ax_bloch.plot(traj[:, 0], traj[:, 1], traj[:, 2], linewidth=2)

    ax_bloch.quiver(
        0, 0, 0,
        r[0], r[1], r[2],
        linewidth=3,
        arrow_length_ratio=0.12
    )

    axis_norm = np.linalg.norm(axis)
    if axis_norm != 0:
        n = axis / axis_norm
        ax_bloch.quiver(
            0, 0, 0,
            n[0], n[1], n[2],
            linestyle="dashed",
            linewidth=2,
            arrow_length_ratio=0.1
        )

    P0 = (1 + r[2]) / 2
    P1 = (1 - r[2]) / 2
    omega_eff = np.sqrt(Omega_val**2 + Delta**2)

    ax_bloch.set_title(
        f"{current_case}\n"
        f"Ω={Omega_val:.2f}, Δ={Delta:.2f}, Ω_eff={omega_eff:.2f}\n"
        f"P(|0⟩)={P0:.3f}, P(|1⟩)={P1:.3f}"
    )

    # =========================
    # Pulso real de laboratorio
    # =========================

    ax_lab.clear()

    t_lab = np.linspace(0, duration, 2000)
    omega_drive = omega_qubit + Delta

    lab_pulse = Omega_val * np.cos(omega_drive * t_lab + phase)

    ax_lab.plot(t_lab, lab_pulse)
    ax_lab.axvline(time, linestyle="--")

    ax_lab.set_title("Pulso real en laboratorio")
    ax_lab.set_xlabel("Tiempo")
    ax_lab.set_ylabel(r"$A\cos(\omega_d t + \phi)$")
    ax_lab.grid(True)

    # =========================
    # Control IQ en marco rotante
    # =========================

    ax_iq.clear()

    I = Omega_val * np.cos(phase) * np.ones_like(t_lab)
    Q = Omega_val * np.sin(phase) * np.ones_like(t_lab)
    Z_detuning = Delta * np.ones_like(t_lab)

    ax_iq.plot(t_lab, I, label="I → eje X")
    ax_iq.plot(t_lab, Q, label="Q → eje Y")
    ax_iq.plot(t_lab, Z_detuning, label="Δ → eje Z")
    ax_iq.axvline(time, linestyle="--")

    ax_iq.set_title("Hamiltoniano efectivo en marco rotante")
    ax_iq.set_xlabel("Tiempo")
    ax_iq.set_ylabel("Componente")
    ax_iq.legend()
    ax_iq.grid(True)

    # =========================
    # Probabilidad Rabi
    # =========================

    ax_prob.clear()

    ax_prob.plot(time_history, prob_history, label="Simulación Bloch")

    if Delta != 0:
        t_formula = np.linspace(0, duration, 1000)
        P_formula = (
            Omega_val**2 / (Omega_val**2 + Delta**2)
            * np.sin(np.sqrt(Omega_val**2 + Delta**2) * t_formula / 2) ** 2
        )
        ax_prob.plot(t_formula, P_formula, linestyle="--", label="Fórmula Rabi")
    else:
        t_formula = np.linspace(0, duration, 1000)
        P_formula = np.sin(Omega_val * t_formula / 2) ** 2
        ax_prob.plot(t_formula, P_formula, linestyle="--", label="Fórmula Rabi")

    ax_prob.axvline(time, linestyle="--")
    ax_prob.set_title("Oscilación de Rabi: probabilidad de medir |1⟩")
    ax_prob.set_xlabel("Tiempo")
    ax_prob.set_ylabel("P(|1⟩)")
    ax_prob.set_ylim(-0.05, 1.05)
    ax_prob.legend()
    ax_prob.grid(True)


ani = FuncAnimation(fig, update, interval=25)

plt.show()