"""
Comparación visual entre estados puros y mixtos
usando matrices densidad y Bloch.
"""

import os
os.environ.pop("MPLBACKEND", None)

import matplotlib
matplotlib.use("TkAgg", force=True)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# =========================================================
# PARÁMETROS QUE PUEDES TOCAR (Mango-friendly)
# =========================================================

# ---- Estado inicial PURO (superficie de Bloch)
theta_pure = 0
phi_pure   = 3.14

# ---- Elige cómo construir el estado MIXTO inicial
# Opciones: "bloch_shrink", "mix_0_1", "mix_two_pure"
MIXED_MODE = "bloch_shrink"

# (A) "bloch_shrink": mismo eje, distinta norma (0..1)
mixed_r_len_0 = 0.55

# (B) "mix_0_1": rho = p0|0><0| + (1-p0)|1><1|
p0_classical = 0.5

# (C) "mix_two_pure": rho = p|psi1><psi1| + (1-p)|psi2><psi2|
mix_p = 0.7
theta_psi2 = 2.2
phi_psi2   = 0.3

# ---- Secuencia de compuertas
# Implementadas: "X","Y","Z","H","S","T"
GATE_SEQUENCE = ["H", "Z", "H", "Z", "H"]
FRAMES_PER_GATE = 60

# ---- Ruido tras cada compuerta (opcional)
APPLY_NOISE_AFTER_EACH_GATE = True
NOISE_MODEL = "dephasing"   # "none", "depolarizing", "dephasing", "amplitude_damping"

# intensidades típicas (ajusta a gusto)
DEPOLARIZING_P = 0.10       # 0..1
DEPHASING_LAMBDA = 0.2     # 0..1 (reduce coherencia)
AMP_DAMP_GAMMA = 0.08       # 0..1 (relajación)

# ---- Animación
INTERVAL_MS = 40


# =========================================================
# ÁLGEBRA: Pauli, densidad, métricas, probabilidades
# =========================================================

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
X  = np.array([[0, 1], [1, 0]], dtype=complex)
Y  = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z  = np.array([[1, 0], [0, -1]], dtype=complex)

H_GATE = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]], dtype=complex)

def purity(rho: np.ndarray) -> float:
    return float(np.real(np.trace(rho @ rho)))

def von_neumann_entropy(rho: np.ndarray, eps: float = 1e-12) -> float:
    vals = np.linalg.eigvalsh(rho)
    vals = np.clip(np.real(vals), eps, 1.0)
    return float(-np.sum(vals * np.log2(vals)))

def probs_in_Z(rho: np.ndarray):
    p0 = float(np.real(rho[0, 0]))
    p1 = float(np.real(rho[1, 1]))
    return p0, p1

def probs_in_X(rho: np.ndarray):
    rho_x = H_GATE @ rho @ H_GATE.conj().T
    return probs_in_Z(rho_x)

def bloch_from_rho(rho: np.ndarray) -> np.ndarray:
    rx = np.real(np.trace(rho @ X))
    ry = np.real(np.trace(rho @ Y))
    rz = np.real(np.trace(rho @ Z))
    return np.array([rx, ry, rz], dtype=float)

def rho_from_bloch(r: np.ndarray) -> np.ndarray:
    rx, ry, rz = r
    return 0.5 * (I2 + rx * X + ry * Y + rz * Z)

def rho_from_statevector(psi: np.ndarray) -> np.ndarray:
    psi = psi.reshape(2, 1)
    return psi @ psi.conj().T


# =========================================================
# ESTADOS INICIALES (puro y mixto)
# =========================================================

def statevector_from_angles(theta: float, phi: float) -> np.ndarray:
    # |psi> = cos(theta/2)|0> + e^{i phi} sin(theta/2)|1>
    return np.array([
        np.cos(theta/2.0),
        np.exp(1j * phi) * np.sin(theta/2.0)
    ], dtype=complex)

