
def ha_elementi_unici(lista):
    """
    Restituisce True se tutti gli elementi sono unici, altrimenti False.
    """
    return len(lista) == len(set(lista))

# Test 1: Lista con elementi unici
lista1 = [1, 2, 3, 4, 5]
print(f"Lista1: {lista1} → Unici? {ha_elementi_unici(lista1)}")  # Output: True

# Test 2: Lista con duplicati
lista2 = [1, 2, 2, 3, 4]
print(f"Lista2: {lista2} → Unici? {ha_elementi_unici(lista2)}")  # Output: False
'''
Complessità computazionale:
Convertire una lista in un set richiede O(n) tempo, dove n è la lunghezza della lista.
Il confronto tra le lunghezze è O(1).
Applicabilità: Funziona per qualsiasi tipo di elemento hashable (es. numeri, stringhe, tuple), ma non per oggetti non hashabili (es. liste annidate).
'''
