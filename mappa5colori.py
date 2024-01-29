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

        for vertice, colore in enumerate(colori_disponibili):
            print(f"Vertice {vertice}: Colore {colore}")


grafo = Grafo(5)  # Creiamo un grafo con 5 vertici

# Aggiungiamo gli archi del grafo
grafo.aggiungi_arco(0, 1)
grafo.aggiungi_arco(0, 2)
grafo.aggiungi_arco(1, 2)
grafo.aggiungi_arco(1, 3)
grafo.aggiungi_arco(2, 3)
grafo.aggiungi_arco(3, 4)

print("Colorazione del grafo:")
grafo.colora_grafo()
