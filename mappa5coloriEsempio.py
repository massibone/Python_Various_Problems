import matplotlib.pyplot as plt
import networkx as nx

# Creiamo un grafo vuoto
G = nx.Graph()

# Aggiungiamo i nodi
nodi = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodi)

# Aggiungiamo gli archi
archi = [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
G.add_edges_from(archi)

# Definiamo i colori per i nodi
colori = ['red', 'green', 'blue', 'yellow', 'orange']

# Assegnamo un colore a ciascun nodo
color_map = {nodo: colori[i] for i, nodo in enumerate(nodi)}

# Disegniamo il grafo con i colori assegnati ai nodi
nx.draw(G, with_labels=True, node_color=[color_map[nodo] for nodo in G.nodes()], node_size=1000, font_size=12)
plt.show()
