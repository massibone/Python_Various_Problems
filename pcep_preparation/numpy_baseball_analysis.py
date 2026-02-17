'''
Analisi di dati relativi ai giocatori di baseball utilizzando la libreria NumPy.
Lo script esegue le seguenti operazioni su un array 2D (np_baseball):

•
Estrazione e stampa della 50esima riga.

•
Creazione di un vettore dedicato per il peso (seconda colonna).

•
Selezione dell'altezza specifica del 124esimo giocatore.

'''

import numpy as np

# Nota: 'baseball' deve essere una lista di liste definita precedentemente.
# Esempio di struttura: baseball = [[180, 78], [185, 82], ...]

def analyze_baseball_data(baseball):
    # Creazione di np_baseball (2 colonne: altezza, peso)
    np_baseball = np.array(baseball)

    # 1. Stampa della 50esima riga di np_baseball
    # L'indicizzazione parte da 0, quindi la 50esima riga è all'indice 49.
    print("50esima riga di np_baseball:")
    print(np_baseball[49, :])

    # 2. Creazione di una nuova variabile np_weight contenente l'intera seconda colonna
    np_weight = np_baseball[:, 1]
    print("\nVariabile np_weight creata correttamente (seconda colonna).")

    # 3. Selezione dell'altezza (prima colonna) del 124esimo giocatore e stampa
    # Il 124esimo giocatore ha indice 123. L'altezza è nella prima colonna (indice 0).
    height_124 = np_baseball[123, 0]
    print(f"\nAltezza del 124esimo giocatore: {height_124}")

    return np_weight, height_124

if __name__ == "__main__":
    # Dati di test per rendere lo script eseguibile
    test_data = [[180, 75]] * 150 
    analyze_baseball_data(test_data)
