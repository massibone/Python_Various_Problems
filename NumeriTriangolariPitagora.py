import matplotlib.pyplot as plt

# Configura il grafico
plt.figure(figsize=(6, 3))
plt.title("Puntini per triangolo")
plt.xlabel("X")
plt.ylabel("Y")

x = []
y = []

# Creazione della base del triangolo (3 puntini)
base_x = [2, 4, 6]
base_y = 0.5  # Altezza della base
x.extend(base_x)
y.extend([base_y] * len(base_x))

# Creazione del secondo livello (2 puntini)
second_level_x = [3, 5]
second_level_y = 1.0  # Altezza del secondo livello
x.extend(second_level_x)
y.extend([second_level_y] * len(second_level_x))

# Creazione del vertice del triangolo (1 puntino)
vertex_x = [4]
vertex_y = 1.5  # Altezza del vertice
x.extend(vertex_x)
y.extend([vertex_y] * len(vertex_x))

plt.scatter(x, y, s=100)  # s è la dimensione dei puntini

plt.grid()
plt.show()
