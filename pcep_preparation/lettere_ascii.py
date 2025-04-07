'''
Creare un dizionario con le lettere dell'alfabeto come chiavi e i loro codici ASCII come valori
'''
dizionario = {lettera: ord(lettera) for lettera in 'abcdefghijklmnopqrstuvwxyz'}
print(dizionario)  # {'a': 97, 'b': 98, 'c': 99, ...}
