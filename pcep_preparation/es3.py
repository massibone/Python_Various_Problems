'''
Trovare parole con 4 lettere che contengono una lettera specifica
'''
# Legge il testo da un file
with open('testo.txt', 'r') as file:
    testo = file.read()

# Sostituisce i caratteri non alfabetici con spazi
testo = ''.join(e for e in testo if e.isalnum() or e.isspace()).lower()

# Divide il testo in parole
parole = testo.split()

# Crea una lista di parole con 4 lettere che contengono "e"
parole_4_lettere_e = [parola for parola in parole if len(parola) == 4 and 'e' in parola]

# Stampa le parole con 4 lettere che contengono "e"
for parola in parole_4_lettere_e:
    print(parola)
