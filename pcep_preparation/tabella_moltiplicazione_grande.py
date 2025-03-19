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