def make_initial_states():
    # Puro
    psi1 = statevector_from_angles(theta_pure, phi_pure)
    rho_pure = rho_from_statevector(psi1)

    # Mixto
    mode = MIXED_MODE.lower()

    if mode == "bloch_shrink":
        # mismo eje que psi1, pero con ||r||<1
        r_p = bloch_from_rho(rho_pure)
        r_m = mixed_r_len_0 * (r_p / (np.linalg.norm(r_p) + 1e-15))
        rho_mixed = rho_from_bloch(r_m)

    elif mode == "mix_0_1":
        p0 = float(p0_classical)
        rho_mixed = np.array([[p0, 0.0],
                              [0.0, 1.0 - p0]], dtype=complex)

    elif mode == "mix_two_pure":
        psi2 = statevector_from_angles(theta_psi2, phi_psi2)
        rho2 = rho_from_statevector(psi2)
        p = float(mix_p)
        rho_mixed = p * rho_pure + (1.0 - p) * rho2

    else:
        raise ValueError(f"MIXED_MODE no soportado: {MIXED_MODE}")

    # Sanitización numérica (hermítica, traza 1)
    rho_mixed = 0.5 * (rho_mixed + rho_mixed.conj().T)
    rho_mixed = rho_mixed / np.trace(rho_mixed)

    return rho_pure, rho_mixed


# =========================================================
# UNITARIAS (compuertas) + interpolación continua U(t)
# =========================================================

def get_gate_axis_angle(gate_name: str):
    g = gate_name.upper()
    if g == "X":
        axis = np.array([1, 0, 0], dtype=float); angle = np.pi
    elif g == "Y":
        axis = np.array([0, 1, 0], dtype=float); angle = np.pi
    elif g == "Z":
        axis = np.array([0, 0, 1], dtype=float); angle = np.pi
    elif g == "S":
        axis = np.array([0, 0, 1], dtype=float); angle = np.pi/2
    elif g == "T":
        axis = np.array([0, 0, 1], dtype=float); angle = np.pi/4
    elif g == "H":
        # H ~ rotación pi alrededor de (X+Z)/sqrt(2) en Bloch (ignorando fase global)
        axis = np.array([1, 0, 1], dtype=float)
        axis = axis / np.linalg.norm(axis)
        angle = np.pi
    else:
        raise ValueError(f"Compuerta no soportada: {gate_name}")
    axis = axis / np.linalg.norm(axis)
    return axis, angle

def U_from_axis_angle(axis: np.ndarray, angle: float) -> np.ndarray:
    """
    U = exp(-i angle/2 * (n·sigma)) = cos(angle/2) I - i sin(angle/2) (n·sigma)
    """
    nx, ny, nz = axis
    n_dot_sigma = nx * X + ny * Y + nz * Z
    return np.cos(angle/2.0) * I2 - 1j * np.sin(angle/2.0) * n_dot_sigma

def evolve_unitary(rho: np.ndarray, U: np.ndarray) -> np.ndarray:
    return U @ rho @ U.conj().T


# =========================================================
# CANALES DE RUIDO (opcional por compuerta)
# =========================================================

def apply_depolarizing(rho: np.ndarray, p: float) -> np.ndarray:
    # rho -> (1-p) rho + p I/2
    return (1.0 - p) * rho + p * (I2 / 2.0)

def apply_dephasing(rho: np.ndarray, lam: float) -> np.ndarray:
    # Mata coherencia: off-diagonal *= (1-lam)
    out = rho.copy()
    out[0, 1] *= (1.0 - lam)
    out[1, 0] *= (1.0 - lam)
    return out

def apply_amplitude_damping(rho: np.ndarray, gamma: float) -> np.ndarray:
    # Kraus:
    # E0 = [[1,0],[0,sqrt(1-g)]], E1=[[0,sqrt(g)],[0,0]]
    g = gamma
    E0 = np.array([[1.0, 0.0],
                   [0.0, np.sqrt(1.0 - g)]], dtype=complex)
    E1 = np.array([[0.0, np.sqrt(g)],
                   [0.0, 0.0]], dtype=complex)
    return E0 @ rho @ E0.conj().T + E1 @ rho @ E1.conj().T

