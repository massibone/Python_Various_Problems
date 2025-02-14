'''
Nell'uso avanzato di costrutti  else
'''

def ricerca_binaria(lista, target):
    sinistra, destra = 0, len(lista) - 1
    while sinistra <= destra:
        mezzo = (sinistra + destra) // 2
        if lista[mezzo] == target:
            return mezzo
        elif lista[mezzo] < target:
            sinistra = mezzo + 1
        else:
            destra = mezzo - 1
    else:
        return -1  # Elemento non trovato
