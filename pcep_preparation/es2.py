'''
Trovare parole con 4 lettere che iniziano con una lettera specifica
'''
# Legge il testo da un file
with open('testo.txt', 'r') as file:
    testo = file.read()

# Sostituisce i caratteri non alfabetici con spazi
testo = ''.join(e for e in testo if e.isalnum() or e.isspace()).lower()

# Divide il testo in parole
parole = testo.split()
