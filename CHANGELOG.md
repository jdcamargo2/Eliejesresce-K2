# CHANGELOG – Elíejesresce K2

> Nota: Las semanas se contabilizan de lunes a domingo.
>
> Excepción: La Semana 1 inicia el domingo 2025-11-02,
> fecha de creación formal del proyecto.
> El estudio sistemático comenzó el lunes siguiente.
>
> El domingo se utiliza como día de cierre y publicación del trabajo semanal.

---

## Semana 1 (2025-11-02 al 2025-11-09)

### Inicio del proyecto

- Creación del repositorio y estructura inicial.
- Definición conceptual de Elí-, -ejes- y -resce.
- Inicio del Diario de Bordo y Biblioteca K2.
- Primeras lecturas y reflexiones sobre identidad y propósito.
- Configuración del entorno de trabajo (VS Code, extensiones, organización).
- Primeros ejercicios de Álgebra Lineal (vectores, matrices, determinantes).
- Introducción a qubits y Esfera de Bloch.

### Diario y Biblioteca

- Exportado y organizado el Diario de Bordo Semana 1 en PDF.
- Exportada y organizada la Biblioteca Semana 1 en PDF.

### Código

- Exportado y organizado prueba en Qiskit.
- Exportado y organizado simulación de transformación lineal en 2D y 3D en python.

---

## Semana 2 (2025-11-10 al 2025-11-16)

### Teoría y aprendizaje

- Ampliada base teórica en Álgebra Lineal: determinantes, cofactores, Sarrus, interpretación geométrica.
- Estudiados conceptos de transpuesta, conjugado y conjugada transpuesta.
- Revisión de compuertas cuánticas adicionales y concepto de matrices unitarias.
- Relación entre determinante y operaciones cuánticas (|det(U)| = 1).

### Diario y Biblioteca

- Exportado y organizado el Diario de Bordo Semana 2 en PDF.
- Exportada y organizada la Biblioteca Semana 2 en PDF.

### Código

- Semana sin nuevos scripts; enfoque completamente teórico.

### Otros

- Reordenamiento del repositorio y limpieza de carpetas.

---

## Semana 3 (2025-11-17 al 2025-11-23)

### Teoría y aprendizaje

- Repaso intensivo de Álgebra Lineal aplicada: normalización, producto
  interno, amplitudes y probabilidades.
- Comprensión profunda del papel de la norma en estados cuánticos.
- Introducción formal a fases, ángulos (φ, ϕ) y su relación con la
  Esfera de Bloch.
- Consolidación del concepto de amplitud vs probabilidad.
- Reflexión sobre colapso, interpretación geométrica y estados puros.

### Diario y Biblioteca

- Exportado y organizado el Diario de Bordo Semana 3 en PDF.
- Exportada y organizada la Biblioteca Semana 3 en PDF.

### Código y prácticas

- Primeras pruebas visuales con rotaciones en la Esfera de Bloch.
- Implementación inicial de animaciones simples.
- Inicio de pruebas con representaciones gráficas en Python.

### Otros

- Avances conceptuales importantes para preparar animaciones más
  complejas.
- Registro de reflexiones personales en Diario de Bordo.

---

## Semana 4 (2025-11-24 al 2025-11-30)

### Teoría y aprendizaje

- Análisis profundo de trayectorias en la Esfera de Bloch.
- Revisión del comportamiento de compuertas cuánticas (H, X, Z) en
  simulación.
- Entendimiento del paralelismo cuántico a nivel visual.
- Lecturas complementarias sobre estados y rotaciones.

### Diario y Biblioteca

- Separación completa del Diario de Bordo por semanas individuales.
- Exportado y organizado el Diario de Bordo Semana 4 en PDF.
- Reorganización completa de la Biblioteca dentro de `/2025/`.
- Eliminación de duplicados acumulativos para mantener trazabilidad
  clara.

### Código

- Corrección del entorno virtual (venv) y restauración de
  dependencias.
- Arreglo del problema de importación de Qiskit en VS Code.
- Solución al bug de BlochAnimation que generaba ventanas infinitas.
- Estructuración final de carpetas de código.
- Implementación de carpetas de mediciones y generación correcta de
  CSV.

### Estructura del repositorio

- Limpieza masiva de archivos incorrectos, duplicados o innecesarios.
- Eliminación definitiva de cualquier resto acumulativo previo.
- Clarificación y normalización de las rutas del proyecto.
- Preparación para futuros README de módulos.

### FRASES

- Creada la carpeta FRASES.
- Añadidos los archivos iniciales "Disvarianza Mental" y "Lejos en
  Espacio" como placeholders para futuros poemas.

### Notas

- READMEs quedan programados para el próximo domingo.
- Repositorio queda alineado al estándar Elíejesresce-K2.

---

## Semana 5 (2025-12-01 al 2025-12-07)

### Teoría y aprendizaje

- Transición de Campamento 1 a Campamento 2 en el estudio cuántico.
- Comprensión completa de la estructura de un circuito en Qiskit (crear, agregar compuertas, medir, ejecutar y analizar).
- Estudio formal del **producto tensorial** y su rol en sistemas de 2 qubits.
- Análisis profundo del comportamiento y propósito de la puerta **CNOT** (control, objetivo, orden, matriz 4×4).
- Diferenciación algebraica entre **estados separables** y **estados entrelazados** mediante el criterio *ad – bc*.
- Introducción y comprensión conceptual de los **cuatro estados de Bell**.
- Primer puente teórico entre Bloch ↔ Qiskit ↔ Álgebra lineal ↔ Estados de Bell.

### Diario y Biblioteca

- Exportado y organizado el **Diario de Bordo – Semana 5** en PDF (Días 21–25).
- Exportada y organizada la **Biblioteca – Semana 5** en PDF (Días 21–25).
- Contenido coherente y alineado con la progresión teórica de la semana.

### Código

- Consolidación de los scripts iniciales dentro de `src/qiskit_projects/learning/`.
- `circuit.py`: estructura base de circuitos y flujo operativo.
- `convencion.py`: definición y estandarización de convenciones Bloch ↔ Qiskit.
- `statevector.py`: obtención, análisis y visualización del vector de estado.
- `bell.py`: implementación y medición de los cuatro estados de Bell.
- `blochAnimation.py`: preparación del módulo para futuras animaciones unificadas.
- Todos los archivos reciben encabezados de documentación indicando su propósito.

### Estructura del repositorio

- Integración completa de Semana 5 en la arquitectura general de Elíejesresce K2.
- Confirmada la trazabilidad limpia sin duplicados ni inconsistencias.
- Actualizada la descripción de la estructura del repositorio para reflejar la organización real bajo `CODIGO/src/`.
- Consolidados los módulos principales en:

  - `esfera_bloch/` para simulaciones y animaciones de la Esfera de Bloch.
  - `qiskit_projects/learning/` para scripts de práctica con Qiskit.
  - `transformacion_lineal/` para visualizaciones y ejercicios de álgebra lineal.
  - `bell.py`: implementación y medición de los cuatro estados de Bell.
  - `blochAnimation.py`: base para futuras animaciones unificadas.
  - Archivos adicionales en preparación (circuit.py, convencion.py, statevector.py) aún no integrados en la carpeta `learning/`.
- Eliminadas referencias anteriores a una estructura `CODIGO/PYTHON` y `CODIGO/QISKIT` que ya no corresponden al estado actual del proyecto.

### Normalización de archivos

- Renombrados todos los PDFs de Biblioteca y Diario para seguir la convención:
  `Nombre_Semana_XX.pdf`.
- Sustituidos espacios por guiones bajos para evitar errores en rutas y asegurar coherencia.

### Notas

- README actualizado parcialmente; progreso semanal ampliado hasta Semana 5.
- Estructura del repositorio actualizada.
- Semana 5 marca el inicio formal del estudio del **entrelazamiento cuántico**.

---

## Semana 6 (2025-12-08 al 2025-12-14)

### Teoría y aprendizaje

- Trabajo centrado en **entrelazamiento**, **Bell measurement** y **teleportación cuántica.**
- Aparición de **fricción conceptual** al interpretar:
  - el significado real de una medición en la base de Bell,
  - la relación entre los diagramas del protocolo de teleportación y su lectura física/matemática.
- Identificación de interpretaciones incorrectas iniciales (medir como “revelar un estado”) y comienzo de su corrección hacia la idea de **medición como proyección**.
- Proceso reiterativo de ir y volver entre:
  - álgebra,
  - diagramas,
  - circuitos en Qiskit,
- La semana no busca cerrar teleportación, sino **entender qué pieza conceptual faltaba** para poder hacerlo correctamente.

### Diario y Biblioteca

- Exportado y organizado el **Diario de Bordo - Semana 6** en PDF.
- Exportada y organizada la **Biblioteca - Semana 6** en PDF.

### Código

- Reorganización del código para agrupar **Python y Qiskit por tema**, reflejando el modo real de estudio (concepto → prueba → revisión).
- Código mantenido flexible para repetir experimentos, cambiar estados iniciales y observar resultados sin forzar conclusiones.

### Estructura del repositorio

- Ajuste de la estructura del repositorio para favorecer la navegación por **conceptos** (Bell, Bloch, teleportación) en lugar de por tecnologías.
- Identificación de puntos a refinar en la organización (nombres, versiones paralelas), sin romper la trazabilidad del trabajo realizado.

### Normalización de archivos

- Consolidación de los archivos:
  - `Biblioteca - Semana 6.pdf`
  - `Diario de Bordo - Semana 6.pdf`
- Semana documentada de forma completa.

### Notas

- El eje se mantuvo, aunque el sistema se dobló.

---

## Semana 7 (2025-12-15 al 2025-12-21)

### Teoría y aprendizaje

* Profundización en **entrelazamiento cuántico**, **medición en la base de Bell** y **protocolo de teleportación**.
* Identificación de fricción conceptual al interpretar:

  * el significado físico de una medición en la base de Bell,
  * la relación entre los diagramas del protocolo y su formulación algebraica.
* Corrección de interpretaciones iniciales incorrectas de la medición

  (de “medir como revelar el estado” hacia **medición como proyección**).
* Trabajo reiterativo de ida y vuelta entre:

  * álgebra lineal,
  * diagramas conceptuales,
  * circuitos en Qiskit,

    con foco en comprensión y no en ejecución mecánica.
* La semana no tuvo como objetivo cerrar la teleportación, sino **detectar la pieza conceptual faltante** necesaria para completarla correctamente.

### Diario y Biblioteca

* Exportado y organizado el **Diario de Bordo – Semana 7** en PDF.
* Exportada y organizada la **Biblioteca – Semana 7** en PDF.
* Contenido alineado con el proceso de revisión conceptual vivido durante la semana.

### Código

* Reorganización del código para agrupar scripts por **conceptos físicos**

  (Bell, Bloch, teleportación) en lugar de por tecnología.
* Ajustes para mantener el código flexible:

  * cambio de estados iniciales,
  * repetición de experimentos,
  * observación de resultados sin forzar conclusiones.

### Estructura del repositorio

* Ajustes menores en la estructura para mejorar la navegación por conceptos.
* Se mantiene la coherencia con la arquitectura definida desde la Semana 5.

### Normalización de archivos

* Consolidación y normalización de los archivos:
  * `Biblioteca_Semana_07.pdf`
  * `Diario_de_Bordo_Semana_07.pdf`
* Semana documentada de forma completa y consistente con las anteriores.

### Notas

* El eje se mantuvo, aunque el sistema se dobló.
* Semana de ajuste conceptual previa al cierre correcto de la teleportación.

---

## Semana 8 (2025-12-22 al 2025-12-28)

### Teoría y aprendizaje

- Profundización intensiva en el **algoritmo de Deutsch–Jozsa**, abordado desde múltiples capas:

  - formulación conceptual,
  - flujo del circuito cuántico,
  - desarrollo algebraico paso a paso,
  - interpretación de la interferencia.
- Comprensión progresiva del rol del **oráculo como caja negra**:

  - transición desde una expectativa de “evaluar valores” hacia la codificación de información en **fases**.
- Identificación explícita de los puntos de fricción conceptual:

  - el significado matemático de la fase `(-1)^{f(x)}`,
  - la recombinación de estados mediante el Hadamard final,
  - la razón por la cual se mide el registro completo y no qubit por qubit.
- Consolidación de la idea central:

  - la computación cuántica **no calcula resultados**, sino que **detecta patrones globales mediante interferencia**.
- Reconocimiento del carácter **frágil** del algoritmo:

  - ausencia de interferencia útil si falta superposición, fase o recombinación.

### Diario y Biblioteca

- Exportado y organizado el **Diario de Bordo – Semana 8** en PDF.
- Exportada y organizada la **Biblioteca – Semana 8** en PDF.
- La documentación refleja:
  - días de avance parcial,
  - días fuera del eje por contexto (Navidad),
  - retorno consciente al proceso sin ruptura del sistema.
- Registro explícito de la confusión como parte del aprendizaje, no como fallo.

### Código

- Implementación y experimentación del algoritmo de **Deutsch–Jozsa en Qiskit**.
- Pruebas con:

  - múltiples qubits de entrada (hasta 28 + 1 auxiliar),
  - distintos tipos de oráculo (constante y balanceado),
  - repetición de experimentos en 1024 shots.
- Verificación empírica del comportamiento teórico:

  - un solo valor distinto basta para que la función sea balanceada.

### Estructura del repositorio

- Se mantiene la estructura conceptual del repositorio introducida en semanas previas.
- El contenido de la semana se integra sin romper la coherencia global del proyecto.
- La organización sigue priorizando **algoritmos y fenómenos físicos** sobre implementaciones aisladas.

### Normalización de archivos

- Consolidación y normalización de los archivos:
  - `Biblioteca_Semana_08.pdf`
  - `Diario_de_Bordo_Semana_08.pdf`
- Semana documentada de forma completa y consistente con la serie histórica del proyecto.

### Notas

- El eje se mantuvo con sesiones más cortas, pero conscientes.
- Semana de consolidación profunda, sin épica, pero con ganancia estructural real.
- Deutsch–Jozsa quedó funcionalmente comprendido, aunque matemáticamente aún abierto, lo cual es consistente con el nivel alcanzado.

---

## Semana 9 (2025-12-29 al 2026-01-04)

### Teoría y aprendizaje

* Consolidación de la **interferencia cuántica** como mecanismo central:
  * distinción clara entre amplitud y probabilidad,
  * rol de la fase relativa frente a la fase global,
  * dependencia de lo observable respecto a la base de medición.
* Uso del **Hadamard como operador de recombinación**:
  * conversión de información de fase en resultados medibles,
  * lectura geométrica del proceso.
