"""
Versión mínima de Grover (2 qubits)
para visualizar amplificación de amplitud.
"""

import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


# =========================
# Utilidades
# =========================

def probabilidades(statevector: Statevector):
    """Devuelve |amplitud|^2 de cada estado"""
    return np.abs(statevector.data) ** 2


def graficar(probs, titulo):
    n = int(np.log2(len(probs)))
    etiquetas = [format(i, f"0{n}b") for i in range(len(probs))]

    plt.figure(figsize=(6, 3.5))
    plt.bar(etiquetas, probs)
    plt.ylim(0, 1)
    plt.xlabel("Estado |x⟩")
    plt.ylabel("Probabilidad")
    plt.title(titulo)
    plt.tight_layout()
    plt.show()


# =========================
# Oráculo y difusión
# =========================

def oraculo_11(qc: QuantumCircuit):
    """
    Marca el estado |11⟩ cambiando solo su fase
    (NO cambia probabilidades)
    """
    qc.cz(0, 1)


def difusion_2q(qc: QuantumCircuit):
    """
    Operador de difusión (inversión sobre el promedio)
    para 2 qubits
    """
    qc.h([0, 1])
    qc.x([0, 1])
    qc.h(1)
    qc.cx(0, 1)
    qc.h(1)
    qc.x([0, 1])
    qc.h([0, 1])


# =========================
# 1. Estado inicial uniforme
# =========================

qc0 = QuantumCircuit(2)
qc0.h([0, 1])

sv0 = Statevector.from_instruction(qc0)
graficar(probabilidades(sv0),
         "Estado inicial: superposición uniforme (H ⊗ H)")


# =========================
# 2. Aplicamos el oráculo
# =========================

qc1 = qc0.copy()
oraculo_11(qc1)

sv1 = Statevector.from_instruction(qc1)
graficar(probabilidades(sv1),
         "Después del oráculo: solo cambia la fase de |11⟩")


# =========================
# 3. Aplicamos difusión
# =========================

qc2 = qc1.copy()
difusion_2q(qc2)

sv2 = Statevector.from_instruction(qc2)
graficar(probabilidades(sv2),
         "Después de la difusión: amplitud de |11⟩ amplificada")


# =========================
# 4. Segunda iteración (overshoot)
# =========================

qc3 = qc2.copy()
oraculo_11(qc3)
difusion_2q(qc3)

sv3 = Statevector.from_instruction(qc3)
graficar(probabilidades(sv3),
         "Dos iteraciones: ejemplo de pasarse del objetivo")


print("Circuito de Grover (1 iteración):")
print(qc2.draw("text"))