def apply_noise_after_gate(rho: np.ndarray) -> np.ndarray:
    model = NOISE_MODEL.lower()
    if not APPLY_NOISE_AFTER_EACH_GATE or model == "none":
        return rho
    if model == "depolarizing":
        return apply_depolarizing(rho, DEPOLARIZING_P)
    if model == "dephasing":
        return apply_dephasing(rho, DEPHASING_LAMBDA)
    if model == "amplitude_damping":
        return apply_amplitude_damping(rho, AMP_DAMP_GAMMA)
    raise ValueError(f"NOISE_MODEL no soportado: {NOISE_MODEL}")


# =========================================================
# VISUAL: esfera de Bloch
# =========================================================

def plot_bloch_sphere(ax):
    u = np.linspace(0, 2*np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    xs = np.outer(np.cos(u), np.sin(v))
    ys = np.outer(np.sin(u), np.sin(v))
    zs = np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(xs, ys, zs, alpha=0.12, edgecolor="none")

    ax.quiver(0,0,0, 1,0,0, color="gray", arrow_length_ratio=0.08)
    ax.quiver(0,0,0, 0,1,0, color="gray", arrow_length_ratio=0.08)
    ax.quiver(0,0,0, 0,0,1, color="gray", arrow_length_ratio=0.08)

    ax.text(1.05, 0, 0, "X")
    ax.text(0, 1.05, 0, "Y")
    ax.text(0, 0, 1.05, "Z")

    for setter in [ax.set_xlim, ax.set_ylim, ax.set_zlim]:
        setter([-1.1, 1.1])

    ax.set_box_aspect([1,1,1])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")


# =========================================================
# PRECOMPUTAR TRAYECTORIA (frames) para ambos rho
# =========================================================

def build_frames(rho_p0: np.ndarray, rho_m0: np.ndarray):
    """
    Devuelve listas por frame:
      rhos_p[frame], rhos_m[frame], gate_labels[frame]
    Donde rhos_* son matrices densidad 2x2.
    """
    rhos_p, rhos_m, gate_labels = [], [], []

    rho_p = rho_p0.copy()
    rho_m = rho_m0.copy()

    for gate in GATE_SEQUENCE:
        axis, angle_total = get_gate_axis_angle(gate)

        # rho de inicio de este gate (base)
        rho_p_start = rho_p.copy()
        rho_m_start = rho_m.copy()

        for step in range(FRAMES_PER_GATE):
            t = step / (FRAMES_PER_GATE - 1)
            U_t = U_from_axis_angle(axis, t * angle_total)

            rho_p_frame = evolve_unitary(rho_p_start, U_t)
            rho_m_frame = evolve_unitary(rho_m_start, U_t)

            # Sanitiza numérico
            rho_p_frame = 0.5 * (rho_p_frame + rho_p_frame.conj().T)
            rho_m_frame = 0.5 * (rho_m_frame + rho_m_frame.conj().T)

            rhos_p.append(rho_p_frame)
            rhos_m.append(rho_m_frame)
            gate_labels.append(gate)

        # actualizar estado al final del gate
        U_full = U_from_axis_angle(axis, angle_total)
        rho_p = evolve_unitary(rho_p, U_full)
        rho_m = evolve_unitary(rho_m, U_full)

        # aplicar ruido (opcional)
        rho_p = apply_noise_after_gate(rho_p)
        rho_m = apply_noise_after_gate(rho_m)

        # re-normaliza traza
        rho_p = rho_p / np.trace(rho_p)
        rho_m = rho_m / np.trace(rho_m)

    return rhos_p, rhos_m, gate_labels


# =========================================================
# MAIN
# =========================================================

def main():
    rho_p0, rho_m0 = make_initial_states()

    # Reporte inicial
    r0p = bloch_from_rho(rho_p0)
    r0m = bloch_from_rho(rho_m0)

    print("\n=== CONFIG ===")
    print("MIXED_MODE =", MIXED_MODE)
    print("NOISE_MODEL =", NOISE_MODEL if APPLY_NOISE_AFTER_EACH_GATE else "none")
    print("\n=== INICIO ===")
    print("Bloch puro:", np.round(r0p, 6), "||r|| =", np.linalg.norm(r0p))
    print("rho puro:\n", np.round(rho_p0, 4))
    print("purity(puro) =", round(purity(rho_p0), 6), " | S(puro) =", round(von_neumann_entropy(rho_p0), 6))

    print("\nBloch mixto:", np.round(r0m, 6), "||r|| =", np.linalg.norm(r0m))
    print("rho mixto:\n", np.round(rho_m0, 4))
    print("purity(mixto) =", round(purity(rho_m0), 6), " | S(mixto) =", round(von_neumann_entropy(rho_m0), 6))
    print()

    # Frames
    rhos_p, rhos_m, gate_labels = build_frames(rho_p0, rho_m0)

    # Figure: 2 paneles
    fig = plt.figure(figsize=(12, 7))
    ax_bloch = fig.add_subplot(121, projection="3d")
    ax_prob  = fig.add_subplot(122)

    plot_bloch_sphere(ax_bloch)

    # Inicial: flechas contexto
    ax_bloch.quiver(0,0,0, r0p[0], r0p[1], r0p[2], color="red",
                    linewidth=2, arrow_length_ratio=0.12, label="Inicial (puro)")
    ax_bloch.quiver(0,0,0, r0m[0], r0m[1], r0m[2], color="dimgray",
                    linewidth=2, arrow_length_ratio=0.12, label="Inicial (mixto)")

    # Flechas dinámicas
    arrow_p = ax_bloch.quiver(0,0,0, r0p[0], r0p[1], r0p[2], color="blue",
                              linewidth=2.5, arrow_length_ratio=0.16, label="Actual (puro)")
    arrow_m = ax_bloch.quiver(0,0,0, r0m[0], r0m[1], r0m[2], color="orange",
                              linewidth=2.5, arrow_length_ratio=0.16, label="Actual (mixto)")

    # Trayectorias
    traj_px, traj_py, traj_pz = [r0p[0]], [r0p[1]], [r0p[2]]
    traj_mx, traj_my, traj_mz = [r0m[0]], [r0m[1]], [r0m[2]]

    (line_p,) = ax_bloch.plot(traj_px, traj_py, traj_pz, linestyle="--", linewidth=2, label="Trayectoria (puro)")
    (line_m,) = ax_bloch.plot(traj_mx, traj_my, traj_mz, linestyle="--", linewidth=2, label="Trayectoria (mixto)")

    title_bloch = ax_bloch.set_title("Bloch: Puro vs Mixto")
    ax_bloch.legend(loc="upper left")
    ax_bloch.view_init(elev=25, azim=40)

    # Panel de probabilidades (Z y X para ambos)
    ax_prob.set_title("Probabilidades de medición (Z y X)")
    ax_prob.set_ylim(0, 1.0)

    labels = ["Z:0", "Z:1", "X:0", "X:1"]
    x = np.arange(len(labels))
    width = 0.35

    # Barras iniciales
    p0z_p, p1z_p = probs_in_Z(rho_p0)
    p0x_p, p1x_p = probs_in_X(rho_p0)

    p0z_m, p1z_m = probs_in_Z(rho_m0)
    p0x_m, p1x_m = probs_in_X(rho_m0)

    bars_p = ax_prob.bar(x - width/2, [p0z_p, p1z_p, p0x_p, p1x_p], width, label="Puro")
    bars_m = ax_prob.bar(x + width/2, [p0z_m, p1z_m, p0x_m, p1x_m], width, label="Mixto")

    ax_prob.set_xticks(x)
    ax_prob.set_xticklabels(labels)
    ax_prob.legend()

    # Texto de métricas
    metrics_text = ax_prob.text(
        0.02, 0.95, "", transform=ax_prob.transAxes, va="top"
    )

    state = {
        "arrow_p": arrow_p, "arrow_m": arrow_m,
        "line_p": line_p, "line_m": line_m,
        "traj_px": traj_px, "traj_py": traj_py, "traj_pz": traj_pz,
        "traj_mx": traj_mx, "traj_my": traj_my, "traj_mz": traj_mz,
        "title_bloch": title_bloch,
        "bars_p": bars_p, "bars_m": bars_m,
        "metrics_text": metrics_text
    }

    def update(frame):
        rho_p = rhos_p[frame]
        rho_m = rhos_m[frame]
        gate = gate_labels[frame]

        rp = bloch_from_rho(rho_p)
        rm = bloch_from_rho(rho_m)

        # Trayectorias
        state["traj_px"].append(rp[0]); state["traj_py"].append(rp[1]); state["traj_pz"].append(rp[2])
        state["traj_mx"].append(rm[0]); state["traj_my"].append(rm[1]); state["traj_mz"].append(rm[2])

        state["line_p"].set_data(state["traj_px"], state["traj_py"])
        state["line_p"].set_3d_properties(state["traj_pz"])

        state["line_m"].set_data(state["traj_mx"], state["traj_my"])
        state["line_m"].set_3d_properties(state["traj_mz"])

        # Flechas dinámicas
        state["arrow_p"].remove()
        state["arrow_m"].remove()
        state["arrow_p"] = ax_bloch.quiver(0,0,0, rp[0], rp[1], rp[2], color="blue",
                                           linewidth=2.5, arrow_length_ratio=0.16)
        state["arrow_m"] = ax_bloch.quiver(0,0,0, rm[0], rm[1], rm[2], color="orange",
                                           linewidth=2.5, arrow_length_ratio=0.16)

        # Probabilidades
        p0z_p, p1z_p = probs_in_Z(rho_p); p0x_p, p1x_p = probs_in_X(rho_p)
        p0z_m, p1z_m = probs_in_Z(rho_m); p0x_m, p1x_m = probs_in_X(rho_m)

        vals_p = [p0z_p, p1z_p, p0x_p, p1x_p]
        vals_m = [p0z_m, p1z_m, p0x_m, p1x_m]

        for b, v in zip(state["bars_p"], vals_p):
            b.set_height(v)
        for b, v in zip(state["bars_m"], vals_m):
            b.set_height(v)

        # Métricas (prueba de teoría)
        pur_p = purity(rho_p); pur_m = purity(rho_m)
        ent_p = von_neumann_entropy(rho_p); ent_m = von_neumann_entropy(rho_m)

        state["metrics_text"].set_text(
            f"Gate: {gate}   frame {frame+1}/{len(rhos_p)}\n"
            f"||r_puro||={np.linalg.norm(rp):.3f}   purity={pur_p:.3f}   S={ent_p:.3f}\n"
            f"||r_mixto||={np.linalg.norm(rm):.3f}   purity={pur_m:.3f}   S={ent_m:.3f}\n\n"
            f"Z puro:({p0z_p:.2f},{p1z_p:.2f})  X puro:({p0x_p:.2f},{p1x_p:.2f})\n"
            f"Z mixto:({p0z_m:.2f},{p1z_m:.2f})  X mixto:({p0x_m:.2f},{p1x_m:.2f})"
        )

        state["title_bloch"].set_text(
            f"Bloch: Puro vs Mixto — Gate {gate} (frame {frame+1}/{len(rhos_p)})"
        )

        return (
            state["arrow_p"], state["arrow_m"],
            state["line_p"], state["line_m"],
            *state["bars_p"], *state["bars_m"],
            state["metrics_text"], state["title_bloch"]
        )

    anim = FuncAnimation(fig, update, frames=len(rhos_p), interval=INTERVAL_MS, blit=False)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
