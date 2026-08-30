**Qubit (|ψ⟩) — Bit cuántico**

Unidad básica de información cuántica. Puede estar en superposición de |0⟩ y |1⟩ simultáneamente; sus coeficientes complejos determinan probabilidades.

|ψ⟩ = α|0⟩ + β|1⟩, |α|² + |β|² = 1

---

**Statevector (|ψ⟩) — Vector de estado**

Representación matemática completa del estado de un sistema cuántico. Es un vector en un espacio de Hilbert que contiene toda la información del sistema antes de la medición.

|ψ⟩ ∈ ℋ

---

**Orthogonal — Ortogonal**

Dos vectores son ortogonales si su producto interno es cero, lo que significa que son perpendiculares (90°) en el espacio vectorial.

⟨v, w⟩ = 0

---

**Inner product — Producto interno**

Operación que toma dos vectores y produce un número escalar que mide su “alineación”. Permite definir ángulos, norma y ortogonalidad. En espacios complejos incluye conjugación.

⟨v, w⟩ = Σ vᵢ × wᵢ

---

**Conjugation (z̄, z\*) — Conjugación (compleja)**

Operación que cambia el signo de la parte imaginaria de un número complejo.

z = a + ib → z̄ = a − ib

---

**Orthonormal (⟨vᵢ, vⱼ⟩ = δᵢⱼ) — Ortonormal**

Conjunto de vectores que son ortogonales entre sí y tienen norma 1. Esto significa que son perpendiculares y están normalizados.

⟨vᵢ, vⱼ⟩ = 0 si i ≠ j y = 1 si i = j

---

**Kronecker delta (δᵢⱼ) — Delta de Kronecker**

Función que vale 1 cuando los índices son iguales y 0 cuando son distintos. Se usa para expresar ortonormalidad y seleccionar componentes específicos.

---

**Norm (||v||) — Norma**

Magnitud o “longitud” de un vector definida por el producto interno. Indica el tamaño del vector en el espacio.

||v|| = √⟨v, v⟩

---

**Computational basis — Base computacional**

Conjunto de estados ortonormales que definen los valores clásicos 0 y 1 en un qubit.

{|0⟩, |1⟩}

---

**Complex projective space (CP¹) — Espacio proyectivo complejo**

Espacio de estados físicos de un qubit puro.

CP¹ = S³ / S¹

---

**Spin — Spin**

Propiedad cuántica intrínseca de ciertas partículas; no es una rotación clásica, sino un grado de libertad que al medirse en un eje genera valores discretos.

Para spin 1/2 da dos resultados (+ o -)

---

**Interference — Interferencia**

Fenómeno donde se combinan amplitudes complejas; pueden reforzarse o cancelarse dependiendo de su fase relativa.

---

**Global phase (e^{iθ}) — Fase global**

Factor complejo común que multiplica a todo el estado y no afecta el resultado físico.

|ψ⟩ ≡ e^{iθ}|ψ⟩

---

**Relative phase (e^{iφ}) — Fase relativa**

Diferencia de fase entre componentes del estado. Se revela mediante interferencia al cambiar de base.

α|0⟩ + e^{iφ}β|1⟩

---

**Spectral decomposition (A = Σ aₐPₐ) — Descomposición espectral**

Forma en que un operador hermítico se expresa como suma de cada eigenvalor multiplicado por su proyector asociado.

A = Σ aₐPₐ, con PₐP_b = δₐb Pₐ y Σ Pₐ = I

---

**Characteristic polynomial (det(A − λI)) — Polinomio característico**

Ecuación cuyo cero da los eigenvalores de un operador/matriz. Es el primer paso para construir proyectores espectrales y la descomposición espectral.

det(A − λI) = 0

---

**Observable — Observable**

Propiedad física de un sistema cuántico que puede ser medida experimentalmente (energía, posición, spin, etc). Matemáticamente se representa mediante un operador hermítico. Los posibles resultados de la medición son los eigenvalores del operador.

