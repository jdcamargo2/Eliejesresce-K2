import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v = np.array([[1],
             [2],
             [3]])

A = np.array([[1, 0.2, 0.0],
              [0.3, 1, 0.1],
              [0.0, 0.2, 1]])

v_p = A @ v

print(v_p)

#Puntos de un cubo de lado 2L centrado en el origen
L = 2.0

xs = np.array([-L, L])
ys = np.array([-L, L])
zs = np.array([-L, L])

#Aristas del cubo
verts = np.array([[x, y ,z] for x in xs for y in ys for z in zs]).T

#Índices de aristas
edges = [
    (0,1), (0,2), (0,4),
    (1,3), (0,5),
    (2,3), (0,6),
    (3,7),
    (4,5), (0,6),
    (5,7),
    (6,7),
]

verts_t = A @ verts

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')

#Ejes
ax.quiver(0,0,0, v[0,0], v[1,0], v[2,0], color='blue', linewidth=2, label='v')
ax.quiver(0,0,0, v_p[0,0],v_p[1,0],v_p[2,0], color='orange', linewidth=2, alpha=0.7, label="A v")

# --- Ejes originales (rojo, verde, azul)
ax.quiver(0,0,0, 1,0,0, color='crimson',  linewidth=2, alpha=0.7, label='Ejes originales')
ax.quiver(0,0,0, 0,1,0, color='limegreen',linewidth=2, alpha=0.7)
ax.quiver(0,0,0, 0,0,1, color='royalblue',linewidth=2, alpha=0.7)

# --- Ejes transformados (rojo claro, verde claro, azul claro)
ejes = np.eye(3)
ejes_t = A @ ejes
colores_t = ['lightcoral', 'lightgreen', 'lightskyblue']
for i in range(3):
    ax.quiver(0,0,0,
              ejes_t[0,i], ejes_t[1,i], ejes_t[2,i],
              color=colores_t[i], linewidth=2.5, alpha=0.9, linestyle='solid')


#Cubo original (gris)
for i,j in edges:
    p = verts[:, i]; q = verts[:, j]
    ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], color='blue', linewidth=1)

#Cubo transformado
for i,j in edges:
    p = verts_t[:, i]; q = verts_t[:, j]
    ax.plot([p[0], q[0]], [p[1], q[1]], [p[2], q[2]], color='orange', linewidth=1.5)

# Vista
ax.set_box_aspect([1,1,1])
ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_zlim(-3, 3)
ax.view_init(elev=25, azim=45)  # eleva y gira la cámara
ax.set_title("Transformación lineal 3D")
ax.legend()
plt.show()