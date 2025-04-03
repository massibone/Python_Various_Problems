import random

# Funzione per lanciare un dado
def lancia_dado():
    return random.randint(1, 6)

# Funzione per giocare una partita a dadi
def gioca_partita():
    print("Benvenuto alla partita a dadi!")
    giocatore1 = input("Inserisci il nome del giocatore 1: ")
    giocatore2 = input("Inserisci il nome del giocatore 2: ")

    # Inizializza i punteggi dei giocatori
    punteggio_giocatore1 = 0
    punteggio_giocatore2 = 0
   # Gioca la partita
    while True:
        print(f"\nPunteggio attuale: {giocatore1} - {punteggio_giocatore1}, {giocatore2} - {punteggio_giocatore2}")
        input(f"{giocatore1}, premi invio per lanciare il dado...")
        dado_giocatore1 = lancia_dado()
        print(f"{giocatore1} ha lanciato: {dado_giocatore1}")

        input(f"{giocatore2}, premi invio per lanciare il dado...")
        dado_giocatore2 = lancia_dado()
        print(f"{giocatore2} ha lanciato: {dado_giocatore2}")
