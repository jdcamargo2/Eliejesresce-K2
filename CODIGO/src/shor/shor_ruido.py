"""
Shor-21 (modo ligero): construye un circuito tipo PEA/QFT para probar escalabilidad.
Usa simulación MPS para reducir RAM y aplica ruido depolarizante a compuertas usadas (H, X, CP).
No es Shor exacto: el “oráculo” aquí solo simula fases para testear la tubería.
"""

import time
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_aer.noise import NoiseModel, depolarizing_error
from qiskit.circuit.library import QFT


# -------------------------
# 1) Configuración general
# -------------------------
n_count = 14                # qubits de conteo (control / fase)
n_work = 5                  # qubits de trabajo (placeholder; para N=21 suele bastar 5)
n_total = n_count + n_work  # total de qubits

# Simulador MPS: más viable que statevector cuando el estado tiene estructura favorable
sim_mps = AerSimulator(method="matrix_product_state")


# -------------------------
# 2) Circuito "tipo Shor" (ligero)
# -------------------------
# Nota: esto NO implementa la exponenciación modular real.
# Solo crea un patrón de fases que luego la iQFT “concentra” en ciertos resultados.
qc = QuantumCircuit(n_total, n_count)

# (a) Registro de conteo en superposición uniforme
qc.h(range(n_count))

# (b) Inicialización del registro de trabajo
# En Shor real se prepara |1> en el registro de trabajo; aquí lo dejamos como ancla.
qc.x(n_count)  # primer qubit del registro de trabajo

# (c) "Oráculo" simplificado: inyección de fase controlada
# Para Shor real, aquí iría la operación controlada: |y> -> |a^(2^q) * y mod N>
# En este modo ligero, solo aplicamos una fase controlada dependiente de q.
for q in range(n_count):
    # En Shor real, esto influiría mediante multiplicación modular.
    # Aquí SOLO usamos power para decidir si “ponemos algo” o no (test).
    power = pow(2, 2**q, 21)
    if power != 1:
        # Fase pequeña controlada hacia un qubit del work register (ancla).
        # Esto no es el oráculo real: es una señal artificial para la demo.
        qc.cp(0.1, q, n_count)

# (d) Inversa de la QFT sobre el registro de conteo
# do_swaps=False evita swaps finales (menos profundidad), y es estándar en implementaciones.
iqft = QFT(n_count, do_swaps=False).inverse()
qc.append(iqft, range(n_count))

# (e) Medición del registro de conteo
qc.measure(range(n_count), range(n_count))


# -------------------------
# 3) Modelo de ruido (suave pero aplicado a las compuertas correctas)
# -------------------------
noise_model = NoiseModel()

# Depolarizing error: 1-qubit y 2-qubits (CP es de 2 qubits)
err_1q = depolarizing_error(0.001, 1)
err_2q = depolarizing_error(0.002, 2)

# IMPORTANTE: aplicar ruido a las compuertas que realmente aparecen en el circuito transpileado.
# H, X son 1q; CP es 2q. (La QFT introduce CP también.)
noise_model.add_all_qubit_quantum_error(err_1q, ["h", "x"])
noise_model.add_all_qubit_quantum_error(err_2q, ["cp"])


# -------------------------
# 4) Transpilación y ejecución
# -------------------------
print(f"--- Ejecutando Shor-21 (Modo Ligero) con {n_total} qubits ({n_count} conteo + {n_work} work) ---")
start = time.time()

# Transpilar para el backend; optimization_level=1 mantiene cosas simples sin destruir estructura
tqc = transpile(qc, sim_mps, optimization_level=1)

# Ejecutar con ruido
result = sim_mps.run(tqc, noise_model=noise_model, shots=1024).result()

elapsed = time.time() - start
counts = result.get_counts()

print(f"¡Éxito! Tiempo: {elapsed:.2f}s")

# Top 3 resultados
top3 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top Resultados:", top3)