---

**QuantumCircuit — Circuito cuántico**

Representación ordenada de operaciones sobre qubits. En Qiskit, es el objeto que describe qué le haces al sistema.

---

**Unitary operator (U) — Operador unitario**

Es una transformación sobre un estado cuántico sin cambiar su norma ni probabilidades; solo lo rota o mezcla dentro del espacio. Conserva el producto interno.

U†U = I

---

**Unitary evolution (U(t)) — Evolución unitaria**

Es la forma en la que cambia un sistema cuántico en el tiempo mediante operadores unitarios, garantizando que las probabilidades se mantengan y la dinámica sea reversible.

---

**Hamiltonian (H) — Hamiltoniano**

Operador que representa la energía total del sistema y define cómo evoluciona en el tiempo.

iℏ ∂|ψ(t)⟩/∂t = H|ψ(t)⟩

---

**Schrödinger equation — Ecuación de Schrödinger**

Ley fundamental que describe cómo cambia un estado cuántico en el tiempo según el Hamiltoniano.

iℏ ∂|ψ(t)⟩/∂t = H|ψ(t)⟩

---

**Coherence (—) — Coherencia**

Capacidad de un sistema cuántico para mantener relaciones de fase bien definidas entre estados en superposición.
Permite interferencia y comportamiento no clásico observable.

Condición: fases relativas estables entre componentes del estado

---

**Decoherence (—) — Decoherencia**

Proceso por el cual un sistema cuántico pierde coherencia al interactuar con su entorno, destruyendo la información de fase.
El sistema deja de comportarse como superposición y pasa a una mezcla clásica de probabilidades.

Condición: pérdida de fase → ausencia de interferencia

---

**Non-commuting observables ([A, B] ≠ 0) — Observables no conmutativos**

Magnitudes físicas cuyos operadores no pueden intercambiarse sin alterar el resultado, lo que impide conocer sus valores simultáneamente con precisión. Reflejan un límite fundamental en la información accesible del sistema.

[A, B] = AB − BA ≠ 0

---

**Born rule — Regla de Born**

Principio que establece que la probabilidad de medir un estado cuántico es el cuadrado del módulo de su amplitud. Permite convertir información cuántica en resultados observables.

P(x) = |αₓ|²

---

**Quantum amplitude — Amplitud cuántica**

Número complejo que describe la contribución de un estado dentro de una superposición. Su módulo al cuadrado determina la probabilidad de medición.

---

**Permutation — Permutación**

Reordenamiento de los elementos de un conjunto sin eliminar ni repetir elementos. Cambia el orden, pero conserva exactamente los mismos objetos.

---

**Electromagnetic field — Campo electromagnético**

Región física donde cargas eléctricas y campos variables producen efectos eléctricos y magnéticos. Transporta energía mediante campos oscilantes.

---

**Frequency (f) — Frecuencia**

Cantidad de oscilaciones por segundo en una onda o sistema periódico. En cuántica, diferencias de energía pueden asociarse a frecuencias.

1 Hz = 1 s⁻¹, ΔE = hf

---

**Pulse — Pulso**

Aplicación limitada en el tiempo de una señal o campo electromagnético. En qubits, controla cuánto tiempo actúa el campo sobre el sistema.

---

**Resonant — Resonante**

Un sistema es resonante cuando la frecuencia aplicada coincide con su frecuencia natural de respuesta. En qubits, esto permite transferir amplitud entre niveles energéticos.

f = ΔE / h

---

**Rabi Oscillation (Ω) — Oscilación de Rabi**

Evolución oscilatoria de un sistema cuántico de dos niveles cuando un campo electromagnético resonante interactúa con él. Las probabilidades de medir |0⟩ y |1⟩ cambian sinusoidalmente en el tiempo.

P(|1⟩)=sin²(Ωt/2)

---

**Detuning (Δ) — Desintonización**

