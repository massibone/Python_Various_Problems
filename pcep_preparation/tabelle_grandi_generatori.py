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

# Esempio: tabella 10000x10000 (genera righe su richiesta)
tabella_enorme = tabella_moltiplicazione_generatore_grande(10000, 10000)


# Esempio di come accedere ai dati (solo una riga alla volta)
for riga in tabella_enorme:
    # Elabora la riga (ad esempio, salvala in un file)
    print(list(riga)[:10])  # Stampa solo i primi 10 elementi della riga