* Introducción a los **estados mixtos**:
  * empleo de la matriz densidad,
  * diferencia entre superposición y mezcla estadística,
  * relación con pureza y entropía.
* Primer acercamiento funcional al **algoritmo de Grover**:
  * oráculo como inversor de fase,
  * difusión como reflexión sobre el promedio,
  * comprensión del algoritmo como rotación en un subespacio bidimensional.
* Identificación de límites:
  * número óptimo de iteraciones,
  * efecto de *overshoot* al excederlo.

### Diario y Biblioteca

* Exportado y organizado el **Diario de Bordo – Semana 9** en PDF.
* Exportada y organizada la **Biblioteca – Semana 9** en PDF.
* La documentación registra:

  * momentos de consolidación conceptual profunda,
  * aparición explícita de obstáculos reales (estado mixto vs superposición),
  * cierre de año sin ruptura del eje, con transición consciente entre ciclos.

### Código

* Experimentos mínimos para visualizar **fase, interferencia y cambio de base** mediante circuitos simples (H / HZH).
* Implementación didáctica del **algoritmo de Grover para 2 qubits**:
  * visualización de probabilidades a nivel de vector de estado,
  * verificación explícita de que el oráculo no altera probabilidades,
  * demostración del efecto de amplificación tras la difusión.
* Desarrollo de un **laboratorio conceptual en la esfera de Bloch**:
  * comparación entre estados puros y mixtos,
  * evolución mediante matrices densidad,
  * medición en bases Z y X,
  * análisis de pureza y entropía de von Neumann.
* Exploración controlada de **ruido cuántico** :
  * dephasing como pérdida de coherencia,
  * depolarización y relajación como modelos físicos básicos,
  * observación directa del impacto del ruido sobre la interferencia.

### Estructura del repositorio

* La semana se integra como unidad completa, sin fragmentarse por el cambio de año.
* Se mantiene la coherencia estructural del proyecto Elíejesresce K2.
* Se incorporan nuevas carpetas para reflejar la evolución conceptual del proyecto:
  * `grover/`: avances relacionados con el algoritmo de Grover y la amplificación de amplitud.
  * `consolidacion/`: scripts de transición y cierre conceptual entre interferencia, fase y recombinación.
  * `mixtos/`: estudio de estados mixtos, coherencia y matrices densidad.

### Normalización de archivos

* Consolidación y normalización de los archivos:
  * `Biblioteca_Semana_09.pdf`
  * `Diario_de_Bordo_Semana_09.pdf`
* Organización consistente con la serie histórica del proyecto, preservando continuidad conceptual.

### Notas

* Semana de transición entre ciclos anuales, sostenida sin ruptura del eje.
* Avance menos voluminoso en contenido nuevo, pero **más profundo en comprensión estructural** .
* Interferencia, fase y coherencia quedaron ancladas como conceptos centrales.
* Grover quedó comprendido en su esencia geométrica, con aspectos formales aún abiertos.

---

## Semana 10 (2026-01-05 al 2026-01-11)

### Teoría y aprendizaje

* Profundización formal en el **algoritmo de Grover desde su formulación matemática**:
  * definición explícita de los subespacios ∣**w**⟩ y ∣w⊥⟩.
  * descomposición del estado inicial∣**s**⟩ como combinación lineal de ambos.
  * interpretación del algoritmo como **rotación en un plano bidimensional.**
* Análisis geométrico completo del proceso:
  * introducción del ángulo **θ** asociado a la fracción de estados marcados.
  * relación entre sin²(θ) = M/N y la probabilidad de éxito.
  * comprensión del movimiento periódico y del fenómeno de *overshoot.*
* Formalización de los operadores fundamentales:
  * oráculo como **reflexión de fase** sobre el subespacio de soluciones.
  * difusión como **inversión respecto al estado promedio.**
  * composición del operador de Grover como rotación efectiva por **2θ.**
* Comprensión explícita del **número óptimo de iteraciones**:
  * derivación aproximada **k ≈ (π/4)√(N/M).**
  * aplicación práctica a casos pequeños **(N=8,M=1)**.
  * contraste entre teoría continua y ejecución discreta.

### Diario y Biblioteca

* Exportado y organizado el **Diario de Bordo – Semana 10** en PDF.
* Exportada y organizada la **Biblioteca – Semana 10** en PDF.
* Se inaugura explícitamente la **estructura 2026** dentro del proyecto:
  * separación limpia entre ciclos anuales.
* La documentación registra:
  * días fuera del eje asumidos conscientemente por cierre del ciclo universitario,
  * aparición de una bifurcación simbólica entre lo técnico y lo narrativo.

### Código

* Desarrollo de un **nuevo script avanzado de Grover n-qubits**:

  * soporte para uno o múltiples estados marcados.
  * implementación explícita del oráculo como flip de fase selectivo.
  * difusión generalizada mediante operadores multi-controlados.
* Implementación de una **animación geométrica realista** del algoritmo:

  * visualización de los estados en el plano ∣w⟩,∣w⊥⟩.
  * representación de subpasos reales (init → oracle → diffusion).
  * inclusión de círculo guía y vectores base visibles.

### Textos

* Incorporación de **dos nuevos textos originales** al proyecto:

  * *Dos caminos*, reflexión breve sobre colapso, decisión y bifurcación,
  * *El navegante*, narración simbólica inspirada en el espacio complejo, la rotación y el vacío central.

### Estructura del repositorio

* Se consolida la separación anual:
  * `BIBLIOTECA/2026/`
  * `DIARIO/2026/`
* La Semana 10 se integra como unidad completa dentro del nuevo ciclo.
* El repositorio creativo evoluciona:
  * Cambio de nombre (**FRASES**) a (**TEXTOS**)

### Normalización de archivos

* Consolidación y normalización de los archivos:

  * `Biblioteca_Semana_10.pdf`
  * `Diario_de_Bordo_Semana_10.pdf`
* El año se gestiona a nivel de carpeta, no de archivo.

### Notas

* Semana marcada por **alta exigencia académica externa** y cierre de ciclo universitario.
* Menor volumen de días técnicos, pero **mayor densidad conceptual**.
* Grover deja de ser solo algoritmo y se comprende como **estructura geométrica completa**.
* El eje no se rompe: **se adapta y se traslada**.

---

## Semana 11 (2026-01-12 al 2026-01-18)

### Teoría y aprendizaje

* **Cierre conceptual completo del algoritmo de Grover**:
  * consolidación definitiva del algoritmo como **rotación periódica en un subespacio bidimensional**.
  * comprensión explícita del fenómeno de *overshoot* como consecuencia geométrica inevitable.
* **Introducción formal al algoritmo de Shor desde su núcleo matemático**:
  * transición conceptual de la **factorización directa** a la **búsqueda de periodicidad**.
  * separación clara entre la parte **clásica** (aritmética modular, orden, gcd) y la **cuántica**.
  * identificación del rol central de la transformada de Fourier.
* Estudio progresivo de las transformadas:
  * desarrollo **manual y explícito de la DFT** sobre conjuntos pequeños.
  * comprensión de la DFT como cambio de base global.
* Introducción a la **Transformada Cuántica de Fourier (QFT)**:
  * comparación estructural con la DFT clásica.
  * identificación del papel exclusivo de las **fases relativas**.
  * comprensión de la QFT como **preparación de interferencia**.

### Diario y Biblioteca

* Exportado y organizado el **Diario de Bordo – Semana 11** en PDF.
* Exportada y organizada la **Biblioteca – Semana 11** en PDF.
* La documentación registra:
  * el tránsito explícito **Grover → Shor** como cambio de paradigma.
  * la aparición de la Fourier (DFT/QFT) como **puente conceptual obligatorio**.

### Código

* Desarrollo de un **script mínimo y transparente de Grover**:

  * implementación directa sobre **Statevector**.
  * visualización explícita de amplitudes y probabilidades.
  * demostración práctica del *overshoot* en espacios pequeños.

### Textos

* Incorporación de **un nuevo texto simbólico** al proyecto:

  * *Grover*, poema-metáfora del algoritmo como lluvia,
  * desbordamiento al exceder el número óptimo de iteraciones.

### Estructura del repositorio

* La Semana 11 se integra dentro del ciclo 2026.

### Normalización de archivos

* Consolidación y normalización de los archivos:

  * `Biblioteca_Semana_11.pdf`
  * `Diario_de_Bordo_Semana_11.pdf`

### Notas

* Semana marcada por un **cambio de eje cognitivo** :

  * de la amplificación (Grover),
  * a la extracción de estructura (Shor).
* Se acepta explícitamente la dificultad:

  * la QFT no se “domina” aún.

---

## Semana 12 (2026-01-19 al 2026-01-25)

### Teoría y aprendizaje

* **Desarrollo completo y guiado del algoritmo de Shor mediante un ejemplo concreto**:
  * elección explícita de un número compuesto pequeño \(N = 15\).
  * análisis previo mediante **gcd** como parte clásica del algoritmo.
  * formulación explícita de la función periódica \(f(x) = a^x (mod N)\).
* **Construcción paso a paso de la estructura cuántica de Shor**:
  * definición y justificación del tamaño de ambos registros cuánticos.
  * preparación del primer registro en superposición uniforme.
  * evaluación reversible de la función modular.
* **Comprensión funcional de la QFT dentro de Shor**:
  * interpretación de la QFT como mecanismo de **extracción de periodicidad**.
  * relación entre picos en el dominio de frecuencia y el período oculto \(r\).
  * recuperación de \(r\) mediante fracciones continuas.
* **Verificación clásica posterior**:
  * comprobación de condiciones sobre \(r\).
  * extracción de factores no triviales mediante **gcd**.
  * identificación explícita de casos degenerados y no degenerados.

### Diario y Biblioteca

* Exportado y organizado el **Diario de Bordo – Semana 12** en PDF.
* Exportada y organizada la **Biblioteca – Semana 12** en PDF.
* La documentación registra:
  * días **fuera del eje** por cierre del ciclo académico.
  * un desarrollo largo, manuscrito y razonado del algoritmo de Shor.
  * preguntas conceptuales abiertas sobre:
    * primalidad,
    * tamaño de registros,
    * rol exacto de la QFT.

### Código

* **Sin desarrollo de código nuevo**.
* El trabajo se centró en:
  * razonamiento matemático,
  * trazado manual del algoritmo,
  * comprensión estructural antes de la implementación en Qiskit.

### Estructura del repositorio

* La Semana 12 se integra dentro del ciclo 2026.

### Normalización de archivos

* Consolidación y normalización de los archivos:

  * `Biblioteca_Semana_12.pdf`
  * `Diario_de_Bordo_Semana_12.pdf`

### Notas

* Semana de **baja intensidad operativa**, pero **alta densidad conceptual**.
* El foco se desplazó de la implementación a la **comprensión profunda**.
* Se asume explícitamente:

  * el cansancio,
  * el cierre del ciclo universitario,
  * la necesidad de desacelerar sin romper la continuidad.
* Shor queda **cerrado a nivel conceptual**, pero aún **no implementado**.
* El eje no se pierde: **se sostiene en mínimo**.

---

## Semana 13 (2026-01-26 al 2026-02-01)

### Teoría y aprendizaje

* Se implementó **completamente el algoritmo de Shor en Qiskit** sobre un caso realista:
  * selección explícita del número compuesto \(N = 21\) y base \(a = 2\).
  * incorporación de la **fase clásica inicial** mediante verificación de coprimalidad con `gcd`.
  * identificación explícita del período \(r = 6\) y validación matemática de la periodicidad.
* Se realizó la **transición formal de teoría a implementación computacional**:
  * construcción explícita de las unitarias controladas \(U^{2^j}\) mediante **permutaciones modulares**.
  * adopción de **estimación de fase iterativa (IPE)** con *feed-forward clásico* en lugar de una QFT completa.
  * interpretación directa de los valores medidos \(m/Q\) como aproximaciones racionales del período.
* Se cerró el **ciclo matemático–cuántico–clásico de Shor**:
  * recuperación del período mediante **fracciones continuas**.
  * verificación de condiciones sobre \(r\) (paridad y no degeneración).
  * extracción explícita de los factores no triviales \(3\) y \(7\) mediante `gcd`.
* Se incorporó un **análisis explícito de los límites de simulación clásica**:
  * identificación del crecimiento exponencial del **statevector** como barrera práctica real.
  * comparación entre simulación exacta y métodos aproximados.
  * comprensión de que el cuello de botella es el **hardware clásico**, no el algoritmo.

### Diario y Biblioteca

* Se exportó y organizó el **Diario de Bordo – Semana 13** en formato PDF.
* Se exportó y organizó la **Biblioteca – Semana 13** en formato PDF.
* La documentación registrada incluye:
  * implementación diaria y progresiva del algoritmo de Shor en Qiskit.
  * dificultades técnicas reales relacionadas con:
    * límites de memoria RAM,
    * incompatibilidades con CUDA y GPU,
    * gestión de versiones de dependencias.
  * desarrollo manuscrito completo del caso \(N = 21\), incluyendo:
    * cálculo del tamaño de registros,
    * resultados de simulación,
    * aplicación de fracciones continuas,
    * verificación final de los factores.
  * reflexiones explícitas sobre:
    * la naturaleza híbrida (clásica–cuántica) del algoritmo,
    * la diferencia entre Shor ideal y Shor ruidoso,
    * el impacto emocional del cierre de un campamento.

### Código

* Se desarrolló código intensivo en Qiskit, incluyendo:
  * implementación de **Shor ideal sin ruido** para validación lógica.
  * implementación de **Shor con ruido** para análisis de degradación.
  * pruebas de **escalabilidad con statevector** hasta alcanzar el límite del hardware.
  * uso del método **Matrix Product State (MPS)** para extender el número de qubits simulables.
* Se implementaron explícitamente:
  * circuitos **GHZ** para *stress testing* del simulador.
  * Shor-21 en versiones ideal y ruidosa.
  * variantes ligeras para estudiar comportamiento computacional y consumo de recursos.

### Estructura del repositorio

* Se integró completamente la **Semana 13** dentro del ciclo 2026.
* Se estableció una separación clara entre:
  * scripts ideales,
  * scripts ruidosos,
  * pruebas de límite y escalabilidad.
* Se reorganizó el material experimental y documental para mantener coherencia interna.
* Se actualizó la carpeta **`IDENTIDAD`**:
  * migración completa de los documentos base a **formato PDF**.
  * eliminación de formatos editables.
  * incorporación de un **nuevo documento estratégico** con la expansión del plan:

    * `ELIEJESRESCE_K2_PROYECTO_AUMENTADO.pdf`.

### Normalización de archivos

* Se normalizaron los nombres y formatos de los archivos del proyecto.
* Se consolidaron como referencias oficiales:

  * `Biblioteca_Semana_13.pdf`
  * `Diario_de_Bordo_Semana_13.pdf`
