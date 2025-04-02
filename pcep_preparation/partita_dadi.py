import random

# Funzione per lanciare un dado
def lancia_dado():
    return random.randint(1, 6)

# Funzione per giocare una partita a dadi
def gioca_partita():
    print("Benvenuto alla partita a dadi!")
    giocatore1 = input("Inserisci il nome del giocatore 1: ")
    giocatore2 = input("Inserisci il nome del giocatore 2: ")
