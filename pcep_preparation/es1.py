'''
Trova tutte le parole con 4 lettere di senso compiuto. Possiamo utilizzare la lista dei quadrati pari per creare un filtro per le parole.
'''
# Legge il testo da un file
with open('testo.txt', 'r') as file:
    testo = file.read()

# Sostituisce i caratteri non alfabetici con spazi
testo = ''.join(e for e in testo if e.isalnum() or e.isspace()).lower()

# Divide il testo in parole
parole = testo.split()

# Crea una lista di parole con 4 lettere
parole_4_lettere = [parola for parola in parole if len(parola) == 4]

# Stampa le parole con 4 lettere
for parola in parole_4_lettere:
    print(parola)