* Se normalizaron los documentos de identidad bajo un criterio único de nombrado:

  * uso consistente de mayúsculas,
  * eliminación de acentos y caracteres especiales,
  * uso de guiones bajos,
  * prefijos `ELIEJESRESCE` / `ELIEJESRESCE_K2`.

### Notas

* Se completa por primera vez el **ciclo íntegro del algoritmo de Shor**:
  * desde la teoría,
  * pasando por la implementación,
  * hasta la validación y el cierre.
* Se deja explícito que:
  * Shor **no es trivialmente escalable** en simulación clásica.
  * el límite encontrado **no es conceptual**, sino computacional.
* El **Campamento 2 queda cerrado**
* El proyecto se expande: **el K2 se eleva** y aparecen nuevos campamentos en el horizonte.

---

## Semana 14 (2026-02-02 al 2026-02-08)

### Teoría y aprendizaje

- Se inició formalmente el **Campamento Anclaje**, orientado en la **consolidación matemática** del ascenso cuántico.
- Se abordó de manera estructurada el **Espacio de Hilbert** como soporte matemático del estado cuántico:
  - comprensión del estado cuántico como **vector normalizado** en un espacio vectorial complejo.
  - identificación clara de que la cuántica **no vive en la esfera de Bloch**, sino en Hilbert.
- Se descompuso el Espacio de Hilbert en sus **capas matemáticas fundamentales**:
  - espacio vectorial complejo,
  - producto interno hermítico,
  - norma inducida,
  - métrica asociada,
  - sucesiones de Cauchy,
  - completitud.
- Se clarificó que:
  - la **norma y la métrica no son axiomas independientes**, sino consecuencias directas del producto interno.
  - la completitud es la condición que garantiza la **existencia de límites físicos**.
- Se estableció la relación formal entre:
  - convergencia,
  - sucesiones de Cauchy,
  - completitud,
  - y la definición rigurosa de Espacio de Hilbert.
- Se cerró la interpretación física:
  - Hilbert como la **estructura matemática mínima sin contradicciones** capaz de soportar evolución, medición y probabilidad cuántica.

### Diario y Biblioteca

- Se exportó y organizó el **Diario de Bordo – Semana 14** en formato PDF.
- Se exportó y organizó la **Biblioteca – Semana 14** en formato PDF.
- La documentación registrada incluye:
  - desarrollo manuscrito completo de la jerarquía de espacios matemáticos.
  - ejercicios explícitos construyendo un Espacio de Hilbert sobre \(C^2\).
  - verificación directa de:

    - hermiticidad del producto interno,
    - definición correcta de norma,
    - métrica inducida,
    - convergencia y condición de Cauchy.

### Código

- No se desarrolló código nuevo esta semana de forma deliberada.
- La semana se dedicó a:

  - **anclaje conceptual**,
  - revisión matemática,
  - consolidación de fundamentos previos al siguiente bloque computacional.

### Estructura del repositorio

- Se integró completamente la **Semana 14** dentro del ciclo 2026.
- Se mantuvo la coherencia entre:
  - Diario,
  - Biblioteca,
  - estructura global del proyecto.
- No se realizaron cambios estructurales mayores.

### Normalización de archivos

- Se consolidaron como referencias oficiales:
  - `Biblioteca_Semana_14.pdf`
  - `Diario_de_Bordo_Semana_14.pdf`
- Se mantuvo el criterio único de nombrado:
  - uso consistente de mayúsculas,
  - guiones bajos,
  - ausencia de acentos y caracteres especiales.

### Notas

- Se deja explícito que:
  - sin Espacio de Hilbert no existe cuántica coherente,
  - sin completitud no existe evolución física bien definida.
- El **Campamento Anclaje queda formalmente iniciado**.

---

## Semana 15 (2026-02-09 al 2026-02-15)

### Teoría y aprendizaje

- Se realizó lectura profunda y estructural del artículo:

  “Distributed quantum computing across an optical network link”, D. Main, P. Drmota, D. P. Nadlinger, E. M. Ainley, A. Agrawal, B. C. Nichol, R. Srinivas, G. Araneda y D. M. Lucas.
- Se identificó que el artículo presenta:

  - Demostración experimental de computación cuántica distribuida funcional.
  - Implementación de entrelazamiento remoto “heralded” entre módulos de iones atrapados.
  - Teleportación de compuertas cuánticas (incluyendo una compuerta CZ remota).
  - Ejecución distribuida del algoritmo de Grover.
  - Arquitectura modular conectada mediante enlace óptico.
- Se estudió y formalizó conceptualmente:

  - Heralded Remote Entanglement.
  - Fault-Tolerant Quantum Computing.
  - Quantum Repeaters.
  - Entanglement Purification.
  - Ion Traps y Paul Traps.
  - All-to-all connectivity.
  - Vacuum and Cryogenic Systems.
  - Diamond Color Centers.
  - Superconducting Qubits.
  - Neutral Atoms.
  - Wavelength Conversion.
  - Trapped Ion Quantum Processing Modules.
  - Zeeman States.
  - Pauli Operators.
  - Non-local Gates.
- Se comprendió que el artículo integra simultáneamente:

  - Física experimental (trampas de iones, estados Zeeman, ultra alto vacío).
  - Óptica cuántica (interferencia de fotones, conversión de longitud de onda).
  - Teoría de información cuántica (entanglement swapping, compuertas no locales).
  - Arquitectura modular escalable.
- Se ejecutó un ejercicio estructural formal en ℂ²:

  - Identificación del estado cuántico como vector normalizado.
  - Interpretación geométrica de la medición como proyección.
  - Uso explícito de operadores proyectores.
  - Aplicación directa de la regla de Born.
- Se formalizó que:

  - La probabilidad es consecuencia del producto interno en el Espacio de Hilbert.
  - La medición no es una compuerta unitaria, sino una operación asociada a operadores hermíticos.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_15.pdf`
  - `Biblioteca_Semana_15.pdf`
- El Diario documenta:

  - Lectura profunda del artículo.
  - Extracción sistemática de dudas.
  - Resumen conceptual sin traducción.
  - Resolución estructural de preguntas.
  - Ejercicio formal en espacio de Hilbert.
  - Creación del “Codex” como sistema de términos técnicos.
- La Biblioteca incluye:

  - Desarrollo manuscrito de cada término técnico extraído del artículo.
  - Formalización conceptual de protocolos de entrelazamiento remoto.
  - Explicación estructurada de plataformas físicas cuánticas.
  - Ejercicio matemático explícito sobre medición en base computacional.

### Código

- No se desarrolló nuevo código.

### Estructura del repositorio

- No se realizaron modificaciones estructurales mayores.

### Normalización de archivos

- Se consolidaron como referencias oficiales:

  - `Biblioteca_Semana_15.pdf`
  - `Diario_de_Bordo_Semana_15.pdf`

### Notas

- Se crea formalmente el **Codex** como técnica de acumulación de vocabulario técnico.

---

## Semana 16 (2026-02-16 al 2026-02-22)

### Teoría y aprendizaje

- Se consolidó geométricamente la estructura del espacio de estados de un qubit:

  - Identificación formal de ℋ = ℂ² como espacio de Hilbert.
  - Interpretación de ℂ² como ℝ⁴.
  - Restricción a la 3-esfera S³ mediante normalización ‖ψ‖ = 1.
  - Eliminación de la fase global como redundancia física.
  - Identificación del espacio físico como S³ / S¹ ≅ CP¹.
  - Equivalencia geométrica CP¹ ≅ S² (esfera de Bloch).
- Se formalizó estructuralmente:

  - Diferencia precisa entre fase global y fase relativa.
  - Interpretación geométrica de la órbita de fase como fibra S¹.
  - Interpretación geométrica del cociente por fase global (S³/S¹).
  - Reducción de grados de libertad: 4 → 3 → 2.
  - Distinción entre espacio matemático (Hilbert) y espacio físico (proyectivo).
- Se integró lectura de Shankar como referencia formal:

  - Comprensión de la mecánica cuántica como extensión estructural de la clásica.

---

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_16.pdf`
  - `Biblioteca_Semana_16.pdf`
- El Diario documenta:

  - Proceso de comprensión geométrica del qubit.
  - Discusión sobre Bloch vs Hilbert.
  - Clarificación profunda de fase global.
  - Consolidación conceptual antes de avanzar a nuevos algoritmos.
- La Biblioteca incluye:

  - Desarrollo manuscrito del paso ℂ² → S³ → CP¹ → S².
  - Explicación formal de reducción por fase global.
  - Síntesis estructural del espacio proyectivo complejo.

---

### Código

- Se desarrolló una animación conceptual en Python que visualiza:

  - ℂ² como ℝ⁴ (vista parcial).
  - Normalización hacia S³.
  - Proyección estereográfica S³ → ℝ³.
  - Órbita de fase global.
  - Colapso geométrico mediante el mapa de Hopf hacia la esfera de Bloch.

---

### Codex

- Se crea formalmente la estructura del **Codex** dentro del repositorio.
- Se define la lógica de crecimiento semanal (no acumulativa).
- Se integra el archivo correspondiente a la semana:

  - `Codex_Semana_16.pdf`
- Se consolida el Codex como sistema oficial de acumulación de vocabulario técnico del proyecto.

---

### Estructura del repositorio

- Se agregó la carpeta dedicada a `codex/` siguiendo la lógica semanal ya utilizada en Diario y Biblioteca.

---

### Normalización de archivos

- Se consolidaron como referencias oficiales:

  - `Biblioteca_Semana_16.pdf`
  - `Diario_de_Bordo_Semana_16.pdf`
  - `Codex_Semana_16.pdf`

---

### Notas

- El qubit físico vive en el espacio proyectivo complejo.

---

## Semana 17 (2026-02-23 al 2026-03-01)

### Teoría y aprendizaje

- Se consolidó formalmente la estructura operativa del espacio de Hilbert:

  - Definición rigurosa de espacio de Hilbert como espacio vectorial complejo completo con producto interno.
  - Formalización de la norma inducida por el producto interno.
  - Interpretación de la completitud mediante sucesiones de Cauchy.
  - Clarificación estructural de la ortogonalidad: ⟨φ|ψ⟩ = 0.
  - Interpretación física de estados ortogonales como resultados mutuamente excluyentes.
- Se formalizó la teoría de operadores cuánticos:

  - Definición general de operador lineal A : ℋ → ℋ.
  - Distinción estructural entre operadores hermíticos y unitarios.
  - Condición de hermiticidad: A† = A.
  - Condición de unitariedad: U†U = I.
  - Interpretación física: evolución reversible vs medición.
- Se introdujo formalmente la estructura espectral:

  - Ecuación de eigenvalor: A|ψ⟩ = λ|ψ⟩.
  - Interpretación física de eigenvalores como resultados posibles de medición.
  - Interpretación de eigenvectores como estados estables frente al observable.
- Se consolidó la teoría de proyectores:

  - Definición de operador proyector P = |a⟩⟨a|.
  - Idempotencia: P² = P.
  - Modelado matemático del colapso como proyección sobre subespacio propio.
- Se formalizó la teoría de conmutadores:

  - Definición: [A,B] = AB − BA.
  - Caso [A,B] = 0 → existencia de base común de eigenvectores.
  - Caso [A,B] ≠ 0 → incompatibilidad de observables.
  - Conexión estructural con el principio de incertidumbre.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_17.pdf`
  - `Biblioteca_Semana_17.pdf`
- El Diario documenta:

  - Consolidación conceptual del espacio de Hilbert.
  - Incremento en el nivel de abstracción matemática.
  - Registro de días fuera del eje por proceso de mudanza.
- La Biblioteca incluye:

  - Desarrollo manuscrito de operadores hermíticos, unitarios y proyectores.
  - Formalización de conmutadores y compatibilidad de observables.
  - Síntesis estructural de eigenvalores y eigenvectores.
  - Consolidación matemática del Campamento Anclaje.

### Código

- No se desarrollaron nuevos algoritmos.

### Estructura del repositorio

- Se mantiene la organización modular

### Normalización de archivos

- Se consolidaron como referencias oficiales:

  - `Biblioteca_Semana_17.pdf`
  - `Diario_de_Bordo_Semana_17.pdf`

### Notas

- Avanzar con la mente dispersa es complicado.

---

## Semana 18 (2026-03-02 al 2026-03-08)

### Teoría y aprendizaje

- Se consolidó algebraica y geométricamente la estructura espectral de operadores hermíticos:

  - Construcción de eigenvalores a partir del polinomio característico.
  - Construcción de eigenvectores asociados a cada eigenvalor.
  - Normalización de eigenvectores para formar estados físicos válidos.
  - Construcción de proyectores espectrales a partir de eigenvectores normalizados.
  - Verificación de propiedades de los proyectores: ortogonalidad, idempotencia y resolución de la identidad.
  - Reconstrucción de una matriz a partir de su descomposición espectral `A = Σ a Pₐ`.
- Se formalizó estructuralmente la interpretación de la medición cuántica:

  - Comprensión de la medición como proyección sobre subespacios propios de un observable.
  - Descomposición de un estado en componentes asociadas a distintos subespacios propios.
  - Cálculo de probabilidades de medición mediante proyectores.
  - Comprensión de que los posibles resultados de medición son los eigenvalores del observable.
  - Clarificación de que un observable se representa mediante un operador hermítico.
- Se consolidó la distinción conceptual entre tipos de operadores cuánticos:

  - Diferencia entre observable y compuerta cuántica.
  - Comprensión de que las compuertas representan evolución unitaria.
  - Comprensión de que la medición no es una compuerta, sino una operación de naturaleza distinta.
  - Revisión del papel de los conmutadores y de la base de eigenvectores compartida.
- Se reforzó la intuición del marco matemático del espacio de Hilbert:

  - Operadores como transformaciones lineales en el espacio de Hilbert.
  - Relación entre operadores, eigenvalores, eigenvectores y medición.
  - Consolidación de una intuición geométrica sobre proyección, descomposición y certeza en la medición.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_18.pdf`
  - `Biblioteca_Semana_18.pdf`
- El Diario documenta:

  - Construcción de eigenvalores, eigenvectores y proyectores espectrales.
  - Trabajo con una matriz no normalizada para obtener su estructura espectral.
  - Comprensión de la descomposición de estados en subespacios propios.
  - Diferenciación entre observable y compuerta.
  - Un punto de quiebre conceptual claro en el Día 88.
  - Un día fuera de eje en el Día 89.
  - Repaso integrador de operadores, espacio de Hilbert, conmutadores, eigenvalores y eigenvectores en el Día 90.
