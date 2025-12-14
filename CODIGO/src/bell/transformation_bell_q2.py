"""
Visualiza las transformaciones entre los estados de Bell bajo la acción de las
operaciones de Pauli (X, Y, Z) aplicadas al segundo qubit.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Nodos (los estados Bell)
states = ["Φ+", "Ψ+", "Φ-", "Ψ-"]

# Grafo
G = nx.Graph()
G.add_nodes_from(states)

# Aristas para Pauli en el segundo qubit (q2)

edges = [
    # X2: Φ+ ↔ Ψ+, Φ- ↔ Ψ-
    ("Φ+", "Ψ+", "X₂"),
    ("Φ-", "Ψ-", "X₂"),
    # Z2: Φ+ ↔ Φ-, Ψ+ ↔ Ψ-
    ("Φ+", "Φ-", "Z₂"),
    ("Ψ+", "Ψ-", "Z₂"),
    # Y2: Φ+ ↔ Ψ-, Φ- ↔ Ψ+
    ("Φ+", "Ψ-", "Y₂"),
    ("Φ-", "Ψ+", "Y₂"),
]

# Añadimos aristas al grafo
for u, v, label in edges:
    if G.has_edge(u, v):
        G[u][v]["label"] += f", {label}"
    else:
        G.add_edge(u, v, label=label)

# Posición de los nodos (idéntica al grafo de q1)
pos = {
    "Φ+": (0, 1),
    "Ψ+": (1, 1),
    "Φ-": (0, 0),
    "Ψ-": (1, 0),
}

plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="white", edgecolors="black")
nx.draw_networkx_labels(G, pos, font_size=16)

nx.draw_networkx_edges(G, pos, width=2)

edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

plt.title("Transformaciones de Bell bajo Pauli en el segundo qubit (q₂)", pad=20)
plt.axis("off")
plt.tight_layout()
plt.show()
