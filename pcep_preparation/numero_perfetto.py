def trova_numero_perfetto(limite):
    '''
    Trova il primo numero perfetto minore o uguale a limite.
    Args:
        limite: Il limite superiore della ricerca.
    Returns:
        Il numero perfetto trovato, altrimenti None.
    '''
    


    for num in range(2, limite + 1):
        divisori = []
        for i in range(1, num):
            if num % i == 0:
                divisori.append(i)
        try:
            if sum(divisori) == num:
                return num
        except TypeError:
            print("Errore: divisori non è una lista.")
    else:
        print("Nessun numero perfetto trovato fino a", limite)

# Un numero perfetto è uguale alla somma dei suoi divisori propri
risultato = trova_numero_perfetto(10000)
if risultato:
    print("Il primo numero perfetto trovato è:", risultato)
