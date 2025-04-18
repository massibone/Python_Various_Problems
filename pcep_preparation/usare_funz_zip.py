'''
Le liste devono avere la stessa lunghezza. 
Se una lista è più corta, 
zip() si fermerà alla lunghezza della lista più breve.'''
# Esempio di liste
chiavi = ["nome", "età", "città"]
valori = ["Alice", 30, "Roma"]

# Creazione del dizionario usando zip()
dizionario = dict(zip(chiavi, valori))

print(dizionario)