- La Biblioteca incluye:

  - Desarrollo manuscrito del caso diagonal y del caso no normalizado.
  - Construcción paso a paso de eigenvalores y eigenvectores.
  - Normalización explícita de vectores propios.
  - Construcción y verificación de proyectores espectrales.
  - Reconstrucción matricial mediante descomposición espectral.
  - Mini-reto de descomposición de un estado arbitrario con cálculo de probabilidades.
  - Repaso conceptual de operadores, observables, proyectores y conmutadores.

### Código

- No se desarrolló código nuevo esta semana.

### Codex

Se integró el archivo correspondiente a la semana:

- `Codex_Semana_18.pdf`

Se añadieron y consolidaron entradas fundamentales del marco matemático y físico actual:

- Descomposición espectral.
- Polinomio característico.
- Observable.

El Codex de esta semana acompaña directamente la transición desde la geometría del qubit hacia la estructura formal de medición y observables.

### Estructura del repositorio

No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

- Se consolidaron como referencias oficiales:

  - `Biblioteca_Semana_18.pdf`
  - `Diario_de_Bordo_Semana_18.pdf`
  - `Codex_Semana_18.pdf`

### Notas

- La medición cuántica quedó comprendida como una proyección sobre subespacios propios.

---

## Semana 19 (2026-03-09 al 2026-03-15)

### Teoría y aprendizaje

- Se consolidó el cierre conceptual del **Campamento Anclaje**, integrando la comprensión formal de varios pilares de la mecánica cuántica aplicados a computación cuántica.

  - El estado cuántico se comprendió formalmente como un vector normalizado dentro de un **espacio de Hilbert complejo**.
  - Se reforzó la interpretación de la **medición como proyección** sobre una base de eigenvectores.
  - Se distinguió claramente entre **operadores unitarios** (evolución del sistema) y **operadores hermíticos** (observables).
  - Se consolidó la interpretación física de **eigenvalores y eigenvectores** como resultados posibles de medición y estados estables frente a un observable.
  - Se reforzó la intuición de la **Transformada Cuántica de Fourier (QFT)** como un cambio de base que revela periodicidad.
- Durante la semana se produjo una conexión conceptual importante relacionada con la medición en diferentes bases:

  - Medición en **Z** distingue poblaciones entre \|0⟩ y \|1⟩.
  - Medición en **X** revela la coherencia del estado.
  - Medición en **Y** revela información sobre la fase relativa.
- Esta comprensión llevó a reconocer la relación con **tomografía cuántica**, donde un estado no puede caracterizarse completamente con una sola base de medición.
- También se reafirmó la diferencia entre la representación física del sistema cuántico y su simulación clásica:

  - La simulación clásica requiere almacenar explícitamente el **statevector completo**, cuyo tamaño crece exponencialmente con el número de qubits.
  - El sistema físico cuántico codifica información en fases, interferencias y correlaciones entre estados.
- El progreso conceptual fue sólido, aunque se registró un día de baja energía que afectó momentáneamente el ritmo de estudio.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario de Bordo - Semana 19.pdf`
  - `Biblioteca - Semana 19.pdf`
- El **Diario de Bordo** documentó:

  - un inicio irregular con un día fuera de eje
  - la creación y ajuste de scripts de simulación
  - el traslado del entorno de trabajo hacia **WSL**
  - conexiones conceptuales surgidas durante la implementación de código
  - el cierre formal del **Campamento Anclaje**
  - un inicio simbólico del **Campamento 3**
- La **Biblioteca** incluyó:

  - preguntas y respuestas sobre operadores y bases de eigenvectores
  - reflexiones sobre conmutadores y observables incompatibles
  - la relación entre medición y proyección en el espacio de Hilbert
  - una síntesis de las cinco misiones del Campamento Anclaje
  - notas sobre medición en distintas bases y su relación con tomografía cuántica

### Código

Durante la semana se trabajó en dos scripts principales.

**1. Prueba de límite de simulación de statevector**

- Se reutilizó una idea previa para probar una lógica distinta de ejecución.
- El script genera estados tipo **GHZ** aplicando una compuerta Hadamard inicial seguida de una cadena de compuertas CNOT.
- El simulador se fuerza a construir y devolver el **statevector completo**, permitiendo observar:

  - tiempo de ejecución
  - dimensión del vector
  - límite práctico de simulación clásica
- Este script funcionó como demostración empírica del **crecimiento exponencial del espacio de estados** en sistemas cuánticos simulados clásicamente.

**2. Simulación visual de operadores cuánticos sobre un qubit**

- Se desarrolló una simulación animada del efecto de un operador sobre un qubit en la **esfera de Bloch**.
- El programa permite seleccionar:

  - estado inicial
  - operador aplicado
  - base de medición
- La visualización incluye simultáneamente:

  - trayectoria del estado en la esfera de Bloch
  - vector de estado actual
  - probabilidades de medición en tiempo real
  - representación explícita del estado \|ψ⟩
  - coordenadas de Bloch
  - eigenvalores del operador aplicado
- Este código integró en una sola simulación varios conceptos clave del Campamento Anclaje:

  - espacio de Hilbert
  - evolución mediante operadores unitarios
  - medición en diferentes bases
  - interpretación geométrica del estado cuántico

### Codex

- No se añadió un archivo nuevo de Codex durante esta semana.

### Estructura del repositorio

- Se inició la transición del entorno de trabajo hacia **Linux mediante WSL**.
- Se revisó el comportamiento de scripts de simulación en el nuevo entorno.
- No se realizaron cambios estructurales importantes en la organización del repositorio.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_19.pdf`
- `Diario_de_Bordo_Semana_19.pdf`

### Notas

* Esta semana marcó el **cierre del Campamento Anclaje**, donde el qubit dejó de entenderse solo desde la intuición geométrica de la esfera de Bloch y pasó a interpretarse como un objeto matemático formal dentro del espacio de Hilbert.
* La comprensión de medición en distintas bases permitió conectar la geometría del estado con la reconstrucción de información cuántica, consolidando una visión más completa de la relación entre operadores, evolución y observables.

---

## Semana 20 (2026-03-16 al 2026-03-22)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado debido a una alta carga logística asociada al viaje a Venezuela.
- Se realizó una introducción inicial al Postulado 1 de la mecánica cuántica, contrastando:

  - Mecánica clásica: estado definido por posición y momento (x(t), p(t))
  - Mecánica cuántica: estado representado como vector |ψ(t)⟩ en un espacio de Hilbert
- Se estableció la diferencia conceptual clave:

  - En clásica: estado completamente determinado
  - En cuántica: estado definido por amplitudes complejas que generan probabilidades
- Se realizó un repaso breve del Postulado 1 para mantener continuidad en el proceso.
- Dificultades:

  - Interrupción del ritmo por actividades externas
  - Falta de tiempo para profundizar en desarrollo matemático

---

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_20.pdf`
  - `Biblioteca_Semana_20.pdf`
- El Diario documenta:

  - Múltiples días fuera de eje por logística de viaje
  - Inicio del Campamento 3
  - Introducción conceptual al Postulado 1
  - Reflexión sobre el cambio de entorno (viaje inminente)
- La Biblioteca incluye:

  - Comparación directa entre mecánica clásica y cuántica
  - Definición del estado clásico como punto en espacio de fases
  - Definición del estado cuántico como vector en espacio de Hilbert

  Ejemplo:

  - Definición clásica: x(t), p(t)
  - Definición cuántica: |ψ(t)⟩
- La biblioteca fue principalmente conceptual y de introducción, sin desarrollo matemático profundo.

---

### Código

- No se desarrolló código nuevo esta semana.

---

### Codex

- No se añadieron nuevas entradas al Codex esta semana.

---

### Estructura del repositorio

- Se añadieron los documentos correspondientes a la Semana 20:
  - Diario
  - Biblioteca
- No se realizaron cambios estructurales adicionales.

---

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_20.pdf`
- `Diario_de_Bordo_Semana_20.pdf`

### Notas

Semana marcada por una transición física importante más que por avance teórico. A pesar de la interrupción del ritmo, se mantuvo el vínculo con el sistema mediante acciones mínimas, iniciando el Campamento 3 y estableciendo la base conceptual del Postulado 1.

El sistema no se rompió: se adaptó.

---

## Semana 21 (2026-03-23 al 2026-03-29)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado y se centró en mantener la continuidad del sistema en condiciones de viaje.

  - Se realizó un repaso breve del Postulado 1, reforzando la idea del estado cuántico como vector complejo.
  - Se reinterpretó la situación personal como un sistema cuántico, incorporando:
    - superposición de estados (avance, bloqueo, flujo)
    - ruido y decoherencia (estrés, incertidumbre, cansancio)
    - operador de acción mínima como mecanismo de control del sistema
  - Se conectó la medición con la toma de decisiones y probabilidad en contextos reales.

### Diario y Biblioteca

- El Diario documenta:

  - inicio de un nuevo Diario de Bordo tras alcanzar 100 páginas
  - inicio del viaje hacia Venezuela
  - múltiples días fuera de eje debido a problemas logísticos
  - reinterpretación del proceso como sistema cuántico
  - continuidad del vínculo a pesar del contexto adverso
- La Biblioteca incluye:

  - repaso conceptual del Postulado 1
  - construcción de un modelo cuántico abstracto aplicado al estado personal
  - introducción de:

    - superposición no normalizada
    - operador de acción consciente
    - decoherencia como ruido del entorno
  - análisis de una noticia sobre computación cuántica y criptografía (Google, 2026)

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- Se escribió un nuevo texto:

  - `Traslado.md`
- El texto introduce una metáfora temporal del cambio de etapa, conectando memoria, evolución y dirección del sistema personal

### Codex

- No se añadieron nuevas entradas al Codex esta semana.

### Estructura del repositorio

- Se añadieron los documentos semanales correspondientes.
- No se realizaron cambios estructurales relevantes.

### Normalización de archivos

- Se consolidaron como referencias oficiales:

  - `Biblioteca_Semana_21.pdf`
  - `Diario_de_Bordo_Semana_21.pdf`
- No se generó archivo de Codex para esta semana.

### Notas

- La semana no representó un avance técnico fuerte, pero sí una validación del sistema: incluso en condiciones de ruido, el eje no se pierde, se adapta.
- Se consolidó una idea clave: el sistema no exige perfección, exige continuidad.

---

## Semana 22 (2026-03-30 al 2026-04-05)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado debido al proceso de mudanza y cambio de entorno.
- Se realizó una revisión conceptual de mecánica clásica a partir del libro "Mecánica General - I. Rubio", identificándola como base para la ecuación de Schrödinger.
- Se retomó el eje del proyecto mediante una revisión de los postulados de la mecánica cuántica según Shankar:

  - Estado como vector en espacio de Hilbert
  - Evolución mediante operadores unitarios
  - Medición como colapso a eigenestados
  - Evolución gobernada por la ecuación de Schrödinger
- Se consolidó una conexión clave:

  - Los primeros tres postulados describen el sistema en un instante
  - El cuarto describe su evolución temporal
- Se identificó una dificultad importante:

  - Falta de representación explícita de la ecuación de Schrödinger dentro del marco práctico

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_22.pdf`
  - `Biblioteca_Semana_22.pdf`
- El Diario documenta:

  - varios días fuera de eje por mudanza
  - mantenimiento del vínculo con el proyecto
  - reconexión progresiva con los postulados
  - transición hacia implementación en código
- La Biblioteca incluye:

  - revisión de mecánica clásica como base de la cuántica
  - formulación simplificada de los 4 postulados
  - conexión entre teoría y Qiskit
  - introducción clara al concepto de fase y cambio de base

### Código

- Se desarrolló un script en Qiskit para explorar los postulados cuánticos con un qubit:

  - Preparación de estados:

    - |+> con Hadamard
    - |1> con X
    - estado con fase compleja
  - Análisis del estado:

    - uso de `Statevector`
    - visualización de amplitudes y probabilidades
  - Evolución unitaria:

    - compuertas H y X como operadores unitarios
  - Medición:

    - simulación en base Z con `measure`
    - medición en base X mediante cambio de base (H + measure)
  - Interpretación física integrada:

    - el estado es un vector complejo previo a medición
    - la fase relativa no se ve en Z pero sí en cambios de base
    - las compuertas representan evolución unitaria

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- Se definió un cambio estructural importante:

  - El Codex deja de ser un archivo PDF semanal
  - Pasa a ser un archivo Markdown acumulativo
- Se integrará progresivamente el contenido del cuaderno físico al repositorio
- Se revisó el documento base del Codex

  - Estructura:

    - Término — Traducción
    - Definición clara
    - Fórmula (si aplica)
  - Entre parte del contenido incluye:

    - Qubit
    - Estadovector
    - Producto interno
    - Base computacional
    - Fase global y relativa
    - Operadores unitarios
    - Descomposición espectral

### Estructura del repositorio

- Se definió una nueva política para el Codex:

  - Archivo único acumulativo (`codex.md`)
  - Eliminación del formato semanal en PDF

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_22.pdf`
  - `Diario_de_Bordo_Semana_22.pdf`
  - Codex migrará a `.md` en lugar de PDF

### Notas

Semana de transición donde el foco no fue avanzar en contenido sino sostener el sistema. El punto clave fue la reconexión con los postulados y su traducción a código, logrando ver por primera vez el sistema cuántico como una estructura completa: estado, evolución y medición integrados en una misma representación operativa.

---

## Semana 23 (2026-04-06 al 2026-04-12)

### Teoría y aprendizaje

- La semana comenzó con un repaso de los postulados cuánticos desde reconstrucción interna, sin depender de libros ni apuntes externos.

  - Se consolidó la idea de que el estado cuántico se representa como vector normalizado en un espacio de Hilbert complejo.
  - Se reforzó la evolución unitaria como transformación central del sistema.
  - Se aclaró el papel de la medición como colapso hacia eigenestados siguiendo la regla de Born.
  - Se afianzó la relación entre compuertas cuánticas y la ecuación de Schrödinger como evolución unitaria discreta.
