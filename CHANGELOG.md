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
