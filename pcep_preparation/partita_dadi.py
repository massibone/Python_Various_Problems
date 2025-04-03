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

 
        # Aggiorna i punteggi dei giocatori
        if dado_giocatore1 > dado_giocatore2:
            punteggio_giocatore1 += 1
            print(f"{giocatore1} vince questo round!")
        elif dado_giocatore2 > dado_giocatore1:
            punteggio_giocatore2 += 1
            print(f"{giocatore2} vince questo round!")
        else:
            print("Parità! Nessun punto assegnato.")

        # Verifica se un giocatore ha vinto la partita
        if punteggio_giocatore1 >= 3:
            print(f"\n{giocatore1} vince la partita con un punteggio di {punteggio_giocatore1} - {punteggio_giocatore2}!")
            break
        elif punteggio_giocatore2 >= 3:
            print(f"\n{giocatore2} vince la partita con un punteggio di {punteggio_giocatore2} - {punteggio_giocatore1}!")
            break

# Gioca la partita
gioca_partita()