- Se revisó y refactorizó el script de postulados para que reflejara de forma explícita cada uno de los postulados dentro de un único experimento con un qubit.
- El avance conceptual más importante de la semana fue el paso desde la comprensión de los postulados hacia su materialización como arquitectura funcional, mediante el diseño y consolidación de un sistema cuántico distribuido simulado.
- También se identificó con claridad una limitación estructural importante:

  - el sistema todavía no es completamente distribuido, ya que mantiene un orquestador central que procesa y coordina el protocolo.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_23.pdf`
  - `Biblioteca_Semana_23.pdf`
- El Diario documenta:

  - repaso de postulados desde reconstrucción interna
  - refactorización del código de postulados
  - nacimiento del proyecto de sistema cuántico distribuido
  - paso a una versión tangible con nodos funcionando por red
  - mejora posterior hacia una versión 2 con nuevas características
  - reflexión crítica sobre la diferencia entre un sistema distribuido simulado y uno realmente distribuido
- La Biblioteca incluye:

  - formulación compacta de los cuatro postulados
  - reinterpretación del script para recorrer explícitamente cada postulado
  - preparación del estado \(|psi> = (|0> + i|1>) / sqrt{2}) usando compuertas H y S
  - diseño conceptual completo del sistema de computación cuántica distribuida
  - arquitectura, stack, flujo del sistema y fases del protocolo
  - documentación de la versión 1 y de la versión 2 del sistema
  - mejoras introducidas en la versión 2 y resultados obtenidos

### Código

- Se trabajó sobre un script de Qiskit que muestra de forma explícita los cuatro postulados cuánticos con un solo qubit.

  - Se representa el estado como vector normalizado.
  - Se prepara el estado mediante evolución unitaria.
  - Se conecta la evolución con la ecuación de Schrödinger.
  - Se compara la medición teórica con la observada en base Z y base X.
- Se desarrolló y consolidó un sistema cuántico distribuido simulado como subproyecto independiente del repositorio principal.
- El sistema evolucionó en dos etapas:

  - **Versión 1**

    - nodos conectados por red
    - enlace básico entre ambos nodos
    - primeras pruebas funcionales del protocolo
    - presencia de errores de diseño y carencia de funcionalidades
  - **Versión 2**

    - generación de enlace con heraldo
    - canal de transmisión con ruido dependiente de distancia
    - estados de Bell variables por enlace
    - medición local en cada nodo
    - protocolo de revelación
    - reconstrucción global de correlación
    - paneles de información en tiempo real
    - actualización del estado de ambos nodos
    - integración de Qiskit para el cálculo cuántico del sistema
    - corrección de bugs detectados en la versión anterior
- Durante el cierre semanal, el sistema fue organizado como repositorio independiente, con README, requirements, LICENSE, documentación visual y relación explícita con el proyecto principal Elíejesresce K2.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se agregaron términos nuevos esta semana.

### Estructura del repositorio

- Se mantuvo el repositorio principal como núcleo conceptual y documental del proyecto.
- Se abrió un repositorio satélite para el sistema cuántico distribuido simulado, como expansión práctica del Campamento 3.
- Se volvió necesario añadir en el repositorio principal una referencia explícita a este nuevo subproyecto derivado en el README.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_23.pdf`
  - `Diario_de_Bordo_Semana_23.pdf`
- El código de postulados quedó como referencia explícita del trabajo teórico-práctico de la semana.
- El prototipo DQC quedó formalizado además como repositorio independiente documentado.

### Notas

Esta semana marcó un punto de inflexión real en Elíejesresce K2: los postulados dejaron de ser solo un objeto de estudio y empezaron a operar como criterio de construcción. El avance más fuerte no fue únicamente entender mejor la mecánica cuántica, sino transformarla en arquitectura, protocolo, interfaz y sistema ejecutable. La pregunta ya no fue solo qué hace un estado cuántico, sino cómo se organiza un sistema que intente comportarse como uno.

---

## Semana 24 (2026-04-13 al 2026-04-19)

### Teoría y aprendizaje

- Se desarrolló la comprensión fundamental de la ecuación de Schrödinger como ley de evolución del estado cuántico.

  - Se identificó el papel del Hamiltoniano como generador de la dinámica del sistema.
  - Se interpretó la ecuación como una relación entre cómo cambia el estado y qué lo hace cambiar.
  - Se comprendió que la evolución del estado puede interpretarse como una rotación en el espacio de Hilbert.
  - Se reforzó la idea de que la mecánica cuántica describe evolución, no resultados directos.
- Se resolvió explícitamente un sistema basado en la ecuación de Schrödinger.

  - Se partió de un Hamiltoniano tipo X.
  - Se desacopló el sistema mediante derivadas de segundo orden.
  - Se obtuvo una solución oscilatoria en términos de funciones seno y coseno.
  - Se conectaron las amplitudes con probabilidades medibles.
- Se consolidó la relación:

  - Hamiltoniano → evolución
  - Evolución → operador unitario
  - Operador unitario → compuertas cuánticas
- Se comprendió que las compuertas no son fundamentales, sino manifestaciones de la evolución.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_24.pdf`
  - `Biblioteca_Semana_24.pdf`
- El Diario documenta:

  - días con dificultad física (gripe) que afectaron el ritmo
  - continuidad del proyecto a pesar de condiciones adversas
  - reflexiones sobre la constancia ("Siempre se vuelve")
  - transición hacia una comprensión más profunda del sistema cuántico como evolución
- La Biblioteca incluye:

  - desarrollo completo de la ecuación de Schrödinger
  - descomposición conceptual de sus términos
  - resolución matemática paso a paso del sistema
  - interpretación física de la solución obtenida

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- Se escribió un nuevo texto titulado "Volver".

  - Reflexiona sobre la constancia del proyecto en el tiempo.
  - Refuerza la idea de que el vínculo con el proceso se mantiene incluso en días difíciles.

### Codex

- Se añadieron nuevas entradas relacionadas con:

  - Hamiltoniano
  - Ecuación de Schrödinger

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_24.pdf`
  - `Diario_de_Bordo_Semana_24.pdf`

### Notas

La semana marca un punto de inflexión conceptual: la mecánica cuántica deja de verse como una colección de operaciones y pasa a entenderse como una teoría de evolución gobernada por el Hamiltoniano. La ecuación de Schrödinger se internaliza no solo como fórmula, sino como mecanismo dinámico que da origen a todo el comportamiento del sistema.

---

## Semana 25 (2026-04-20 al 2026-04-26)

### Teoría y aprendizaje

- La semana se centró en consolidar la relación entre evolución cuántica y medición.

  - Se reforzó la interpretación de la ecuación de Schrödinger como generadora de evolución del sistema.
  - Se comprendió que el Hamiltoniano define completamente dicha evolución.
  - Se integró la idea de que las compuertas cuánticas representan evoluciones específicas del sistema.
  - Se estudió la medición como un proceso físico que rompe la evolución continua.
  - Se profundizó en el concepto de decoherencia como pérdida de información de fase.
  - Se estableció la diferencia entre fase controlada (coherencia) y fase aleatoria (decoherencia).
  - Se conectó la decoherencia con la aparición de comportamiento clásico.
- Dificultades:

  - Persisten dudas sobre la conexión exacta entre el colapso teórico y el proceso físico real de medición.
  - La interpretación de sistemas con decoherencia aún resulta abstracta.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_25.pdf`
  - `Biblioteca_Semana_25.pdf`
- El Diario documenta:

  - días fuera de eje debido a diligencias y cansancio
  - integración de Anki como herramienta de estudio
  - consolidación de ideas clave sobre medición y coherencia
  - dificultades conceptuales en decoherencia
  - preguntas abiertas sobre qubits lógicos y variaciones del sistema
- La Biblioteca incluye:

  - desarrollo conceptual del Hamiltoniano total
  - síntesis de la ecuación de Schrödinger como motor de evolución
  - explicación de la medición como proyección
  - descripción del proceso físico de medición: interacción, entrelazamiento, amplificación y decoherencia
  - esquema conceptual de coherencia vs decoherencia

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

Conceptos añadidos:

- Coherence
- Decoherence

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_25.pdf`
- `Diario_de_Bordo_Semana_25.pdf`

### Notas

La semana marca una transición importante desde entender la mecánica cuántica como un sistema de resultados hacia comprenderla como un proceso de evolución. La introducción de la decoherencia permite explicar la pérdida de comportamiento cuántico, aunque aún queda por cerrar la brecha conceptual entre el modelo teórico del colapso y su realización física.

---

## Semana 26 (2026-04-27 al 2026-05-03)

### Teoría y aprendizaje

- La semana se centró en la consolidación de los postulados de la mecánica cuántica y su conexión con el algoritmo de Shor.

  - Se reforzó la comprensión del estado cuántico como vector en un espacio de Hilbert complejo.
  - Se consolidó la evolución unitaria como consecuencia de la ecuación de Schrödinger.
  - Se profundizó en la medición como proyección sobre eigenvectores y su interpretación mediante la regla de Born.
  - Se comprendió el límite fundamental de la información a través de observables no conmutativos.
  - Se estableció la conexión entre la periodicidad en Shor y su codificación en la fase del sistema.
  - Se integró la necesidad de múltiples mediciones en diferentes bases (tomografía cuántica).
- La semana tuvo un fuerte enfoque en integrar conceptos ya vistos, más que en introducir nuevos.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_26.pdf`
  - `Biblioteca_Semana_26.pdf`
- El Diario documenta:

  - continuidad del eje mediante resolución de tarjetas en Anki
  - días con carga académica que limitaron profundidad
  - cierre de la misión 0 con repaso final
  - inicio de conexión entre postulados y Shor
  - un día fuera de eje
- La Biblioteca incluye:

  - resumen estructurado de los postulados cuánticos
  - relación entre coherencia, interferencia y decoherencia
  - interpretación física y matemática de la medición
  - introducción conceptual a Shor desde los postulados
  - desarrollo de la función periódica f(x) = a^x mod N y su codificación en fase

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- Se integraron nuevos conceptos:

  - Observables no conmutativos

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:
  - `Biblioteca_Semana_26.pdf`
  - `Diario_de_Bordo_Semana_26.pdf`

### Notas

Esta semana marca un punto de transición importante: los postulados dejan de ser teoría aislada y comienzan a funcionar como marco real para entender algoritmos como Shor. No se avanzó en volumen, pero sí en profundidad.

---

## Semana 27 (2026-05-04 al 2026-05-10)

### Teoría y aprendizaje

- La semana se centró principalmente en reconstruir conceptualmente el algoritmo de Shor a partir de los postulados fundamentales de la mecánica cuántica.

  - Se consolidó la relación entre superposición, evolución unitaria, colapso parcial y medición probabilística dentro del flujo conceptual de Shor.
  - Se reforzó la interpretación de la QFT como un cambio de base que transforma diferencias de fase en diferencias observables de amplitud.
  - Se estudió cómo los picos de amplitud permiten revelar la periodicidad asociada a la función modular.
  - Se conectó la regla de Born con la extracción probabilística de información después de aplicar la QFT.
  - Se revisó cómo los operadores definen bases de medición dentro del espacio de Hilbert.
  - Surgieron dudas relacionadas con el papel físico de la fase y la naturaleza de la información revelada al cambiar de base.

- Parte importante de la semana se dedicó a repaso y consolidación mediante tarjetas de Anki.

- La semana tuvo varias interrupciones debido a la mudanza y proyectos universitarios, generando múltiples días fuera de eje.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_27.pdf`
  - `Biblioteca_Semana_27.pdf`

- El Diario documenta:

  - reconstrucción conceptual de Shor
  - consolidación de postulados
  - preguntas relacionadas con fase cuántica y QFT
  - dificultades al reconstruir matemáticamente Shor
  - mantenimiento del eje durante la mudanza

- La Biblioteca incluye:

  - relación entre postulados y Shor
  - interpretación geométrica y probabilística de la QFT
  - aparición de picos de amplitud tras el cambio de base
  - conexión entre amplitud y probabilidad mediante la regla de Born
  - repasos de conceptos olvidados relacionados con operadores y bases de medición

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.
  
### Codex

Conceptos añadidos o consolidados:

- Born Rule
- Quantum Amplitude
- Permutation

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_27.pdf`
- `Diario_de_Bordo_Semana_27.pdf`

### Notas

La semana representó una transición desde entender Shor como un algoritmo hacia comprenderlo como una consecuencia directa de los postulados de la mecánica cuántica. La QFT dejó de verse únicamente como una herramienta matemática y comenzó a interpretarse como un mecanismo físico capaz de transformar información de fase en amplitudes medibles. Incluso con la mudanza y los días fuera de eje, el proyecto mantuvo continuidad conceptual.

---

## Semana 28 (2026-05-11 al 2026-05-15)

### Teoría y aprendizaje

- Se inició formalmente la Misión 2 del Campamento 3 enfocada en la mecánica cuántica aplicada al hardware cuántico.

- Se consolidó la comprensión del qubit como un sistema físico real de dos niveles energéticos.

  - Se conectó la representación abstracta del estado cuántico con sistemas físicos reales.
  - Se reforzó la idea de superposición como fenómeno físico y no únicamente matemático.

- Se estudió el papel del Hamiltoniano como operador de energía y generador de evolución temporal.

  - Se relacionó directamente la ecuación de Schrödinger con el comportamiento físico del qubit.
  - Se entendió que controlar un qubit implica modificar físicamente su Hamiltoniano mediante campos externos.

- Se desarrolló la intuición física del control cuántico.

  - Se estudió cómo campos electromagnéticos, microondas y pulsos controlan la evolución del sistema.
  - Se consolidó la interpretación física de las compuertas cuánticas como evoluciones unitarias inducidas.

- Se trabajó resonancia cuántica y transferencia de amplitud entre niveles energéticos.

  - Se conectó frecuencia, diferencia de energía y transición entre estados.
  - Se introdujo la noción de oscilaciones de Rabi como mecanismo físico fundamental del control de qubits.

- Se realizaron conexiones conceptuales importantes entre:

  - mecánica cuántica
  - teoría de operadores
  - evolución temporal
  - hardware cuántico
  - control físico experimental

- Se identificó explícitamente la enorme profundidad y ramificación física detrás del software cuántico.

- Hubo un día fuera de eje debido a procesos universitarios, manteniendo aun así la continuidad general del sistema.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_28.pdf`
  - `Biblioteca_Semana_28.pdf`

- El Diario documenta:

  - el inicio de la Misión 2 del Campamento 3
  - la transición conceptual hacia hardware cuántico
  - dificultades asociadas a la profundidad física de los temas
  - conexiones entre teoría abstracta y control físico real
  - un día fuera de eje por inscripción universitaria
  - reflexiones conceptuales relacionadas con el ruido, resonancia y evolución física

- La Biblioteca incluye:

  - desarrollo conceptual de sistemas de dos niveles
  - Hamiltoniano y ecuación de Schrödinger
  - control físico del qubit
  - resonancia cuántica
  - interpretación física de compuertas
  - oscilaciones de Rabi
  - conexiones entre teoría y hardware cuántico

- La biblioteca de esta semana representó principalmente una consolidación física e interpretativa de conceptos previamente matemáticos.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- Se desarrolló el texto conceptual:

  - `Los Telares de la Realidad.md`

- El texto exploró una interpretación simbólica entre ruido, cuántica y construcción física de la realidad.

### Codex

Conceptos añadidos o consolidados:

- Born rule
- Quantum amplitude
- Permutation
- Electromagnetic field
- Frequency
- Pulse
- Resonant

