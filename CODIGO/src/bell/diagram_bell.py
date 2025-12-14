"""
Construye el estado de Bell |Φ+>, grafica probabilidades y fases, y muestra las
esferas de Bloch (reducción por traza parcial) para evidenciar el entrelazamiento.
"""

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, partial_trace
from qiskit.visualization import plot_bloch_multivector

# 1. Construir el estado de Bell |Φ+> = (|00> + |11>)/sqrt(2)
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

# Obtenemos el statevector
sv = Statevector.from_instruction(qc)
state = sv.data  # numpy array de long 4 (|00>,|01>,|10>,|11>)

print("Statevector |Φ+>:", state)

# 2. Probabilidades en la base computacional
basis_labels = ["00", "01", "10", "11"]
probs = np.abs(state) ** 2

# 3. Fases (argumento de cada amplitud)
phases = np.angle(state)  # en radianes, entre -pi y pi

# 4. Graficar probabilidades y fases
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# --- Gráfico de probabilidades ---
axes[0].bar(basis_labels, probs)
axes[0].set_title("Probabilidades en la base computacional")
axes[0].set_ylabel("Probabilidad")

# --- Gráfico de fases ---
# Convertimos a grados solo para interpretarlo más fácil
phases_deg = phases * 180 / np.pi
axes[1].bar(basis_labels, phases_deg)
axes[1].set_title("Fases de las amplitudes")
axes[1].set_ylabel("Fase (grados)")

plt.tight_layout()
plt.show()

# 5. Esferas de Bloch para cada qubit (usando estados reducidos)
#   Tomamos la matriz de densidad total y trazamos parcial

rho = sv.to_operator().data  # matriz de densidad 4x4 (pura)
# Trazas parciales: dejamos cada qubit
rho_qubit0 = partial_trace(sv, [1])  # traza sobre qubit 1
rho_qubit1 = partial_trace(sv, [0])  # traza sobre qubit 0

print("\nMatriz reducida del qubit 0:\n", rho_qubit0.data)
print("\nMatriz reducida del qubit 1:\n", rho_qubit1.data)

# Qiskit puede dibujar la Bloch multivector directamente para el estado total.
# Para ver que cada qubit está maximálmente mezclado, usamos plot_bloch_multivector.
fig2 = plot_bloch_multivector(sv)
fig2.suptitle("Esferas de Bloch de los qubits en el estado |Φ+>", y=0.92)
plt.show()
