Qubit (|ψ⟩) — Bit cuántico

Unidad básica de información cuántica. Puede estar en superposición de |0⟩ y |1⟩ simultáneamente; sus coeficientes complejos determinan probabilidades.
|ψ⟩ = α|0⟩ + β|1⟩, |α|² + |β|² = 1

---

Statevector (|ψ⟩) — Vector de estado

Representación matemática completa del estado de un sistema cuántico. Es un vector en un espacio de Hilbert que contiene toda la información del sistema antes de la medición.
|ψ⟩ ∈ ℋ

---

Orthogonal — Ortogonal

Dos vectores son ortogonales si su producto interno es cero, lo que significa que son perpendiculares (90°) en el espacio vectorial.
⟨v, w⟩ = 0

---

Inner product — Producto interno

Operación que toma dos vectores y produce un número escalar que mide su “alineación”. Permite definir ángulos, norma y ortogonalidad. En espacios complejos incluye conjugación.
⟨v, w⟩ = Σ vᵢ × wᵢ

---

Conjugation (z̄, z*) — Conjugación (compleja)

Operación que cambia el signo de la parte imaginaria de un número complejo.
z = a + ib → z̄ = a − ib

---

Orthonormal (⟨vᵢ, vⱼ⟩ = δᵢⱼ) — Ortonormal

Conjunto de vectores que son ortogonales entre sí y tienen norma 1. Esto significa que son perpendiculares y están normalizados.
⟨vᵢ, vⱼ⟩ = 0 si i ≠ j y = 1 si i = j

---

Kronecker delta (δᵢⱼ) — Delta de Kronecker

Función que vale 1 cuando los índices son iguales y 0 cuando son distintos. Se usa
para expresar ortonormalidad y seleccionar componentes específicos.

---

Norm (||v||) — Norma

Magnitud o “longitud” de un vector definida por el producto interno. Indica el tamaño del vector en el espacio.
||v|| = √⟨v, v⟩

---

Computational basis — Base computacional

Conjunto de estados ortonormales que definen los valores clásicos 0 y 1 en un qubit.
{|0⟩, |1⟩}

---

Complex projective space (CP¹) — Espacio proyectivo complejo

Espacio de estados físicos de un qubit puro.
CP¹ = S³ / S¹

---

Spin — Spin

Propiedad cuántica intrínseca de ciertas partículas; no es una rotación clásica, sino un grado de libertad que al medirse en un eje genera valores discretos.
Para spin 1/2 da dos resultados (+ o -)

---

Interference — Interferencia

Fenómeno donde se combinan amplitudes complejas; pueden reforzarse o cancelarse dependiendo de su fase relativa.

---

Global phase (e^{iθ}) — Fase global

Factor complejo común que multiplica a todo el estado y no afecta el resultado físico.
|ψ⟩ ≡ e^{iθ}|ψ⟩

---

Relative phase (e^{iφ}) — Fase relativa

Diferencia de fase entre componentes del estado. Se revela mediante interferencia al cambiar de base.
α|0⟩ + e^{iφ}β|1⟩

---

Spectral decomposition (A = Σ aₐPₐ) — Descomposición espectral

Forma en que un operador hermítico se expresa como suma de cada eigenvalor multiplicado por su proyector asociado.
A = Σ aₐPₐ, con PₐP_b = δₐb Pₐ y Σ Pₐ = I

---

Characteristic polynomial (det(A − λI)) — Polinomio característico

Ecuación cuyo cero da los eigenvalores de un operador/matriz. Es el primer paso para construir proyectores espectrales y la descomposición espectral.
det(A − λI) = 0

---

Observable — Observable

Propiedad física de un sistema cuántico que puede ser medida experimentalmente (energía, posición, spin, etc). Matemáticamente se representa mediante un operador hermítico. Los posibles resultados de la medición son los eigenvalores del operador.

---

QuantumCircuit — Circuito cuántico

Representación ordenada de operaciones sobre qubits. En Qiskit, es el objeto que describe qué le haces al sistema.

---

Unitary operator (U) — Operador unitario

Es una transformación sobre un estado cuántico sin cambiar su norma ni probabilidades; solo lo rota o mezcla dentro del espacio. Conserva el producto interno.
U†U = I

---

Unitary evolution (U(t)) — Evolución unitaria

Es la forma en la que cambia un sistema cuántico en el tiempo mediante operadores unitarios, garantizando que las probabilidades se mantengan y la dinámica sea reversible.

---

Hamiltonian (H) — Hamiltoniano

Operador que representa la energía total del sistema y define cómo evoluciona en el tiempo.
iℏ ∂|ψ(t)⟩/∂t = H|ψ(t)⟩

---

Schrödinger equation — Ecuación de Schrödinger

Ley fundamental que describe cómo cambia un estado cuántico en el tiempo según el Hamiltoniano.
iℏ ∂|ψ(t)⟩/∂t = H|ψ(t)⟩

---

Coherence (—) — Coherencia

Capacidad de un sistema cuántico para mantener relaciones de fase bien definidas entre estados en superposición.
Permite interferencia y comportamiento no clásico observable.
Condición: fases relativas estables entre componentes del estado

---

Decoherence (—) — Decoherencia

Proceso por el cual un sistema cuántico pierde coherencia al interactuar con su entorno, destruyendo la información de fase.
El sistema deja de comportarse como superposición y pasa a una mezcla clásica de probabilidades.
Condición: pérdida de fase → ausencia de interferencia

---

Non-commuting observables ([A, B] ≠ 0) — Observables no conmutativos

Magnitudes físicas cuyos operadores no pueden intercambiarse sin alterar el resultado, lo que impide conocer sus valores simultáneamente con precisión. Reflejan un límite fundamental en la información accesible del sistema.

[A, B] = AB − BA ≠ 0