### Estructura del repositorio

- Se añadieron nuevos documentos correspondientes a la Semana 28.
- No se realizaron modificaciones estructurales importantes en el repositorio.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_28.pdf`
- `Diario_de_Bordo_Semana_28.pdf`

### Notas

Esta semana marcó el inicio del descenso hacia la física real del hardware cuántico. El qubit dejó de verse únicamente como un vector abstracto y comenzó a entenderse como un sistema físico gobernado por energía, resonancia y evolución temporal. La conexión entre teoría matemática y control experimental empezó a tomar forma concreta dentro del ascenso.

---

## Semana 29 (2026-05-18 al 2026-05-24)

### Teoría y aprendizaje

- La semana se centró en consolidar la comprensión física de las oscilaciones de Rabi como mecanismo fundamental de control cuántico.

  - Se estudió cómo un campo electromagnético resonante modifica el Hamiltoniano de un sistema de dos niveles.
  - Se conectó el concepto de compuerta cuántica con pulsos físicos de microondas aplicados sobre el qubit.
  - Se comprendió que el control cuántico depende de parámetros físicos como frecuencia, amplitud, fase y duración del pulso.
  - Se reforzó la idea de que una compuerta cuántica corresponde a una evolución continua gobernada por un Hamiltoniano.
  - Se consolidó la relación entre resonancia, intercambio de energía y evolución sinusoidal de probabilidades.
  - Se exploró el efecto del detuning y cómo una frecuencia desintonizada reduce la amplitud de las oscilaciones y genera errores.

- También hubo jornadas de repaso y consolidación conceptual utilizando Anki y revisión de temas anteriores.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_29.pdf`
  - `Biblioteca_Semana_29.pdf`

- El Diario documenta:

  - días de consolidación y repaso
  - reflexiones sobre resonancia y ruido
  - conexiones intuitivas con oscilaciones sinusoidales
  - días fuera de eje utilizados como recuperación

- La Biblioteca incluye:

  - explicación conceptual de las oscilaciones de Rabi
  - relación entre Hamiltoniano y control físico
  - resonancia entre microondas y diferencia de energía
  - interpretación física de compuertas cuánticas
  - resumen conceptual del fenómeno de Rabi
  - integración conceptual entre teoría y simulación computacional

### Código

- Se desarrolló una simulación interactiva de oscilaciones de Rabi y control físico de qubits.

- El programa implementó:

  - evolución de un qubit sobre la esfera de Bloch
  - Hamiltoniano efectivo en marco rotante
  - control IQ mediante componentes I, Q y detuning
  - pulsos resonantes y desintonizados
  - visualización simultánea de:
    - trayectoria del estado cuántico
    - pulso físico de laboratorio
    - Hamiltoniano efectivo
    - probabilidad de transición entre |0⟩ y |1⟩

- La simulación permitió conectar directamente la física experimental del hardware cuántico con la interpretación geométrica en la esfera de Bloch.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- Se consolidaron conceptos relacionados con:

  - Resonancia
  - Oscilaciones de Rabi
  - Hamiltoniano efectivo
  - Control IQ
  - Detuning
  - Sistemas de dos niveles
  - Pulsos resonantes

### Estructura del repositorio

- Se incorporó una nueva sección en CODIGO llamada 'rabi'.
- No se realizaron cambios importantes en la estructura general del repositorio.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_29.pdf`
- `Diario_de_Bordo_Semana_29.pdf`

### Notas

La semana representó una transición importante entre la mecánica cuántica abstracta y el control físico real de qubits. Las oscilaciones de Rabi dejaron de verse como una simple fórmula matemática y comenzaron a entenderse como la dinámica física que permite implementar compuertas cuánticas mediante campos electromagnéticos resonantes.

---

## Semana 30 (2026-05-25 al 2026-05-29)

### Teoría y aprendizaje

- La semana se centró en consolidar una línea importante del Campamento 3 mediante el repaso de temas previos y la disección conceptual del código asociado a oscilaciones de Rabi.

  - Se reforzó la idea de que un qubit físico puede modelarse como un sistema de dos niveles energéticos permitidos.
  - Se conectó el control externo mediante un pulso o campo electromagnético con la modificación efectiva del Hamiltoniano del sistema.
  - Se consolidó la lectura del Hamiltoniano efectivo en el marco rotante, identificando los papeles de la frecuencia natural del qubit, la frecuencia del drive, el detuning, la frecuencia de Rabi y la velocidad real de rotación.
  - Se trabajó la interpretación de las oscilaciones de Rabi como el resultado observable de una evolución gobernada por Schrödinger y convertida en probabilidades mediante la regla de Born.
  - Se clarificó que el detuning no reduce la norma del estado, sino que cambia el eje efectivo alrededor del cual rota el vector en la esfera de Bloch.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_30.pdf`
  - `Biblioteca_Semana_30.pdf`

- El Diario documenta:

  - días fuera de eje por cierre de actividades y exámenes finales;
  - el regreso al repaso de temas pendientes;
  - la disección final del código de Rabi;
  - el cierre satisfactorio del ciclo semanal.

- La Biblioteca incluye:

  - repaso de cartas de Anki relacionadas con temas nuevos, vencidos y fallados;
  - estructura física del control de un qubit mediante fase, duración, amplitud y frecuencia;
  - explicación del qubit como sistema cuántico real de dos niveles;
  - desarrollo conceptual del Hamiltoniano efectivo;
  - separación de símbolos como ωq, ωd, Δ, Ω y Ωeff;
  - ciclo de funcionamiento desde el sistema físico hasta la medición probabilística;
  - vínculo entre Schrödinger, Bloch y Born como tres ventanas del mismo fenómeno.

### Código

- Se revisó conceptualmente el código de simulación de oscilaciones de Rabi, conectando sus parámetros con el modelo físico trabajado durante la semana.

- No se registró el desarrollo de un script completamente nuevo durante esta semana.

### TEXTOS

- No se desarrollaron textos literarios nuevos esta semana.

### Codex

Se integró una nueva entrada al Codex:

- `SINUSOIDAL (sin) — Sinusoidal`

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_30.pdf`
- `Diario_de_Bordo_Semana_30.pdf`

### Notas

La Semana 30 funcionó como una consolidación importante dentro del Campamento 3: permitió entender mejor que las oscilaciones de Rabi no son solo una curva probabilística, sino la manifestación visible de un sistema cuántico real controlado por un campo externo, descrito por un Hamiltoniano efectivo y observado finalmente mediante probabilidades.

---

## Semana 31 (2026-06-01 al 2026-06-07)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado y estuvo marcado por una continuidad irregular del eje.

  - Se registraron varios días fuera de eje, con dificultad para mantener la sintonía del estudio.
  - Se mantuvo el vínculo con el proyecto mediante repaso de cartas de Anki y revisión de conceptos anteriores.
  - Se inició el contacto conceptual con la superconductividad como entrada al hardware cuántico.
  - Se introdujo la idea de la unión Josephson como pieza física clave para construir circuitos superconductores con niveles de energía cuantizados.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_31.pdf`
  - `Biblioteca_Semana_31.pdf`

- El Diario documenta una semana corta e irregular:

  - Día 151: repaso de cartas de Anki y mantenimiento mínimo del eje.
  - Día 152: día fuera de eje, sin comentarios.
  - Día 153: finalización del texto `Disvarianza Mental`.
  - Día 154: nuevo día fuera de eje, con olvido del estudio.
  - Día 155: idea inicial sobre superconductividad y resistencia.

- La Biblioteca incluye:

  - Registro de términos observados o pendientes: ventana, Schrödinger, Bloch, Born/Rabi.
  - Repaso de cartas de Anki vistas previamente, como Rabi, Hamiltoniano y compuertas.
  - Continuación y sentido final del texto `Disvarianza Mental`.
  - Primer apunte conceptual sobre superconductividad:
    - la corriente eléctrica puede fluir sin resistencia en ciertos materiales muy fríos;
    - los superconductores permiten reducir pérdidas de energía en circuitos;
    - la unión Josephson permite obtener niveles de energía cuantizados útiles para representar `|0⟩` y `|1⟩`.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- Se desarrolló y cerró el texto:

  - `Disvarianza_Mental.md`

- El texto consolidó una reflexión personal sobre desviación, eje mental y retorno a la dirección interna.

### Codex

- No se añadieron nuevas entradas.

### Estructura del repositorio

- Se añadieron los documentos correspondientes a la Semana 31.
- Se incorporó el texto `Disvarianza_Mental.md` como producción escrita de la semana.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_31.pdf`
  - `Diario_de_Bordo_Semana_31.pdf`

### Notas

- La Semana 31 no fue una semana de avance técnico fuerte, sino una semana de sostenimiento del eje. Aun con interrupciones y días fuera de ritmo, el proyecto mantuvo continuidad mediante repaso, cierre textual y apertura conceptual hacia la superconductividad.

---

## Semana 32 (2026-06-08 al 2026-06-14)

### Teoría y aprendizaje

- La semana se centró en consolidar la intuición física detrás de la superconductividad y su conexión con el hardware cuántico.

  - Se trabajó la idea de los pares de Cooper como correlaciones cuánticas entre electrones dentro de un superconductor.
  - Se reforzó que los electrones individuales son fermiones y obedecen el principio de exclusión de Pauli.
  - Se entendió que un par de Cooper, al estar formado por dos fermiones con espines opuestos, puede comportarse colectivamente como un bosón compuesto.
  - Se repasaron ideas clave: momento total compensado, carga doble, brecha de energía, longitud de coherencia y fase común.
  - Se conectó la superconductividad con la posibilidad de corriente sin resistencia.
  - Se revisó electricidad clásica para aclarar corriente, voltaje, resistencia, ley de Ohm, corriente continua y corriente alterna.
  - Se introdujo la unión Josephson como una estructura superconductor–aislante delgado–superconductor capaz de permitir corriente superconductora por acoplamiento cuántico.
  - Persistió una dificultad conceptual importante: comprender de forma intuitiva el túnel cuántico y cómo una corriente puede atravesar una barrera aislante delgada.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_32.pdf`
  - `Biblioteca_Semana_32.pdf`

- El Diario documenta:

  - avance desde la intuición inicial de superconductores y pares de Cooper;
  - dudas sobre si ciertos fenómenos son clásicos o cuánticos;
  - repaso de temas anteriores;
  - conexión con electricidad clásica;
  - primera noción de unión Josephson.

- La Biblioteca incluye:

  - desarrollo conceptual sobre pares de Cooper;
  - explicación de fermiones, bosones y bosones compuestos;
  - repaso de longitud de coherencia, brecha de energía y fase común;
  - fundamentos de electricidad clásica;
  - ley de Ohm aplicada a conductores normales y superconductores;
  - diferencia entre DC y AC;
  - introducción al efecto Josephson DC.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

Se integraron nuevas entradas conceptuales al Codex:

- Fermion
- Boson
- Composite Boson

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_32.pdf`
- `Diario_de_Bordo_Semana_32.pdf`

### Notas

La semana funcionó como puente entre física fundamental y hardware cuántico: los pares de Cooper dejaron de ser solo una idea abstracta y empezaron a conectarse con superconductores reales, corriente sin resistencia y uniones Josephson. El avance principal fue entender que la computación cuántica superconductora nace de una mezcla muy delicada entre electricidad clásica, correlación cuántica y fase colectiva.

---

## Semana 33 (2026-06-15 al 2026-06-19)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado y se centró principalmente en revisión, mantenimiento y consolidación.

  - Se repasaron conceptos previos mediante tarjetas de Anki.
  - Se reforzó la idea de que el acoplamiento cuántico entre superconductores con distinta fase puede producir corriente.
  - Se retomó la condición física `kBT << Δ`, conectando energía térmica, superconductividad y estabilidad del estado.
  - Se consolidó la intuición de que los pares de Cooper son correlaciones cuánticas.
  - Se repasó que la superconductividad corresponde a un estado de ciertos materiales donde no aparece resistencia eléctrica.
  - Se registró una conexión pendiente con Shor y su parte cuántica asociada a la estimación de fase.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_33.pdf`
  - `Biblioteca_Semana_33.pdf`

- El Diario documenta:

  - Día 161: repaso de cartas de Anki y detección de temas antiguos que requieren refresco.
  - Día 162: día fuera de eje, registrado como mantenimiento.
  - Día 163: preparación y realización de la primera clase a nivel universitario.
  - Día 164: repaso de teoría con tarjetas y reconocimiento de temas antiguos poco frescos.
  - Día 165: creación de un nuevo texto llamado `Hoy` y cierre de semana con baja energía.

- La Biblioteca incluye:

  - notas de repaso sobre acoplamiento cuántico entre superconductores.
  - recordatorios sobre energía térmica, fase, frecuencia, amplitud y duración.
  - consolidación de ideas sobre pares de Cooper y superconductividad.
  - mención de Shor y la estimación de fase como punto cuántico pendiente.
  - registro del nuevo texto `Hoy` como representación reflexiva de la semana.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- Se desarrolló un texto nuevo llamado `Hoy`.

  - El texto representó la semana desde una perspectiva más personal.
  - Su núcleo fue la diferencia entre la emoción inicial y el eje persistente en el tiempo.
  - El texto funcionó como cierre simbólico de una semana de baja energía pero continuidad sostenida.

### Codex

- No se generaron nuevas entradas esta semana.


### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_33.pdf`
- `Diario_de_Bordo_Semana_33.pdf`

### Notas

La Semana 33 no fue una semana de expansión técnica fuerte, sino de permanencia. El avance principal estuvo en sostener el proyecto mediante repaso, memoria y registro, incluso con energía baja y días fuera de eje. El núcleo conceptual quedó en la consolidación de superconductividad, pares de Cooper y acoplamiento cuántico, mientras que el núcleo personal quedó expresado en el texto `Hoy`.

---

## Semana 34 (2026-06-22 al 2026-06-26)

### Teoría y aprendizaje

- Se consolidó la entrada al estudio del hardware cuántico superconductivo, enfocándose en la relación entre superconductores, aislante delgado y unión de Josephson.

  - Se trabajó la idea de que la unión de Josephson permite el túnel cuántico de pares de Cooper entre superconductores.
  - Se conectó la diferencia de fase superconductora con una energía dependiente de fase.
  - Se identificó que esta energía introduce no linealidad en el Hamiltoniano del circuito.
  - Se reforzó la intuición de que la anarmonicidad permite obtener niveles de energía discretos no igualmente espaciados.
  - Se conectó esa estructura energética con la posibilidad de seleccionar dos niveles como |0⟩ y |1⟩.
  - Se clarificó que el transmon superconductivo es una forma concreta de construir un qubit físico, aunque no la única.
  - Se repasó la idea de superposición de direcciones en flux qubits, asociando los estados base a corrientes en sentidos opuestos.

