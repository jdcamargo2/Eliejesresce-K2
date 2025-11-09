import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

v = np.array([[1],
             [2],
             [3]])

A = np.array([[1, 0.2, 0.0],
              [0.3, 1, 0.1],
              [0.0, 0.2, 1]])

v_p = A @ v

print(v_p)

# Puntos de un cubo de lado 2L centrado en el origen
L = 2.0
xs = np.array([-L, L])
ys = np.array([-L, L])
zs = np.array([-L, L])

# Aristas del cubo
# (Generadas automáticamente: conectamos vértices que difieren en exactamente un eje)
verts_list = np.array([[x, y, z] for x in xs for y in ys for z in zs], dtype=float)  # (8,3)
verts = verts_list.T  # (3,8) para respetar tu formato original si lo necesitas en columnas

def generar_aristas(verts_8x3):
    E = []
    for i in range(len(verts_8x3)):
        for j in range(i+1, len(verts_8x3)):
            diff = np.abs(verts_8x3[i] - verts_8x3[j])
            # En un cubo, dos vértices forman arista si sólo cambia 1 coordenada
            if np.count_nonzero(diff) == 1:
                E.append((i, j))
    return E

# Índices de aristas
edges = generar_aristas(verts_list)

# (Caras del cubo para dibujar superficies semitransparentes y mejorar la lectura)
faces_idx = [
    [0,1,3,2],  # z = -L
    [4,5,7,6],  # z = +L
    [0,1,5,4],  # y = -L
    [2,3,7,6],  # y = +L
    [0,2,6,4],  # x = -L
    [1,3,7,5],  # x = +L
]

# Aplicamos la transformación a todos los vértices (forma vectorizada y estable)
verts_t_list = (A @ verts_list.T).T  # (8,3)
verts_t = verts_t_list.T             # (3,8) si quisieras usar columnas

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

# Ejes
ax.quiver(0,0,0, v[0,0], v[1,0], v[2,0], color='blue', linewidth=2, label='v')
ax.quiver(0,0,0, v_p[0,0],v_p[1,0],v_p[2,0], color='orange', linewidth=2, alpha=0.85, label="A v")

# --- Ejes originales (rojo, verde, azul)
ax.quiver(0,0,0, 1,0,0, color='crimson',  linewidth=2, alpha=0.9, label='Ejes originales')
ax.quiver(0,0,0, 0,1,0, color='limegreen',linewidth=2, alpha=0.9)
ax.quiver(0,0,0, 0,0,1, color='royalblue',linewidth=2, alpha=0.9)

# --- Ejes transformados (rojo claro, verde claro, azul claro)
ejes = np.eye(3)
ejes_t = A @ ejes
colores_t = ['lightcoral', 'lightgreen', 'lightskyblue']
for i in range(3):
    ax.quiver(0,0,0,
              ejes_t[0,i], ejes_t[1,i], ejes_t[2,i],
              color=colores_t[i], linewidth=2.5, alpha=0.9, linestyle='solid')

# Cubo original (gris)
# (Añadimos caras semitransparentes + aristas limpias para mejor lectura)
faces = [verts_list[idx] for idx in faces_idx]
pc = Poly3DCollection(faces, facecolor='gray', alpha=0.10, edgecolor='none')
ax.add_collection3d(pc)
edge_segs = [(verts_list[i], verts_list[j]) for (i,j) in edges]
lc = Line3DCollection(edge_segs, colors='blue', linewidths=1.2, alpha=0.9)
ax.add_collection3d(lc)

# Cubo transformado
faces_t = [verts_t_list[idx] for idx in faces_idx]
pc_t = Poly3DCollection(faces_t, facecolor='orange', alpha=0.18, edgecolor='none')
ax.add_collection3d(pc_t)
edge_segs_t = [(verts_t_list[i], verts_t_list[j]) for (i,j) in edges]
lc_t = Line3DCollection(edge_segs_t, colors='orange', linewidths=1.6, alpha=0.95)
ax.add_collection3d(lc_t)

# Vista
# (Límites y aspecto ajustados automáticamente a todos los puntos para no recortar nada)
all_pts = np.vstack([verts_list, verts_t_list])
mins = all_pts.min(axis=0) - 0.5
maxs = all_pts.max(axis=0) + 0.5
ax.set_xlim(mins[0], maxs[0]); ax.set_ylim(mins[1], maxs[1]); ax.set_zlim(mins[2], maxs[2])
ax.set_box_aspect(np.ptp(all_pts, axis=0))
ax.view_init(elev=25, azim=45)  # eleva y gira la cámara
ax.set_title("Transformación lineal 3D")
ax.legend(loc='upper left')
plt.tight_layout()
plt.show()
