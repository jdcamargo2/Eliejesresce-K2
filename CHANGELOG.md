# CHANGELOG – Elíejesresce K2

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
- Comprensión completa de la estructura de un circuito en Qiskit(crear, agregar compuertas, medir, ejecutar y analizar).
- Estudio formal del **producto tensorial** y su rol en sistemas de 2 qubits.
- Análisis profundo del comportamiento y propósito de la puerta **CNOT**(control, objetivo, orden, matriz 4×4).
- Diferenciación algebraica entre **estados separables** y **estados entrelazados**mediante el criterio *ad – bc*.
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