Diferencia entre la frecuencia aplicada por el campo externo y la frecuencia natural de resonancia del sistema cuántico. Produce transferencias de energía imperfectas y errores.

Δ = ω_d − ω_q

---

**Rotating Frame — Marco rotante**

Sistema de referencia matemático que rota junto con la frecuencia del drive para simplificar la dinámica del qubit y eliminar oscilaciones rápidas.

H_eff = 1/2 (ΩX + ΔZ)

---

**IQ Control (I,Q) — Control IQ**

Método de control cuántico donde las componentes I y Q controlan rotaciones sobre los ejes X e Y del qubit mediante la fase del pulso electromagnético.

H_eff ∝ I·X + Q·Y + Δ·Z

---

**Resonance — Resonancia**

Condición donde la frecuencia aplicada coincide con la diferencia de energía del sistema, permitiendo máxima transferencia de energía y control eficiente del qubit.

f = ΔE / h

---

**SINUSOIDAL (sin) — Sinusoidal**

Forma de variación suave y repetitiva que sube y baja como una onda regular. Aparece en señales, vibraciones, campos electromagnéticos y pulsos porque describe oscilaciones periódicas simples.

Fórmula: x(t)=A sin(ωt+ϕ)

---

**FERMION — Fermión**

Partícula con espín semientero que no puede ocupar exactamente el mismo estado cuántico que otra partícula idéntica. Los electrones son fermiones y obedecen el principio de exclusión de Pauli.

Condición: s = 1/2, 3/2, 5/2, ...

---

**BOSON — Bosón**

Partícula con espín entero que sí puede compartir el mismo estado cuántico con otras partículas idénticas. Por eso muchos bosones pueden actuar colectivamente como un solo estado físico.

Condición: s = 0, 1, 2, ...

---

**COMPOSITE BOSON — Bosón compuesto**

Objeto formado por un número par de fermiones que puede comportarse colectivamente como un bosón. Un par de Cooper es un ejemplo: dos electrones fermiónicos se correlacionan y actúan como una unidad bosónica.
Condición: número par de fermiones → espín total entero.

---

**MACHINE LEARNING (ML) — Aprendizaje automático**

Método mediante el cual un sistema usa datos o experiencia para ajustar su comportamiento y mejorar en una tarea.
Aprender implica modificar parámetros internos a partir de la experiencia.

---

**PARAMETER ($\theta$) — Parámetro**

Valor interno ajustable que modifica el comportamiento de un modelo.
Durante el entrenamiento, estos valores cambian para mejorar las predicciones.

---

**PREDICTION ($\hat{y}$) — Predicción**

Salida que produce un modelo para una entrada utilizando sus parámetros actuales.

$$\hat{y} = f_{\theta}(x)$$

---

**OVERFITTING — Sobreajuste**

Ocurre cuando un modelo aprende características demasiado específicas de los datos de entrenamiento y funciona peor con datos nuevos.
Buen ajuste al entrenamiento $\neq$ buena generalización.

---

**REGULARITY — Regularidad**

Patrón o relación que aparece de forma suficientemente consistente en los datos como para ser aprendido por un modelo.
La generalización depende de capturar regularidades útiles y no detalles accidentales.

---

**LOSS FUNCTION ($L$) — Función de pérdida**

Función que cuantifica qué tan incorrectas son las predicciones de un modelo.
El entrenamiento busca parámetros que produzcan una pérdida menor.

$$\theta^* = \arg\min_{\theta} L(\theta)$$

---

**MEAN SQUARED ERROR (MSE) — Error cuadrático medio**

Función de pérdida que promedia el cuadrado de las diferencias entre valores reales y predichos.
Valores menores indican predicciones más cercanas a los datos reales.

$$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$$

---

**LINEAR REGRESSION — Regresión lineal**

Modelo que aproxima la relación entre variables mediante una función lineal cuyos parámetros pueden ajustarse con los datos.

$$\hat{y} = wx + b$$
