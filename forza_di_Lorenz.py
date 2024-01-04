import numpy as np
import matplotlib.pyplot as plt

def lorentz_force(distance, magnetic_moment=1, permeability=4 * np.pi * 1e-7):
    """
    Calcola la forza di Lorentz tra due magneti circolari.
    """
    return (magnetic_moment**2 * permeability) / (4 * np.pi * distance**4)

# Parametri dei magneti
radius = 0.01  # Raggio del magnete in metri (10 mm)
height = 0.01  # Altezza del magnete in metri (10 mm)
magnetic_moment = np.pi * radius**2 * height  # Momento magnetico del magnete

# Distanze per il grafico (da 10 mm a 50 mm)
distances = np.linspace(0.01, 0.05, 100)

# Calcolo delle forze per ogni distanza
forces = [lorentz_force(distance, magnetic_moment) for distance in distances]

# Plot del grafico
plt.plot(distances, forces)
plt.title('Forza di Lorentz tra due magneti circolari')
plt.xlabel('Distanza (m)')
plt.ylabel('Forza (N)')
plt.show()