- La semana tuvo interrupciones y días fuera de eje, pero también produjo un avance conceptual importante: pasar de “qubit como estado abstracto” a “qubit como sistema físico realizable”.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_34.pdf`
  - `Biblioteca_Semana_34.pdf`

- El Diario documenta:

  - Dos días fuera de eje registrados durante la semana.
  - Una revisión profunda del túnel cuántico, la diferencia energética superconductora y la estructura mental acumulada hasta ahora.
  - La definición de una idea general teórica del hardware cuántico.
  - El cierre de algunas dudas sobre estructuras físicas de qubits, como flux qubits y superposición de direcciones.
  - Un día de repaso con tarjetas de Anki para hilar ideas.

- La Biblioteca incluye:

  - Apuntes sobre la unión superconductor–aislante–superconductor.
  - Relación entre unión de Josephson, túnel cuántico y pares de Cooper.
  - Organización mental de la estructura física: electrones → frío extremo → pares de Cooper → condensado superconductor → circuito superconductivo.
  - Conexión entre unión de Josephson, capacitor, Hamiltoniano del circuito, anarmonicidad y estados |0⟩ / |1⟩.
  - Repaso de fórmulas clave del transmon:
    - Energía dependiente de fase: `-EJ cos(φ)`
    - Hamiltoniano básico: `H = 4EC(n - ng)^2 - EJ cos(φ)`
    - Diferencia de fase: `Δφ`

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se desarrollaron nuevas entradas esta semana.
  
### Estructura del repositorio

- No se modificó la estructura general del repositorio esta semana.
- Se incorporan los documentos semanales como registro oficial del avance.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_34.pdf`
- `Diario_de_Bordo_Semana_34.pdf`

### Notas

- La Semana 34 fue una semana de avance irregular pero conceptualmente importante. El núcleo del progreso fue comprender que la física del hardware cuántico no es un detalle posterior, sino la base que permite que un qubit exista como sistema físico controlable. La unión de Josephson apareció como el puente entre superconductividad, fase, no linealidad y niveles de energía útiles para codificar información cuántica.

---

## Semana 35 (2026-06-29 al 2026-07-03)

### Teoría y aprendizaje

- El progreso teórico de la semana fue limitado y se centró principalmente en revisión, consolidación y mantenimiento del eje de estudio.

  - Se repasaron conceptos asociados al transmon y al efecto Josephson mediante tarjetas de Anki.
  - Se consolidó la intuición de la entropía como dispersión, incertidumbre y pérdida de energía útil.
  - Se distinguió entre baja entropía como energía más concentrada y alta entropía como energía más distribuida y menos aprovechable.
  - Se reforzó la diferencia entre macroestado y microestado como base estadística para entender por qué los sistemas tienden a estados de mayor entropía.
  - Se dejó planteada la transición conceptual hacia la Misión 3: La Batalla contra la Entropía, enfocada en decoherencia.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_35.pdf`
  - `Biblioteca_Semana_35.pdf`

- El Diario documenta una semana irregular, marcada por repasos rápidos, días fuera de eje y actividades externas al proyecto.

  - Día 171: se trabajó la entropía como conquista conceptual.
  - Día 172: se registró un día fuera de eje por avance en otros proyectos.
  - Día 173: se realizó repaso rápido en Anki para mantener continuidad.
  - Día 174: se registró un día fuera de eje asociado a trámites universitarios.
  - Día 175: se retomó el repaso rápido en Anki mientras se gestionaban papeles y planes alternativos.

- La Biblioteca fue principalmente de repaso y consolidación.

  - Se repasaron fórmulas del transmon, incluyendo la energía Josephson dependiente de fase y el Hamiltoniano básico.
  - Se escribió una reflexión de cierre sobre haber tocado parte de la zona física de la cuántica.
  - Se inició la Misión 3 con una introducción conceptual a la entropía.
  - Se aclaró que la entropía no es simplemente “caos”, sino una medida de dispersión, incertidumbre y pérdida de energía útil.
  - Se conectó el equilibrio termodinámico con estados de máxima entropía.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se desarrollaron nuevas entradas.

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_35.pdf`
- `Diario_de_Bordo_Semana_35.pdf`

### Notas

La Semana 35 fue una semana de baja producción técnica, pero de continuidad real. El avance principal no estuvo en desarrollar teoría nueva, sino en mantener vivo el proyecto durante días atravesados por otros trámites y prioridades. La idea central que quedó consolidada fue que la entropía prepara el terreno para comprender la decoherencia: el entorno no solo “molesta” al qubit, sino que dispersa información, energía y fase hasta romper la coherencia útil del sistema.

---

## Semana 36 (2026-07-06 al 2026-07-12)

### Teoría y aprendizaje

- El progreso teórico de la semana fue moderado y se concentró principalmente en comprender la coherencia y la decoherencia de un qubit.

  - Se definió la coherencia como la conservación de una relación de fase estable entre las amplitudes de un estado cuántico.
  - Se estudió cómo la interacción entre el qubit y su entorno distribuye información del sistema y destruye gradualmente su capacidad de interferir.
  - Se comprendió que la decoherencia no corresponde a un único mecanismo, sino que engloba distintos procesos de pérdida de información cuántica.
  - Se diferenció entre el tiempo de relajación $T_1$, asociado a la pérdida de energía del estado excitado, y el tiempo de desfase $T_2$, asociado a la pérdida de la fase relativa.
  - Se relacionó $T_2$ con la relajación energética y el desfase puro mediante:

  $$\frac{1}{T_2} = \frac{1}{2T_1} + \frac{1}{T_\phi}$$

  - Se consolidó que un qubit puede perder coherencia sin necesariamente perder energía.
  - Se repasaron mediante Anki conceptos relacionados con el Hamiltoniano del transmon, la diferencia de fase, la energía de Josephson y la energía de carga.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos correspondientes a la semana:

  - `Diario de bordo - Semana 36.pdf`
  - `Biblioteca - Semana 36.pdf`

- El Diario documentó:

  - El estudio de coherencia, decoherencia y los tiempos $T_1$ y T2.
  - Dos días fuera de eje debido al cansancio y al trabajo en proyectos externos.
  - La reestructuración general del proyecto dentro del repositorio Git.
  - Una sesión de repaso mediante Anki.
  - La continuidad del proyecto aun durante una semana fragmentada por otras responsabilidades.

- El registro semanal fue irregular:

  - Día 176: estudio de coherencia, decoherencia, $T_1$ y T2.
  - Día 177: día fuera de eje por cansancio y proyectos externos.
  - Día 178: reestructuración total del proyecto en Git.
  - Día 179: repaso de contenidos mediante Anki.
  - Día 180: día fuera de eje por trabajo en el proyecto SIGEDON.

- La Biblioteca incluyó:

  - Una explicación intuitiva de la coherencia como estabilidad de fase.
  - El papel del entorno en la pérdida de información cuántica.
  - La evolución conjunta entre qubit y entorno.
  - La relajación energética $|1\rangle \rightarrow |0\rangle$.
  - El desfase de una superposición cuántica.
  - La relación entre $T_1$, $T_2$ y $T_\phi$.
  - Un repaso del Hamiltoniano básico del transmon y de sus componentes energéticos.

### Código

- No se desarrolló código nuevo relacionado con el contenido cuántico durante esta semana.

- La actividad técnica se concentró en la organización y documentación del repositorio, no en nuevas simulaciones o implementaciones.


### TEXTOS

- No se desarrollaron textos, poemas o relatos nuevos esta semana.

### Codex

- No se añadieron nuevas entradas al Codex durante esta semana.

### Estructura del repositorio

- Se realizó una reestructuración general de la documentación principal del proyecto para mejorar su navegación, legibilidad y presentación externa.

- Se añadió `ESTRUCTURA.md` como mapa técnico del repositorio.

  - El documento establece el propósito de las carpetas principales.
  - Facilita la orientación de nuevos lectores.
  - Reduce la necesidad de deducir la organización únicamente a partir de los nombres de los directorios.

- Se añadió `VISION.md` como documento central de identidad y dirección del proyecto.

  - Se trasladó allí la explicación conceptual de Elíejesresce.
  - Se separó la visión general del proyecto de los documentos operativos y de estudio.
  - Se estableció una entrada más clara para comprender el propósito del ascenso.

- Se revisó `README.md`.

  - Se adaptó a la nueva arquitectura documental.
  - Se mejoró la navegación hacia los documentos principales.
  - Se redujo la repetición de explicaciones que ahora pertenecen a `VISION.md` y `ESTRUCTURA.md`.

- Se simplificaron los nombres de los documentos almacenados en `IDENTIDAD/`.

  - `ELIEJESRESCE_CONCEPTO.pdf` fue sustituido por `concepto.pdf`.
  - `ELIEJESRESCE_K2_GUIA_MAESTRA_DE_ASCENSO.pdf` fue sustituido por `guia_maestra.pdf`.
  - `ELIEJESRESCE_K2_PROYECTO_AUMENTADO.pdf` fue sustituido por `ruta_aumentada.pdf`.
  - `ELIEJESRESCE_K2_PROYECTO.pdf` fue sustituido por `ruta_original.pdf`.

- Se retiraron de `IDENTIDAD/` documentos redundantes o que ya no cumplían una función clara dentro de la nueva estructura.

  - `ELIEJESRESCE_K2_HORARIO.pdf`
  - `ELIEJESRESCE_K2_PORTADA.pdf`
  - `fondo.png`

- Se mantuvieron sin cambios estructurales las áreas `DIARIO/`, `BIBLIOTECA/` y `CODEX/`, debido a que ya cumplen correctamente su función dentro del flujo semanal.

- La reorganización permitió que el repositorio dejara de presentarse como una acumulación de documentos y comenzara a funcionar como un sistema documental con identidad, visión y rutas de navegación explícitas.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la Semana 36:

  - `Diario de bordo - Semana 36.pdf`
  - `Biblioteca - Semana 36.pdf`

- Se normalizaron los nombres de los documentos permanentes de identidad, eliminando prefijos largos y redundantes.

- Los documentos originales eliminados fueron reemplazados por versiones con nombres más cortos y coherentes con el contexto de la carpeta que los contiene.

### Notas

- La Semana 36 no estuvo dominada por una gran cantidad de contenido nuevo, sino por una combinación de consolidación conceptual y mantenimiento estructural.

- En el plano científico, se construyó una comprensión más precisa de la decoherencia: el qubit pierde su comportamiento útil cuando el entorno obtiene información sobre su estado, ya sea mediante pérdida de energía, pérdida de fase o ambas.

- En el plano documental, el proyecto recibió una reorganización profunda que separó con mayor claridad su identidad, su visión, su estructura y sus rutas de aprendizaje.

- Aunque dos jornadas quedaron fuera de eje, la semana mantuvo continuidad mediante estudio, repaso y trabajo de infraestructura. El avance principal no fue recorrer una gran distancia nueva, sino hacer que el camino ya recorrido resultara mucho más claro y respirable.

---

## Semana 37 (2026-07-13 al 2026-07-19)

### Teoría y aprendizaje

- Se cerró el Campamento 3, dedicado a construir una comprensión conceptual de la base física de los qubits y de algunas de sus principales limitaciones reales.

  - Se consolidó la distinción entre relajación energética y pérdida de coherencia de fase mediante los tiempos T1 y T2.
  - Se comprendió que T1 describe la transición del estado excitado |1⟩ al estado fundamental |0⟩ causada por la pérdida de energía hacia el entorno.
  - Se reforzó que T2 describe la degradación de la relación de fase entre las amplitudes de una superposición, incluso cuando el qubit todavía conserva energía.
  - Se conectaron el sistema físico de dos niveles, el Hamiltoniano, la resonancia y el control mediante campos externos.
  - Se cerró la revisión conceptual de superconductividad, efecto Josephson, qubits transmon, ruido y decoherencia.
  - El estudio fue deliberadamente conceptual: no se profundizó extensamente en matemáticas ni se desarrollaron implementaciones, porque el objetivo del campamento era comprender la física necesaria para continuar el ascenso.

- Se inició la fase de transición denominada **El Laboratorio**, orientada al control experimental del qubit.

  - Esta fase fue presentada como el puente entre comprender físicamente el qubit y aprender a controlarlo mediante señales reales.
  - No se desarrolló todavía contenido experimental nuevo más allá de la introducción de la fase.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_37.pdf`
  - `Biblioteca_Semana_37.pdf`

- El Diario documentó:

  - un repaso ligero mediante Anki;
  - dos días fuera del eje;
  - una jornada afectada por más de veinticuatro horas sin dormir;
  - la retroalimentación final sobre T1 y T2;
  - el cierre del Campamento 3;
  - el comienzo simbólico de la fase El Laboratorio;
  - varias interrupciones relacionadas con el trabajo realizado en el sistema SIGEDON.

- La Biblioteca incluyó:

  - la diferencia física entre pérdida de energía y pérdida de fase;
  - la interpretación de |0⟩ como estado fundamental y |1⟩ como estado excitado;
  - la transición |1⟩ → |0⟩ como proceso de relajación;
  - la explicación de la pérdida progresiva de sincronización de fase en una superposición;
  - el cierre conceptual del Campamento 3;
  - los hitos alcanzados en sistemas de dos niveles, Hamiltonianos, resonancia, superconductividad, efecto Josephson, transmon, ruido, decoherencia, T1 y T2;
  - la introducción de El Laboratorio como fase de transición hacia el control experimental.

- La semana tuvo un ritmo irregular y estuvo marcada por trabajo externo, cansancio y días fuera del eje. Aun así, se mantuvo la continuidad suficiente para cerrar formalmente una etapa completa del proyecto.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se añadieron nuevas entradas al Codex esta semana.

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.
- El principal cambio dentro de la ruta de aprendizaje fue la transición formal desde el Campamento 3 hacia la fase El Laboratorio.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_37.pdf`
  - `Diario_de_Bordo_Semana_37.pdf`

### Notas

La Semana 37 no destacó por su volumen de trabajo, sino por cerrar una etapa importante. El Campamento 3 dejó una cadena conceptual completa desde el qubit como sistema físico hasta sus mecanismos reales de control, ruido y pérdida de información. Incluso con interrupciones y días fuera del eje, el sistema se dobló, pero no se rompió.

---

## Semana 38 (2026-07-20 al 2026-07-26)

### Teoría y aprendizaje

