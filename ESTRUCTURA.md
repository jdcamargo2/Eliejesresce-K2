# Estructura del repositorio

Este documento funciona como mapa interno de **Elíejesresce K2**. Su objetivo es explicar cómo está organizado el repositorio, qué contiene cada carpeta y cómo navegar el proyecto sin perderse entre documentos, código, bitácoras y material histórico.

```text
ELIEJESRESCE-K2/
├── BIBLIOTECA/
│   ├── 2025/
│   │   └── Biblioteca_Semana_XX.pdf
│   └── 2026/
│       └── Biblioteca_Semana_XX.pdf
│
├── CODEX/
│   └── Codex.md
│
├── DIARIO/
│   ├── 2025/
│   │   └── Diario_de_Bordo_Semana_XX.pdf
│   └── 2026/
│       └── Diario_de_Bordo_Semana_XX.pdf
│
├── CODIGO/
│   └── src/
│       ├── bell/
│       ├── consolidacion/
│       ├── deutsch_jozsa/
│       ├── esfera_bloch/
│       ├── estres_cuantico/
│       ├── grover/
│       ├── hilbert/
│       ├── learning_qiskit/
│       ├── mixtos/
│       ├── operadores/
│       ├── postulados/
│       ├── rabi/
│       ├── shor/
│       ├── teleportacion_cuantica/
│       └── transformacion_lineal/
│
├── IDENTIDAD/
│   ├── VISION.md
│   ├── Guia_Maestra_de_Ascenso.pdf
│   └── recursos visuales y documentos base
│
├── TEXTOS/
│   └── textos simbólicos y reflexivos del proyecto
│
├── CHANGELOG.md
├── ESTRUCTURA.md
├── LICENSE.txt
└── README.md
```

# Raíz del repositorio

La raíz contiene los documentos principales de navegación, presentación y control del proyecto.

- `README.md`: portada pública del repositorio.
- `CHANGELOG.md`: registro semanal completo del avance técnico, conceptual y estructural.
- `ESTRUCTURA.md`: mapa interno del repositorio.
- `LICENSE.txt`: licencia del proyecto.

# BIBLIOTECA/

Contiene los documentos semanales de estudio técnico. Aquí viven explicaciones, derivaciones, notas conceptuales, ejercicios, fórmulas, conexiones y desarrollo profundo de los temas trabajados.

Convención de nombre:

```text
Biblioteca_Semana_XX.pdf
```

# DIARIO/

Contiene la bitácora semanal del proceso. Registra avances, dudas, días fuera de eje, reflexiones, decisiones y continuidad del proyecto.

Convención de nombre:

```text
Diario_de_Bordo_Semana_XX.pdf
```

# CODEX/

Contiene el diccionario técnico acumulativo del proyecto.

- `Codex.md`: archivo vivo donde se integran términos técnicos de computación cuántica, álgebra lineal, física, hardware, papers, siglas y conceptos asociados.

# CODIGO/

Contiene simulaciones, scripts, experimentos y laboratorios conceptuales desarrollados durante el proyecto.

La carpeta principal es:

```text
CODIGO/src/
```

Organización actual por tema:

- `bell/`: estados de Bell, diagramas y transformaciones asociadas.
- `consolidacion/`: scripts de cierre, repaso o integración conceptual.
- `deutsch_jozsa/`: implementación del algoritmo de Deutsch–Jozsa.
- `esfera_bloch/`: visualizaciones, mediciones y animaciones de la Esfera de Bloch.
- `estres_cuantico/`: pruebas de límite, simulación y escalabilidad.
- `grover/`: implementaciones y visualizaciones del algoritmo de Grover.
- `hilbert/`: ejercicios y simulaciones asociadas al espacio de Hilbert.
- `learning_qiskit/`: scripts iniciales de aprendizaje y convenciones en Qiskit.
- `mixtos/`: estados mixtos, matriz densidad y pérdida de coherencia.
- `operadores/`: operadores cuánticos, evolución y medición.
- `postulados/`: simulaciones asociadas a los postulados de la mecánica cuántica.
- `rabi/`: simulaciones de oscilaciones de Rabi y control físico de qubits.
- `shor/`: implementaciones del algoritmo de Shor ideal y ruidoso.
- `teleportacion_cuantica/`: teleportación cuántica en álgebra, circuitos y simulación.
- `transformacion_lineal/`: visualizaciones de transformaciones lineales en 2D y 3D.

# IDENTIDAD/

# IDENTIDAD/

Contiene la visión narrativa, documentos fundacionales, ruta técnica vigente, guía maestra y recursos visuales del universo Elíejesresce K2.

Elementos principales:

- `VISION.md`: visión narrativa y filosófica actual del proyecto.
- `concepto.pdf`: explicación original del concepto de la palabra Elíejesresce.
- `guia_maestra.pdf`: guía de constancia, protocolos, frases fundamentales, ejes de estabilidad y modo viaje.
- `ruta_aumentada.pdf`: ruta técnica vigente del ascenso cuántico.
- `ruta_original.pdf`: documento original del proyecto, conservado como referencia histórica.
- `logo.png`: logo principal del proyecto.

# TEXTOS/

Contiene escritos simbólicos, poemas, reflexiones y piezas narrativas nacidas del estudio cuántico.

Estos textos no son material externo al proyecto: funcionan como registro de intuiciones, metáforas y formas personales de interpretar conceptos cuánticos.

# Convenciones generales

Los documentos semanales usan número de semana con dos dígitos:

```text
Semana_01
Semana_02
Semana_10
Semana_35
```

Los PDFs principales siguen esta forma:

```text
Biblioteca_Semana_XX.pdf
Diario_de_Bordo_Semana_XX.pdf
```

El `CHANGELOG.md` conserva el avance completo semana a semana.

El `README.md` funciona como portada pública y no debe contener listados extensos de archivos.

# Criterio de navegación

Para entender el proyecto desde fuera, sigue esta ruta:

1. [`README.md`](./README.md) — portada pública del proyecto.
2. [`CHANGELOG.md`](./CHANGELOG.md) — avance completo semana a semana.
3. [`IDENTIDAD/VISION.md`](./IDENTIDAD/VISION.md) — visión narrativa y filosófica.
4. [`CODEX/Codex.md`](./CODEX/Codex.md) — diccionario técnico acumulativo.
5. [`CODIGO/src/`](./CODIGO/src/) — simulaciones y experimentos.