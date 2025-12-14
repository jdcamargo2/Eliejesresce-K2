"""
Visualiza las transformaciones entre los estados de Bell bajo la acción de las
operaciones de Pauli (X, Y, Z) aplicadas al primer qubit.
"""

import networkx as nx
import matplotlib.pyplot as plt

# 1. Definimos los nodos: los 4 estados de Bell
states = ["Φ+", "Ψ+", "Φ-", "Ψ-"]

# 2. Creamos el grafo (no dirigido, porque X, Y, Z llevan de ida y vuelta entre estados Bell)
G = nx.Graph()
G.add_nodes_from(states)

# 3. Definimos las aristas con sus etiquetas (acción de Pauli en el primer qubit)
# X1: Φ+ ↔ Ψ+, Φ- ↔ Ψ-
edges = [
    ("Φ+", "Ψ+", "X₁"),
    ("Φ-", "Ψ-", "X₁"),
    # Z1: Φ+ ↔ Φ-, Ψ+ ↔ Ψ-
    ("Φ+", "Φ-", "Z₁"),
    ("Ψ+", "Ψ-", "Z₁"),
    # Y1: Φ+ ↔ Ψ-, Φ- ↔ Ψ+
    ("Φ+", "Ψ-", "Y₁"),
    ("Φ-", "Ψ+", "Y₁"),
]

# 4. Añadimos las aristas al grafo, acumulando etiquetas si coinciden
for u, v, label in edges:
    if G.has_edge(u, v):
        # Si ya existe una arista, concatenamos etiquetas (por si en el futuro agregas X2, Z2, etc.)
        G[u][v]["label"] += f", {label}"
    else:
        G.add_edge(u, v, label=label)

# 5. Posicionamos los nodos en un cuadrado para que el patrón sea claro
pos = {
    "Φ+": (0, 1),  # arriba izquierda
    "Ψ+": (1, 1),  # arriba derecha
    "Φ-": (0, 0),  # abajo izquierda
    "Ψ-": (1, 0),  # abajo derecha
}

# 6. Dibujamos nodos y aristas
plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="white", edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=16)

nx.draw_networkx_edges(G, pos, width=2)

# 7. Dibujamos las etiquetas de las aristas (X₁, Y₁, Z₁)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.axis("off")
plt.title("Transformaciones de Bell bajo Pauli en el primer qubit (q1)", pad=20)
plt.tight_layout()
plt.show()
