def approx_root(num, degree, iterations=10):
    # Inizializza la stima con la radice appropriata del numero
    x = num ** (1 / degree)

    # Creiamo la descrizione del metodo di approssimazione
    metodo_descrizione = f"Stima successiva:\n" \
                          f"Utilizziamo la formula:\n" \
                          f"Stima successiva = 1/2 * (stima corrente + {num} / stima corrente^{degree-1})\n"

    # Esegui l'iterazione per migliorare l'approssimazione
    for i in range(iterations):
        x = 1 / degree * ((degree - 1) * x + num / (x ** (degree - 1)))
        metodo_descrizione += f"\nStima {i+1}:\n" \
                              f"x_{i+1} = 1/2 * (x_{i} + {num} / x_{i}^{degree-1}) = {x}"

    return x, metodo_descrizione

# Richiedi all'utente il grado della radice
degree = int(input("Inserisci il grado della radice (da 3 a 10): "))

# Richiedi all'utente di inserire il valore su cui calcolare l'approssimazione
valore = float(input("Inserisci il valore su cui calcolare l'approssimazione: "))

# Descrizione del metodo di approssimazione a mente
print(f"Approssimazione della radice {degree}-esima usando metodo a mente:")
print(f"{approx_root(valore, degree)[1]}")

# Calcola l'approssimazione della radice
approssimazione = approx_root(valore, degree)[0]

# Mostra il risultato
print(f"\nL'approssimazione della radice {degree}-esima è: {approssimazione}")