- Se inició la Fase de Transición: **El Laboratorio**, orientada al control experimental de qubits.

  - Se introdujo la espectroscopía como el estudio de la respuesta de un sistema frente a distintas frecuencias.
  - Se comprendió que la espectroscopía cuántica permite localizar la frecuencia de resonancia correspondiente a una transición entre niveles energéticos.
  - Se relacionó la diferencia de energía entre los estados `|0⟩` y `|1⟩` con la frecuencia de transición mediante `ΔE = hf`.
  - Se describió el procedimiento experimental de inicializar, excitar, medir y repetir el experimento para construir la población excitada `P₁(f)`.
  - Se reconoció que una respuesta elevada en `P₁` señala la proximidad de una resonancia del sistema.
  - Se introdujo la teoría de control cuántico mediante los parámetros frecuencia, amplitud, duración y fase de los pulsos.
  - Se estudiaron las oscilaciones de Rabi como la evolución coherente de la población entre `|0⟩` y `|1⟩`.
  - Se conectó la amplitud del pulso con la frecuencia angular de Rabi y, por tanto, con la velocidad de rotación del estado.
  - Se distinguió entre variar la duración del pulso para observar `P₁(t)` y variar su amplitud para modificar la velocidad de la oscilación.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_38.pdf`
  - `Biblioteca_Semana_38.pdf`

- El Diario documentó:

  - La introducción teórica a la espectroscopía cuántica.
  - La comprensión general del procedimiento experimental utilizado para realizarla.
  - El inicio conceptual de la teoría de control cuántico.
  - Un día fuera del eje debido a los finales universitarios.
  - Un repaso breve de tarjetas en Anki para mantener la continuidad durante los últimos días de evaluaciones.

- La Biblioteca incluyó:

  - La apertura formal de la Fase de Transición: El Laboratorio.
  - Una explicación intuitiva de espectro, resonancia y respuesta frecuencial.
  - La relación entre niveles energéticos y frecuencia de transición.
  - El procedimiento completo de una espectroscopía de qubit.
  - La construcción experimental de la curva `P₁(f)`.
  - La introducción a los parámetros de control de un pulso de microondas.
  - El modelo ideal de las oscilaciones de Rabi:

    `P₁(t) = sin²(Ωᵣt / 2)`

  - La interpretación de `Ωᵣ` como velocidad angular de la rotación inducida sobre el estado.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se proporcionó un archivo actualizado del Codex para esta semana.

### Estructura del repositorio

- No se modificó la estructura general del repositorio esta semana.
- Se abrió documentalmente la nueva etapa correspondiente a la Fase de Transición: El Laboratorio.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_38.pdf`
  - `Diario_de_Bordo_Semana_38.pdf`

### Notas

- La semana marcó el paso desde comprender la física interna del qubit hacia comprender cómo se identifica y controla experimentalmente. La espectroscopía permitió localizar la transición energética del sistema, mientras que las oscilaciones de Rabi introdujeron la relación entre los parámetros físicos del pulso y la evolución coherente del estado. Aunque los finales universitarios redujeron el ritmo, el eje se mantuvo mediante estudio breve y repaso.

---

## Semana 39 (2026-07-27 al 2026-08-02)

### Teoría y aprendizaje

- No se registraron avances teóricos nuevos durante esta semana.

  - El estudio formal quedó suspendido debido a la atención dedicada a trámites universitarios, documentación y preparativos de viaje.
  - Se realizaron dos repasos breves mediante Anki para mantener activos conceptos estudiados anteriormente.
  - No se introdujeron nuevos conceptos, desarrollos matemáticos ni conexiones técnicas.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_39.pdf`
  - `Biblioteca_Semana_39.pdf`

- El Diario documentó:

  - Tres días fuera del eje.
  - Dos jornadas de repaso mediante Anki.
  - La aceptación en la Universidad de Murcia.
  - El avance de los preparativos del viaje.
  - La organización de documentos y papeles.
  - La obtención de la lista definitiva de requisitos.
  - El trámite del pasaporte.

- La Biblioteca no incorporó contenido teórico nuevo correspondiente a esta semana.

  - Las notas visibles sobre amplitud de pulsos y oscilaciones de Rabi pertenecen al cierre del trabajo anterior.
  - Desde el día 191 solo se registraron días fuera del eje y repasos mediante Anki.
  - No se desarrollaron ejercicios, derivaciones ni exploraciones conceptuales nuevas.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrolló texto nuevo esta semana.

### Codex

- No se añadieron nuevas entradas al Codex esta semana.

### Estructura del repositorio

- No se modificó la estructura del repositorio esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_39.pdf`
- `Diario_de_Bordo_Semana_39.pdf`

### Notas

La Semana 39 no produjo avances técnicos nuevos. El proyecto permaneció en pausa mientras la atención se concentró en la aceptación universitaria, la documentación y los preparativos del viaje. Aun así, el vínculo con el eje se mantuvo mediante repasos mínimos en Anki y el registro honesto de los días fuera del eje.

---

## Semana 40 (2026-08-03 al 2026-08-09)

### Teoría y aprendizaje

- La semana se centró en llevar la intuición de la espectroscopía cuántica a una representación dinámica de la respuesta de un qubit.

  - Se reforzó la relación entre la frecuencia del pulso aplicado y la frecuencia natural del qubit.
  - Se observó que, al aproximarse a la resonancia, aumenta la capacidad del pulso para transferir población entre |0⟩ y |1⟩.
  - Se conectaron la frecuencia, amplitud, duración y fase del pulso con la evolución temporal del estado.
  - Se consolidó la interpretación de las oscilaciones de Rabi como consecuencia de la evolución coherente del qubit bajo un campo de control.
  - Se realizó un repaso mediante Anki, detectándose algunos conceptos previamente estudiados que habían comenzado a olvidarse.

- El ritmo de estudio fue irregular durante parte de la semana, con varios días fuera de eje dedicados principalmente a asuntos personales y documentación.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_40.pdf`
  - `Biblioteca_Semana_40.pdf`

- El Diario documentó:

  - la creación y posterior funcionamiento de la simulación interactiva de espectroscopía;
  - la escritura del texto `Felicidad`;
  - la conexión entre la simulación y las oscilaciones de Rabi;
  - días fuera de eje relacionados con gestiones personales;
  - una sesión final de repaso mediante Anki.

- La Biblioteca incluyó:

  - una descripción conceptual del laboratorio interactivo;
  - la relación entre resonancia, población excitada y evolución del qubit;
  - una explicación básica de cómo el desajuste de frecuencia modifica la trayectoria del estado;
  - el registro conceptual del texto `Felicidad`.

### Código

- Se desarrolló un laboratorio interactivo para simular la respuesta de un qubit ante un pulso de microondas.

  - Permite modificar frecuencia, amplitud, duración y fase mediante controles deslizantes.
  - Calcula la evolución temporal del estado a partir de un modelo de dos niveles.
  - Visualiza simultáneamente la onda aplicada, la población excitada P₁ y la trayectoria del estado sobre la esfera de Bloch.
  - Incluye animación en tiempo real y controles para pausar, continuar y reiniciar la simulación.
  - Permite comparar el comportamiento del qubit dentro y fuera de resonancia.

- Aunque inicialmente fue registrada en el Diario como una simulación en Qiskit, la implementación final adjunta utiliza NumPy y Matplotlib directamente.

### TEXTOS

- Se escribió el texto `Felicidad`.

  - El texto representa un instante en el que emociones, recuerdos y caminos recorridos convergen en un único punto.
  - Utiliza imágenes provenientes de la mecánica cuántica —onda, resonancia, estado y colapso— como recursos metafóricos para expresar cómo algo antes percibido como un sueño termina formando parte de la realidad.

### Codex

- No se añadieron nuevas entradas al Codex esta semana.

### Estructura del repositorio

- No se realizaron cambios significativos en la estructura general del repositorio esta semana.

- Se incorporó el nuevo código correspondiente al laboratorio interactivo y el texto desarrollado durante la semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_40.pdf`
- `Diario_de_Bordo_Semana_40.pdf`

### Notas

La Semana 40 convirtió parte de la teoría reciente de espectroscopía en una representación visual y manipulable. El avance principal no estuvo en introducir nuevos fundamentos, sino en observar directamente cómo los parámetros de un pulso controlan la evolución de un qubit y cómo la resonancia se manifiesta en su población y trayectoria. Fue una semana irregular en ritmo, pero con una conexión clara entre teoría, simulación y representación física.

---

## Semana 41 (2026-08-10 al 2026-08-16)

### Teoría y aprendizaje

- La semana marcó el inicio conceptual del Campamento 4 y una reorientación previa al estudio profundo de Quantum Machine Learning: comprender primero los fundamentos de Machine Learning clásico.

  - Se estudió qué significa realmente que una máquina "aprenda".
  - Se distinguió entre la estructura del modelo, definida por el diseñador, y los parámetros internos que pueden ajustarse durante el entrenamiento.
  - Se comprendió que un sistema de aprendizaje no programa explícitamente una solución para cada caso, sino que utiliza ejemplos para ajustar su comportamiento.
  - Se introdujo la representación general de un modelo parametrizado como `f_θ(x)`.
  - Se interpretó el aprendizaje como la búsqueda de una configuración de parámetros `θ*` que produzca un comportamiento adecuado para la tarea.
  - Se introdujo la generalización como la capacidad de utilizar la estructura aprendida sobre ejemplos nuevos y no únicamente sobre los datos observados durante el entrenamiento.
  - Se aclaró que una máquina no crea completamente su propio programa: la arquitectura, las reglas generales y el objetivo son definidos externamente, mientras que determinados parámetros son ajustados mediante el proceso de aprendizaje.

- El Campamento 4 fue ampliado para convertir la ruta original de QML en un recorrido más profundo y experimental, incluyendo fundamentos de aprendizaje, codificación de datos, quantum kernels, circuitos parametrizados, entrenamiento híbrido, VQC, trainability, PennyLane, comparación con modelos clásicos y una expedición propia.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_bordo_Semana_41.pdf`
  - `Biblioteca_Semana_41.pdf`

- El Diario documentó:

  - un día fuera de eje debido a gestiones y documentos;
  - el inicio formal del Campamento 4 — El Glaciar de la Inteligencia;
  - la ampliación y reorganización de la ruta del campamento;
  - el comienzo del estudio de Machine Learning clásico;
  - la aparición de la generalización como concepto central del aprendizaje.

- La Biblioteca incluyó:

  - un repaso mediante Anki;
  - una introducción al objetivo del Campamento 4;
  - el análisis de la diferencia entre reglas explícitamente programadas y comportamiento aprendido;
  - un modelo lineal sencillo `f(x) = wx + b` para separar estructura y parámetros;
  - la abstracción del modelo mediante `f_θ(x)`;
  - la interpretación de `θ*` como una configuración aprendida;
  - una primera construcción conceptual de la generalización.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se desarrollaron entradas nuevas esta semana.

### Estructura del repositorio

- Se amplió la documentación correspondiente al Campamento 4.

- Se añadió:

  - `campamento_4_extension.pdf`

- Se actualizaron:

  - `ruta_aumentada.pdf`
  - `ruta_original.pdf`

- La ruta del Campamento 4 pasó de una introducción breve a una estructura extendida orientada a construir progresivamente los fundamentos de QML y conectar cada etapa con experimentos reproducibles.

### Normalización de archivos

- Se consolidaron como referencias oficiales de la semana:

  - `Biblioteca_Semana_41.pdf`
  - `Diario_de_bordo_Semana_41.pdf`

### Notas

La Semana 41 funcionó como un cambio de orientación antes de entrar de lleno en QML. La pregunta dejó de ser únicamente cómo construir un modelo cuántico y pasó a una más fundamental: qué significa que cualquier modelo aprenda. La distinción entre estructura, parámetros, experiencia y generalización establece ahora la base clásica necesaria para comprender posteriormente qué parte de ese proceso puede trasladarse o modificarse mediante computación cuántica.

---

## Semana 42 (2026-08-17 al 2026-08-23)

### Teoría y aprendizaje

- La semana se centró en construir los fundamentos conceptuales del aprendizaje automático antes de avanzar hacia modelos de Quantum Machine Learning.

  - Se estudió la función de pérdida como una medida del desacuerdo entre las predicciones de un modelo y las respuestas esperadas.
  - Se introdujo la optimización de los parámetros mediante la búsqueda de valores que minimicen la pérdida:

    θ* = arg min L(θ)

  - Se separaron conceptualmente tres componentes fundamentales del aprendizaje:
    - el modelo `fθ(x)`, encargado de producir respuestas;
    - el estado aprendido, representado por los parámetros resultantes del entrenamiento;
    - el algoritmo de aprendizaje, responsable de transformar `θ → θ'` utilizando la experiencia disponible.
  - Se construyó el marco tarea–experiencia–rendimiento, interpretando el aprendizaje como una mejora del desempeño en una tarea a partir de experiencia.
  - Se desarrolló un mapa completo del proceso de entrenamiento:

    datos → predicción → pérdida → actualización de parámetros → repetición

  - Se consolidó la idea de que durante el entrenamiento el programa no necesita convertirse en otro programa: cambia progresivamente su estado interno mediante los parámetros aprendidos.

### Diario y Biblioteca

- Se exportaron y organizaron los archivos:

  - `Diario_de_Bordo_Semana_42.pdf`
  - `Biblioteca_Semana_42.pdf`

- El Diario documentó cinco jornadas:

  - Los días 207, 208 y 209 estuvieron dedicados al desarrollo conceptual del aprendizaje automático.
  - Los días 206 y 210 fueron registrados como días fuera de eje.
  - El cambio de sistema operativo de Windows a Linux apareció como interrupción principal al inicio de la semana.
  - Se registraron conexiones alrededor de la naturaleza del aprendizaje y de la relación entre mejora de rendimiento y experiencia.

- La Biblioteca desarrolló:

  - función de pérdida;
  - modelo parametrizado;
  - estado aprendido;
  - algoritmo de aprendizaje;
  - tarea, experiencia y medida de rendimiento;
  - ciclo iterativo de entrenamiento;
  - representación gráfica del cambio `θ₀ → θ₁` producido a partir de datos y pérdida.

### Código

- No se desarrolló código nuevo esta semana.

### TEXTOS

- No se desarrollaron textos nuevos esta semana.

### Codex

- No se desarrollaron entradas nuevas esta semana.


### Estructura del repositorio

- No se registraron cambios en la estructura del repositorio durante esta semana.

### Normalización de archivos

Se consolidaron como referencias oficiales de la semana:

- `Biblioteca_Semana_42.pdf`
- `Diario_de_Bordo_Semana_42.pdf`

### Notas

La Semana 42 estableció el modelo mental básico del aprendizaje automático: un sistema produce predicciones, mide su error mediante una función de pérdida y utiliza esa información para modificar sus parámetros. El aprendizaje quedó entendido como el cambio acumulado del estado interno del modelo producido por la experiencia, preparando la base clásica necesaria antes de introducir componentes cuánticos.