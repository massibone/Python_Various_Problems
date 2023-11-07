import matplotlib.pyplot as plt

# Configura il grafico
plt.figure(figsize=(10, 5))
plt.title("Triangolo rovesciato con 8 puntini alla base e livelli decrescenti")
plt.xlabel("X")
plt.ylabel("Y")

x = []
y = []

# Calcola il numero di puntini alla base
base_points = 8
for i in range(base_points):
    x.append(i + 1)
    y.append(1)

# Calcola i puntini per gli altri livelli
num_levels = 8
for level in range(2, num_levels + 1):
    for i in range(level):
        x.append(i + 1 + (base_points - level) / 2)
        y.append(num_levels - level + 1)
        x.append(4.5)
        y.append(8)
plt.scatter(x, y, s=100)  # s è la dimensione dei puntini

plt.grid()
plt.show()
