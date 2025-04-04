'''
Le comprehension sono un modo conciso per creare nuove liste, 
dizionari o altri tipi di dati in Python, 
utilizzando una sintassi specifica. 
Sono utilizzate per semplificare il codice e renderlo più leggibile.
Comprehension per liste: [x**2 for x in range(10) if x % 2 == 0].
per dizionari:
dizionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dizionario_pari = {chiave: valore for chiave, valore in dizionario.items() if valore % 2 == 0}
print(dizionario_pari)  # {'b': 2, 'd': 4}
'''

quadrati_pari = [x**2 for x in range(1, 101) if x % 2 == 0]
for i, quadrato in enumerate(quadrati_pari):
    print(f"Il quadrato di {i*2 + 2} è {quadrato}")
