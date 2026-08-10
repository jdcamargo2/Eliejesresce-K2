"""
Simula interactivamente la respuesta de un qubit a un pulso de microondas
con frecuencia, amplitud, duración y fase ajustables. La evolución temporal
se anima sobre la onda enviada, la población excitada y la esfera de Bloch.
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button


# ============================================================
# CONFIGURACIÓN FÍSICA
# ============================================================

F_QUBIT = 5.0  # GHz

X = np.array(
    [
        [0.0, 1.0],
        [1.0, 0.0],
    ],
    dtype=complex,
)

Y = np.array(
    [
        [0.0, -1.0j],
        [1.0j, 0.0],
    ],
    dtype=complex,
)

Z = np.array(
    [
        [1.0, 0.0],
        [0.0, -1.0],
    ],
    dtype=complex,
)

IDENTITY = np.eye(2, dtype=complex)
GROUND_STATE = np.array([1.0, 0.0], dtype=complex)


# ============================================================
# SIMULACIÓN DEL QUBIT
# ============================================================

def simulate_qubit(
    drive_frequency: float,
    amplitude: float,
    duration: float,
    phase_degrees: float,
    samples: int = 700,
) -> dict[str, np.ndarray | float]:
    """
    Calcula la evolución del qubit bajo un pulso constante en el marco rotante.

    Las frecuencias se expresan en GHz y el tiempo en ns, por lo que
    1 GHz equivale a 1 ciclo por nanosegundo.
    """

    if duration <= 0:
        raise ValueError("La duración debe ser mayor que cero.")

    phase = np.deg2rad(phase_degrees)
    detuning = F_QUBIT - drive_frequency

    times = np.linspace(0.0, duration, samples)

    effective_frequency = np.sqrt(
        detuning**2 + amplitude**2
    )

    if effective_frequency < 1e-12:
        states = np.tile(GROUND_STATE, (samples, 1))
    else:
        rotation_operator = (
            detuning * Z
            + amplitude
            * (
                np.cos(phase) * X
                + np.sin(phase) * Y
            )
        ) / effective_frequency

        angle = np.pi * effective_frequency * times

        states = np.empty((samples, 2), dtype=complex)

        for index, current_angle in enumerate(angle):
            unitary = (
                np.cos(current_angle) * IDENTITY
                - 1.0j
                * np.sin(current_angle)
                * rotation_operator
            )

            states[index] = unitary @ GROUND_STATE

    alpha = states[:, 0]
    beta = states[:, 1]

    population = np.abs(beta) ** 2

    bloch_x = 2.0 * np.real(np.conjugate(alpha) * beta)
    bloch_y = 2.0 * np.imag(np.conjugate(alpha) * beta)
    bloch_z = np.abs(alpha) ** 2 - np.abs(beta) ** 2

    sent_wave = amplitude * np.cos(
        2.0 * np.pi * drive_frequency * times
        + phase
    )

    return {
        "times": times,
        "wave": sent_wave,
        "population": population,
        "bloch_x": bloch_x,
        "bloch_y": bloch_y,
        "bloch_z": bloch_z,
        "detuning": detuning,
        "effective_frequency": effective_frequency,
    }


# ============================================================
# LABORATORIO INTERACTIVO
# ============================================================

class QuantumSpectroscopyLab:
    def __init__(self) -> None:
        self.is_playing = True
        self.current_frame = 0

        self.figure = plt.figure(figsize=(16, 9))
        self.figure.subplots_adjust(
            left=0.08,
            right=0.96,
            top=0.87,
            bottom=0.27,
            wspace=0.28,
            hspace=0.40,
        )

        grid = self.figure.add_gridspec(
            2,
            2,
            width_ratios=[1.45, 1.0],
        )

        self.wave_axis = self.figure.add_subplot(grid[0, 0])
        self.population_axis = self.figure.add_subplot(grid[1, 0])
        self.bloch_axis = self.figure.add_subplot(
            grid[:, 1],
            projection="3d",
        )

        self._create_sliders()
        self._create_buttons()
        self._create_bloch_sphere()

        self.data = self._calculate_current_data()
        self._create_plot_elements()
        self._update_static_plots()

        self.frequency_slider.on_changed(self._slider_changed)
        self.amplitude_slider.on_changed(self._slider_changed)
        self.duration_slider.on_changed(self._slider_changed)
        self.phase_slider.on_changed(self._slider_changed)

        self.animation = FuncAnimation(
            self.figure,
            self._animate,
            interval=20,
            blit=False,
            cache_frame_data=False,
        )

    # --------------------------------------------------------
    # CONTROLES
    # --------------------------------------------------------

    def _create_sliders(self) -> None:
        frequency_axis = self.figure.add_axes(
            [0.15, 0.19, 0.58, 0.025]
        )
        amplitude_axis = self.figure.add_axes(
            [0.15, 0.15, 0.58, 0.025]
        )
        duration_axis = self.figure.add_axes(
            [0.15, 0.11, 0.58, 0.025]
        )
        phase_axis = self.figure.add_axes(
            [0.15, 0.07, 0.58, 0.025]
        )

        self.frequency_slider = Slider(
            ax=frequency_axis,
            label="Frecuencia fd (GHz)",
            valmin=4.50,
            valmax=5.50,
            valinit=4.85,
            valstep=0.005,
        )

        self.amplitude_slider = Slider(
            ax=amplitude_axis,
            label="Amplitud Ω (GHz)",
            valmin=0.01,
            valmax=0.50,
            valinit=0.10,
            valstep=0.005,
        )

        self.duration_slider = Slider(
            ax=duration_axis,
            label="Duración T (ns)",
            valmin=1.0,
            valmax=50.0,
            valinit=10.0,
            valstep=0.1,
        )

        self.phase_slider = Slider(
            ax=phase_axis,
            label="Fase φ (°)",
            valmin=0.0,
            valmax=360.0,
            valinit=0.0,
            valstep=1.0,
        )

    def _create_buttons(self) -> None:
        play_axis = self.figure.add_axes(
            [0.78, 0.145, 0.09, 0.045]
        )
        reset_axis = self.figure.add_axes(
            [0.88, 0.145, 0.09, 0.045]
        )

        self.play_button = Button(
            play_axis,
            "Pausar",
        )
        self.reset_button = Button(
            reset_axis,
            "Reiniciar",
        )

        self.play_button.on_clicked(self._toggle_animation)
        self.reset_button.on_clicked(self._reset_lab)

    # --------------------------------------------------------
    # CÁLCULOS
    # --------------------------------------------------------

    def _calculate_current_data(self) -> dict:
        return simulate_qubit(
            drive_frequency=self.frequency_slider.val,
            amplitude=self.amplitude_slider.val,
            duration=self.duration_slider.val,
            phase_degrees=self.phase_slider.val,
        )

    # --------------------------------------------------------
    # GRÁFICAS
    # --------------------------------------------------------

    def _create_bloch_sphere(self) -> None:
        u = np.linspace(0.0, 2.0 * np.pi, 45)
        v = np.linspace(0.0, np.pi, 25)

        sphere_x = np.outer(np.cos(u), np.sin(v))
        sphere_y = np.outer(np.sin(u), np.sin(v))
        sphere_z = np.outer(np.ones_like(u), np.cos(v))

        self.bloch_axis.plot_wireframe(
            sphere_x,
            sphere_y,
            sphere_z,
            linewidth=0.35,
            alpha=0.17,
        )

        self.bloch_axis.plot(
            [-1, 1],
            [0, 0],
            [0, 0],
            linewidth=0.9,
        )
        self.bloch_axis.plot(
            [0, 0],
            [-1, 1],
            [0, 0],
            linewidth=0.9,
        )
        self.bloch_axis.plot(
            [0, 0],
            [0, 0],
            [-1, 1],
            linewidth=0.9,
        )

        self.bloch_axis.text(1.10, 0, 0, "X")
        self.bloch_axis.text(0, 1.10, 0, "Y")
        self.bloch_axis.text(0, 0, 1.12, "|0⟩")
        self.bloch_axis.text(0, 0, -1.20, "|1⟩")

        self.bloch_axis.set_xlim(-1.15, 1.15)
        self.bloch_axis.set_ylim(-1.15, 1.15)
        self.bloch_axis.set_zlim(-1.15, 1.15)
        self.bloch_axis.set_box_aspect((1, 1, 1))

        self.bloch_axis.set_xticks([])
        self.bloch_axis.set_yticks([])
        self.bloch_axis.set_zticks([])

        self.bloch_axis.set_title(
            "Trayectoria en la esfera de Bloch"
        )

    def _create_plot_elements(self) -> None:
        self.wave_line, = self.wave_axis.plot([], [])
        self.wave_cursor = self.wave_axis.axvline(
            0.0,
            linestyle="--",
            linewidth=1.0,
        )
        self.wave_point, = self.wave_axis.plot(
            [],
            [],
            marker="o",
            markersize=7,
        )

        self.population_line, = self.population_axis.plot([], [])
        self.population_cursor = self.population_axis.axvline(
            0.0,
            linestyle="--",
            linewidth=1.0,
        )
        self.population_point, = self.population_axis.plot(
            [],
            [],
            marker="o",
            markersize=8,
        )

        self.bloch_path, = self.bloch_axis.plot(
            [],
            [],
            [],
            linewidth=2.0,
        )
        self.bloch_point, = self.bloch_axis.plot(
            [],
            [],
            [],
            marker="o",
            markersize=8,
        )

        self.time_text = self.figure.text(
            0.80,
            0.10,
            "",
            fontsize=11,
        )

    def _update_static_plots(self) -> None:
        times = self.data["times"]
        wave = self.data["wave"]
        population = self.data["population"]

        self.wave_line.set_data(times, wave)
        self.population_line.set_data(times, population)

        amplitude_limit = max(
            abs(self.amplitude_slider.val) * 1.2,
            0.05,
        )

        self.wave_axis.set_xlim(0.0, times[-1])
        self.wave_axis.set_ylim(
            -amplitude_limit,
            amplitude_limit,
        )

        self.population_axis.set_xlim(0.0, times[-1])
        self.population_axis.set_ylim(-0.05, 1.05)

        self.wave_axis.set_title(
            "Pulso de microondas enviado"
        )
        self.wave_axis.set_xlabel("Tiempo (ns)")
        self.wave_axis.set_ylabel("Amplitud relativa")
        self.wave_axis.grid(alpha=0.25)

        self.population_axis.set_title(
            "Respuesta del qubit"
        )
        self.population_axis.set_xlabel("Tiempo (ns)")
        self.population_axis.set_ylabel(
            "Población excitada P₁"
        )
        self.population_axis.grid(alpha=0.25)

        self.population_axis.axhline(
            1.0,
            linestyle=":",
            linewidth=0.9,
        )

        self._update_title()
        self.figure.canvas.draw_idle()

    def _update_title(self) -> None:
        detuning = self.data["detuning"]

        if abs(detuning) < 0.01:
            resonance_text = "EN RESONANCIA"
        else:
            resonance_text = "FUERA DE RESONANCIA"

        final_population = self.data["population"][-1]

        self.figure.suptitle(
            (
                "Laboratorio interactivo de espectroscopía cuántica\n"
                f"fq = {F_QUBIT:.3f} GHz | "
                f"fd = {self.frequency_slider.val:.3f} GHz | "
                f"Δ = {detuning:+.3f} GHz | "
                f"P₁ final = {final_population:.3f} | "
                f"{resonance_text}"
            ),
            fontsize=14,
        )

    # --------------------------------------------------------
    # ANIMACIÓN
    # --------------------------------------------------------

    def _animate(self, _frame: int):
        if not self.is_playing:
            return

        samples = len(self.data["times"])

        self.current_frame += 3

        if self.current_frame >= samples:
            self.current_frame = 0

        index = self.current_frame

        times = self.data["times"]
        wave = self.data["wave"]
        population = self.data["population"]

        bloch_x = self.data["bloch_x"]
        bloch_y = self.data["bloch_y"]
        bloch_z = self.data["bloch_z"]

        current_time = times[index]

        self.wave_cursor.set_xdata(
            [current_time, current_time]
        )
        self.population_cursor.set_xdata(
            [current_time, current_time]
        )

        self.wave_point.set_data(
            [current_time],
            [wave[index]],
        )
        self.population_point.set_data(
            [current_time],
            [population[index]],
        )

        self.bloch_path.set_data(
            bloch_x[: index + 1],
            bloch_y[: index + 1],
        )
        self.bloch_path.set_3d_properties(
            bloch_z[: index + 1]
        )

        self.bloch_point.set_data(
            [bloch_x[index]],
            [bloch_y[index]],
        )
        self.bloch_point.set_3d_properties(
            [bloch_z[index]]
        )

        self.time_text.set_text(
            (
                f"t = {current_time:.2f} ns\n"
                f"P₁ = {population[index]:.3f}"
            )
        )

        self.figure.canvas.draw_idle()

    # --------------------------------------------------------
    # EVENTOS
    # --------------------------------------------------------

    def _slider_changed(self, _value: float) -> None:
        self.data = self._calculate_current_data()
        self.current_frame = 0
        self._update_static_plots()

    def _toggle_animation(self, _event) -> None:
        self.is_playing = not self.is_playing

        if self.is_playing:
            self.play_button.label.set_text("Pausar")
        else:
            self.play_button.label.set_text("Continuar")

        self.figure.canvas.draw_idle()

    def _reset_lab(self, _event) -> None:
        self.frequency_slider.reset()
        self.amplitude_slider.reset()
        self.duration_slider.reset()
        self.phase_slider.reset()

        self.current_frame = 0
        self.is_playing = True

        self.play_button.label.set_text("Pausar")
        self.figure.canvas.draw_idle()

    def run(self) -> None:
        plt.show()


# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    laboratory = QuantumSpectroscopyLab()
    laboratory.run()