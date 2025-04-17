import numpy as np

def tabella_moltiplicazione_numpy_grande(righe, colonne):
    """
    Crea una tabella di moltiplicazione di grandi dimensioni utilizzando NumPy.

    Args:
        righe: Numero di righe.
        colonne: Numero di colonne.

    Returns:
        Array NumPy contenente la tabella.
    """
    righe_array = np.arange(1, righe + 1).reshape(-1, 1)
    colonne_array = np.arange(1, colonne + 1)
    tabella = righe_array * colonne_array
    return tabella

# Esempio: tabella 1000x1000
tabella_grande = tabella_moltiplicazione_numpy_grande(1000, 1000)
print(tabella_grande)

# Per tabelle ancora più grandi (es. 10000x10000), 
# considera di salvare l'array in un file
# np.save('tabella_grande.npy', tabella_grande)
