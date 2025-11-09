import numpy as np
import matplotlib.pyplot as plt

x = 1
y = 2

a = -2
b = 1
c = 1
d = -2


v = np.array([[x], [y]])

A = np.array([[a, b],
             [c, d]])

v_transformada = A @ v

#Vectores
print(v_transformada)
print(v)

x_vals = np.linspace(-5, 5, 11)
y_vals = np.linspace(-5, 5, 11)
X, Y = np.meshgrid(x_vals, y_vals)

puntos = np.stack([X.ravel(), Y.ravel()])

puntos_t = A @ puntos
Xt = puntos_t[0, :].reshape(X.shape)
Yt = puntos_t[1, :].reshape(Y.shape)

#Angulos en grados
ang_v = np.degrees(np.arctan2(v[1,0], v[0,0]))
ang_vp = np.degrees(np.arctan2(v_transformada[1,0], v_transformada[0,0]))
print("Ángulo v: ", ang_v, "° Ángulo en v': ", ang_vp, "° Δ: ", ang_vp - ang_v, "°")

print("||v|| = ", np.linalg.norm(v.ravel()), "    ||v'|| = ", np.linalg.norm(v_transformada.ravel()))

fig, ax = plt.subplots()
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)

#Rejilla original
for i in range(len(y_vals)):
    ax.plot(X[i, :], Y[i, :], color='lightgray', linewidth=0.5)
for j in range(len(x_vals)):
    ax.plot(X[j, :], Y[:, j], color='lightgray', linewidth=0.5)

#Rejilla transformada
for i in range(len(y_vals)):
    ax.plot(Xt[i, :], Yt[i, :], color='pink', linewidth=0.8)
for j in range(len(x_vals)):
    ax.plot(Xt[:, j], Yt[:, j], color='pink', linewidth=0.8)

# Vector original
ax.quiver(0, 0, v[0,0], v[1,0], angles='xy', scale_units='xy', scale=1, color='blue', label='Original')

#Vector transformado
ax.quiver(0, 0, v_transformada[0,0], v_transformada[1,0], angles='xy', scale_units='xy', scale=1, color='orange', alpha=0.6, width=0.008, label='Transformada')

ax.set_aspect('equal')
ax.set_xlim(-10, 15)
ax.set_ylim(-10, 15)
ax.legend()
ax.set_title("Transformación lineal: rejilla desformada")
plt.show()