'''
x contenitore 5 lt e y contenitore 3lt tot è sempre 8lt di vino
'''
# Definiamo una funzione che prende in input la capacità dei due contenitori e la quantità di vino da dividere
def divide_wine(capacity1, capacity2, wine):
    # Inizializziamo i contenitori
    container1 = 0
    container2 = 0

    # Versiamo il vino nel grande recipiente
    container1 = wine

    # Se il contenitore da 5 litri è vuoto, lo riempiamo
    if container2 == 0:
        container2 = capacity2

    # Versiamo il vino dal contenitore da 5 litri in quello da 3 litri finché non è pieno
    while container2 > capacity1:
        container2 -= 1
        container1 += 1

    # Versiamo il vino dal contenitore da 3 litri in quello da 5 litri finché non è pieno
    while container1 > capacity2:
        container1 -= 1
        container2 += 1

    # Restituiamo la quantità di vino nei due contenitori
    return container1, container2

# Esempio di utilizzo
capacity1 = 3
capacity2 = 5
wine = 8
container1, container2 = divide_wine(capacity1, capacity2, wine)
print(f"Il contenitore da {capacity1} litri contiene {container1} litri di vino.")
print(f"Il contenitore da {capacity2} litri contiene {container2} litri di vino.")

