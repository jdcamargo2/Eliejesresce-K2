import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization.bloch import Bloch
import matplotlib.pyplot as plt


def get_state_from_ry(theta: float) -> Statevector:
    """
    Devuelve el estado después de aplicar RY(theta) a |0>.
    """
    qc = QuantumCircuit(1)
    qc.ry(theta, 0)
    return Statevector.from_instruction(qc)


def state_to_bloch_vector(state: Statevector) -> np.ndarray:
    """
    Convierte un statevector de 1 qubit en su vector (x, y, z)
    en la esfera de Bloch.
    """
    data = state.data
    if len(data) != 2:
        raise ValueError("Este conversor solo funciona para 1 qubit.")

    alpha = data[0]
    beta = data[1]

    # Fórmulas estándar de la esfera de Bloch
    alpha_conj_beta = np.conjugate(alpha) * beta

    x = 2 * np.real(alpha_conj_beta)
    y = 2 * np.imag(alpha_conj_beta)
    z = np.abs(alpha) ** 2 - np.abs(beta) ** 2

    return np.array([x, y, z], dtype=float)


def animate_ry_rotation(num_frames: int = 40) -> None:
    """
    Animación estable de una rotación RY(theta) desde 0 hasta π
    usando Bloch() SIN crear ventanas infinitas.
    """
    plt.ion()  # modo interactivo
    fig = plt.figure()
    bloch = Bloch(fig=fig)

    for step in range(num_frames + 1):
        theta = np.pi * step / num_frames
        state = get_state_from_ry(theta)
        bloch_vec = state_to_bloch_vector(state)

        # Limpiar y dibujar el nuevo vector
        bloch.clear()
        bloch.add_vectors(bloch_vec)
        bloch.make_sphere()

        plt.title(f"Rotación RY, θ = {theta:.2f} rad")
        plt.pause(0.1)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    animate_ry_rotation()
