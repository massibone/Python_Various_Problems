'''
Per tabelle così grandi da non poter essere memorizzate interamente in RAM, i generatori sono la soluzione.
'''

def genera_riga_moltiplicazione(riga, colonne):
    """Genera una riga della tabella di moltiplicazione."""
    for colonna in range(1, colonne + 1):
        yield riga * colonna

def tabella_moltiplicazione_generatore_grande(righe, colonne):
    """Genera una tabella di moltiplicazione di grandi dimensioni utilizzando generatori."""
    for riga in range(1, righe + 1):
        yield genera_riga_moltiplicazione(riga, colonne)
