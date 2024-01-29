import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, vertici):
        self.vertici = vertici
        self.matrice_adiacenza = [[0 for _ in range(vertici)] for _ in range(vertici)]

    def aggiungi_arco(self, u, v):
        self.matrice_adiacenza[u][v] = 1
        self.matrice_adiacenza[v][u] = 1

    def colora_grafo(self):
        colori_disponibili = [0] * self.vertici
        colori_disponibili[0] = 1

        for vertice in range(1, self.vertici):
            adiacenti_colorati = []
            for i in range(self.vertici):
                if self.matrice_adiacenza[vertice][i] == 1 and colori_disponibili[i] != 0:
                    adiacenti_colorati.append(colori_disponibili[i])

            min_colore = 1
            while True:
                if min_colore not in adiacenti_colorati:
                    break
                min_colore += 1

            colori_disponibili[vertice] = min_colore

        return colori_disponibili

grafo = Grafo(5)  # Creiamo un grafo con 5 vertici

# Aggiungiamo gli archi del grafo
grafo.aggiungi_arco(0, 1)
grafo.aggiungi_arco(0, 2)
grafo.aggiungi_arco(1, 2)
grafo.aggiungi_arco(1, 3)
grafo.aggiungi_arco(2, 3)
grafo.aggiungi_arco(3, 4)

colori = grafo.colora_grafo()

# Creiamo il grafo utilizzando NetworkX
G = nx.Graph()

# Aggiungiamo i nodi e gli archi
for i in range(grafo.vertici):
    G.add_node(i)

for i in range(grafo.vertici):
    for j in range(i+1, grafo.vertici):
        if grafo.matrice_adiacenza[i][j] == 1:
            G.add_edge(i, j)

# Definiamo i colori per i nodi
color_map = {0: 'blue', 1: 'green', 2: 'red', 3: 'yellow', 4: 'orange'}

# Disegniamo il grafo utilizzando Matplotlib
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=[color_map[color] for color in colori], with_labels=True, node_size=800)
plt.show()
