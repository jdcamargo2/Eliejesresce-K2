"""
Animación geométrica del qubit:

ℂ² → normalización (S³) → proyección estereográfica → mapa de Hopf.

Muestra cómo la fase global genera una órbita circular en S³
que colapsa a un único punto en la esfera de Bloch (CP¹ ≅ S²).
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ----------------------------
# Config
# ----------------------------
N = 1200          # puntos nube
SEED = 7
FRAMES_PER_STAGE = 70
TOTAL_STAGES = 4  # 0..3 (ver abajo)

rng = np.random.default_rng(SEED)

# ----------------------------
# Helpers: estados, normas, maps
# ----------------------------
def to_R4(psi):
    """psi in C^2 -> (Re a, Im a, Re b, Im b) in R^4"""
    a, b = psi
    return np.array([np.real(a), np.imag(a), np.real(b), np.imag(b)], dtype=float)

def normalize_C2(psi):
    psi = np.asarray(psi, dtype=np.complex128).reshape(2)
    n = np.linalg.norm(psi)
    if n == 0:
        raise ValueError("Vector cero.")
    return psi / n

def random_C2(n):
    """Nube en C^2 (sin normalizar)"""
    re = rng.normal(size=(n, 2))
    im = rng.normal(size=(n, 2))
    return re + 1j * im

def stereographic_S3_to_R3(x1, x2, x3, x4):
    """Proyección estereográfica desde el polo x4=1: S^3 -> R^3"""
    denom = 1.0 - x4
    # Evitar singularidad cerca del polo
    if np.abs(denom) < 1e-6:
        return None
    return np.array([x1/denom, x2/denom, x3/denom], dtype=float)

# Pauli expectation map -> Bloch vector
def hopf_to_bloch(psi):
    """psi (normalizado) -> r in R^3 (Bloch)"""
    a, b = psi
    x = 2*np.real(np.conj(a)*b)
    y = 2*np.imag(np.conj(a)*b)
    z = np.abs(a)**2 - np.abs(b)**2
    return np.array([x, y, z], dtype=float)

def lerp(a, b, t):
    return (1-t)*a + t*b

# ----------------------------
# Precompute stages for the same base points
# ----------------------------
psi_raw = random_C2(N)                         # Stage A: C^2 (no normalizado)
psi_norm = np.array([normalize_C2(p) for p in psi_raw])  # Stage B: S^3 (norm=1)

R4_raw  = np.array([to_R4(p) for p in psi_raw])   # nube en R^4
R4_norm = np.array([to_R4(p) for p in psi_norm])  # S^3 en R^4

# Para ver en 3D: elegimos 3 coordenadas de R^4 (x1,x2,x3)
R3_from_R4_raw  = R4_raw[:, :3]
R3_from_R4_norm = R4_norm[:, :3]

# Proyección estereográfica de S^3 a R^3 (solo para normalizados)
proj = []
mask = []
for x1, x2, x3, x4 in R4_norm:
    p = stereographic_S3_to_R3(x1, x2, x3, x4)
    if p is None:
        mask.append(False)
        proj.append([np.nan, np.nan, np.nan])
    else:
        mask.append(True)
        proj.append(p)
proj = np.array(proj, dtype=float)
mask = np.array(mask, dtype=bool)

# Bloch points
bloch = np.array([hopf_to_bloch(p) for p in psi_norm], dtype=float)

# Elegimos un punto "héroe" para mostrar órbita de fase
hero_idx = 5
hero_psi = psi_norm[hero_idx]

def phase_orbit(psi, K=100):
    thetas = np.linspace(0, 2*np.pi, K)
    orbit_S3proj = []
    orbit_bloch = []
    for th in thetas:
        p = np.exp(1j*th) * psi  # fase global
        r4 = to_R4(p)
        s = stereographic_S3_to_R3(r4[0], r4[1], r4[2], r4[3])
        if s is None:
            orbit_S3proj.append([np.nan, np.nan, np.nan])
        else:
            orbit_S3proj.append(s)
        orbit_bloch.append(hopf_to_bloch(p))  # debería ser constante
    return np.array(orbit_S3proj, float), np.array(orbit_bloch, float)

orbit_S3proj, orbit_bloch = phase_orbit(hero_psi, K=140)
hero_bloch = hopf_to_bloch(hero_psi)

# ----------------------------
# Plot setup
# ----------------------------
fig = plt.figure(figsize=(13, 6))
ax_left  = fig.add_subplot(121, projection='3d')
ax_right = fig.add_subplot(122, projection='3d')

# Bloch sphere surface (solo decorativo)
u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, np.pi, 30)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones_like(u), np.cos(v))
ax_right.plot_surface(xs, ys, zs, alpha=0.08)

# scatters (se actualizan)
sc_left  = ax_left.scatter([], [], [], s=6)
sc_right = ax_right.scatter([], [], [], s=6)

# hero markers
hero_left  = ax_left.scatter([], [], [], s=80, marker="x")
hero_right = ax_right.scatter([], [], [], s=80, marker="x")

# orbit line objects
orbit_left_line,  = ax_left.plot([], [], [], linewidth=2)
orbit_right_line, = ax_right.plot([], [], [], linewidth=2)

# axes labels
ax_left.set_xlabel("coord 1")
ax_left.set_ylabel("coord 2")
ax_left.set_zlabel("coord 3")

ax_right.set_xlabel("⟨σx⟩")
ax_right.set_ylabel("⟨σy⟩")
ax_right.set_zlabel("⟨σz⟩")
ax_right.set_xlim([-1.05, 1.05])
ax_right.set_ylim([-1.05, 1.05])
ax_right.set_zlim([-1.05, 1.05])

# Limits for left view (auto from proj + raw)
all_left = np.vstack([R3_from_R4_raw, R3_from_R4_norm, proj[mask]])
mins = np.nanmin(all_left, axis=0)
maxs = np.nanmax(all_left, axis=0)
pad = 0.1*(maxs - mins + 1e-9)
ax_left.set_xlim([mins[0]-pad[0], maxs[0]+pad[0]])
ax_left.set_ylim([mins[1]-pad[1], maxs[1]+pad[1]])
ax_left.set_zlim([mins[2]-pad[2], maxs[2]+pad[2]])

# ----------------------------
# Stage definitions (what left/right show)
# ----------------------------
# stage 0: C^2 as R^4 -> show first 3 coords of raw (not normalized). Right blank.
# stage 1: normalize -> interpolate raw->norm on left (first 3 coords), right still blank.
# stage 2: "see S^3" -> switch left to stereographic projection gradually, right blank.
# stage 3: Hopf map -> right shows Bloch points (and phase orbit collapses).

def stage_and_t(frame):
    stage = frame // FRAMES_PER_STAGE
    t = (frame % FRAMES_PER_STAGE) / (FRAMES_PER_STAGE - 1)
    if stage >= TOTAL_STAGES:
        stage = TOTAL_STAGES - 1
        t = 1.0
    return stage, t

def set_scatter(sc, pts):
    sc._offsets3d = (pts[:,0], pts[:,1], pts[:,2])

def init():
    ax_left.set_title("Paso 1: \u2102\u00b2 (Hilbert) como \u211d\u2074 (vista parcial)")
    ax_right.set_title("Aún no en Bloch")
    return sc_left, sc_right, hero_left, hero_right, orbit_left_line, orbit_right_line

def update(frame):
    stage, t = stage_and_t(frame)

    # Default: hide orbit lines until relevant
    orbit_left_line.set_data([], [])
    orbit_left_line.set_3d_properties([])
    orbit_right_line.set_data([], [])
    orbit_right_line.set_3d_properties([])

    if stage == 0:
        # raw cloud left
        pts_left = R3_from_R4_raw
        set_scatter(sc_left, pts_left)

        # right empty
        set_scatter(sc_right, np.zeros((1,3))*np.nan)

        # hero position on left (raw)
        h = R3_from_R4_raw[hero_idx]
        hero_left._offsets3d = ([h[0]], [h[1]], [h[2]])
        hero_right._offsets3d = ([np.nan], [np.nan], [np.nan])

        ax_left.set_title("Paso 1: \u2102\u00b2 (Hilbert) \u2245 \u211d\u2074 — nube sin normalizar (mostrando 3 coords)")
        ax_right.set_title("Paso 5 aún no: Bloch vacío")

    elif stage == 1:
        # interpolate raw -> normalized (in R^4 coords, showing first 3)
        pts_left = lerp(R3_from_R4_raw, R3_from_R4_norm, t)
        set_scatter(sc_left, pts_left)

        set_scatter(sc_right, np.zeros((1,3))*np.nan)

        h = lerp(R3_from_R4_raw[hero_idx], R3_from_R4_norm[hero_idx], t)
        hero_left._offsets3d = ([h[0]], [h[1]], [h[2]])
        hero_right._offsets3d = ([np.nan], [np.nan], [np.nan])

        ax_left.set_title("Paso 2: Normalización \u2014 forzando \u2016\u03c8\u2016=1 (entrando a S\u00b3 en \u211d\u2074)")
        ax_right.set_title("Aún no colapsamos fase ni vamos a Bloch")

    elif stage == 2:
        # move from (first 3 coords of normalized) -> stereographic projection
        # Use only mask points (avoid NaNs) for smoother view
        base = R3_from_R4_norm[mask]
        target = proj[mask]
        pts_left = lerp(base, target, t)
        set_scatter(sc_left, pts_left)

        set_scatter(sc_right, np.zeros((1,3))*np.nan)

        # hero: go to stereographic too
        h_base = R3_from_R4_norm[hero_idx]
        h_target = proj[hero_idx]
        if np.any(np.isnan(h_target)):
            h = h_base
        else:
            h = lerp(h_base, h_target, t)
        hero_left._offsets3d = ([h[0]], [h[1]], [h[2]])
        hero_right._offsets3d = ([np.nan], [np.nan], [np.nan])

        ax_left.set_title("Paso 3: Ver S\u00b3 con trampa visual \u2014 proyección estereográfica S\u00b3 \u2192 \u211d\u00b3")
        ax_right.set_title("Todavía no: cociente por fase / Hopf")

    elif stage == 3:
        # Left: show stereographic projection of S^3 (mask points)
        pts_left = proj[mask]
        set_scatter(sc_left, pts_left)

        # Right: show Bloch points (subset to keep fast)
        pts_right = bloch[:800]
        set_scatter(sc_right, pts_right)

        # Hero: on left and right
        hL = proj[hero_idx]
        if np.any(np.isnan(hL)):
            # fallback: show normalized coords if projection singular
            hL = R3_from_R4_norm[hero_idx]
        hero_left._offsets3d = ([hL[0]], [hL[1]], [hL[2]])

        hero_right._offsets3d = ([hero_bloch[0]], [hero_bloch[1]], [hero_bloch[2]])

        # Show phase orbit gradually on left (circle), and on right it stays as a point
        k = int(1 + t*(len(orbit_S3proj)-1))
        ol = orbit_S3proj[:k]
        ok = ~np.isnan(ol[:,0])
        ol = ol[ok]
        if len(ol) > 2:
            orbit_left_line.set_data(ol[:,0], ol[:,1])
            orbit_left_line.set_3d_properties(ol[:,2])

        # Right orbit: plot the first k points (should lie on top of each other)
        orr = orbit_bloch[:k]
        orbit_right_line.set_data(orr[:,0], orr[:,1])
        orbit_right_line.set_3d_properties(orr[:,2])

        ax_left.set_title("Paso 4: Fase global \u2014 \u03b8 recorre un c\u00edrculo (una fibra) en S\u00b3 (vista proyectada)")
        ax_right.set_title("Paso 5: Hopf \u2014 toda la \u00f3rbita de fase colapsa a 1 punto en Bloch (CP\u00b9 \u2245 S\u00b2)")

    return sc_left, sc_right, hero_left, hero_right, orbit_left_line, orbit_right_line

# ----------------------------
# Run animation
# ----------------------------
frames = FRAMES_PER_STAGE * TOTAL_STAGES
anim = FuncAnimation(fig, update, init_func=init, frames=frames, interval=40, blit=False)
plt.tight_layout()
plt.show()
