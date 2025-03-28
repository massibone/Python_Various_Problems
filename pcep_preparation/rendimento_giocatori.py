import numpy as np
import pandas as pd

def calcola_rendimento_giocatori(df_risultati):
    """
    Calcola il rendimento dei giocatori di calcetto.

    Args:
        df_risultati: DataFrame Pandas contenente i risultati delle partite.

    Returns:
        DataFrame Pandas con il rendimento dei giocatori.
    """
    punteggi = {'V': 3, 'P': 1, 'S': 0, 'N': 0}
    for colonna in df_risultati.columns[1:]:
        df_risultati[colonna] = df_risultati[colonna].map(punteggi)
    df_risultati['punteggio_totale'] = df_risultati.iloc[:, 1:].sum(axis=1)
    df_risultati['media_punti'] = df_risultati['punteggio_totale'] / 5
    return df_risultati

# Esempio: dati casuali
dati = {
    'giocatore': ['Alberto', 'Alessio', 'Luca', 'Marco'],
    'partita1': ['V', 'P', 'S', 'V'],
    'partita2': ['P', 'V', 'N', 'S'],
    'partita3': ['V', 'S', 'V', 'P'],
    'partita4': ['S', 'V', 'P', 'V'],
    'partita5': ['V', 'P', 'S', 'N']
}
df_risultati = pd.DataFrame(dati)

# Calcola il rendimento
df_rendimento = calcola_rendimento_giocatori(df_risultati)

# Stampa il rendimento
print(df_rendimento)
