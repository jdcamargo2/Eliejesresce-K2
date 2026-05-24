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
  * relación entre **sin**θ = **M**/**N** y la probabilidad de éxito.
  * comprensión del movimiento periódico y del fenómeno de *overshoot.*
* Formalización de los operadores fundamentales:
  * oráculo como **reflexión de fase** sobre el subespacio de soluciones.
  * difusión como **inversión respecto al estado promedio.**
  * composición del operador de Grover como rotación efectiva por **2θ.**
* Comprensión explícita del **número óptimo de iteraciones**:
  * derivación aproximada **k≈4πN/M.**
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
- No se realizaron cambios estructurales mayores:

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

  “Distributed quantum computing across an optical network link”**D. Main, P. Drmota, D. P. Nadlinger, E. M. Ainley, A. Agrawal, B. C. Nichol, R. Srinivas, G. Araneda y D. M. Lucas.
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

- Se exportaron

  y organizaron los archivos:

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

- Se crea formalmente el **Codex** como ténica de acumulación de vocabulario técnico.

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

No se modifico la estructura del repositorio esta semana.

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
  - Definición cuántica: |ψ(t)⟩ :contentReference[oaicite:4]{index=4}
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
  - `Diario_de_bordo_Semana_21.pdf`
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

- No se agregaron terminos nuevos esta semana.

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

# Semana 26 (2026-04-27 al 2026-05-03)

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

# Semana 27 (2026-05-04 al 2026-05-10)

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

# Semana 28 (2026-05-11 al 2026-05-15)

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

# Semana 29 (2026-05-18 al 2026-05-24)

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