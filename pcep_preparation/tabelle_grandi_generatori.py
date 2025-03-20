'''
Per tabelle così grandi da non poter essere memorizzate interamente in RAM, i generatori sono la soluzione.
'''

def genera_riga_moltiplicazione(riga, colonne):
    """Genera una riga della tabella di moltiplicazione."""
    for colonna in range(1, colonne + 1):
        yield riga * colonna
