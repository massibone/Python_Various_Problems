'''
Differenze tra list, tuple, e set
'''
# --- ESEMPIO DI LIST (elenco ordinato, mutabile, consente duplicati) ---
print("\n--- LIST ---")
lista = [1, 2, 3, 3, 4]
print("Lista iniziale:", lista)

# Modificabilità
lista.append(5)          # Aggiungi elemento
lista[0] = 0            # Modifica elemento
print("Dopo modifica:", lista)

# Duplicati
print("Elemento duplicato (3) conservato:", lista.count(3))

# Ordine
print("Ordine è mantenuto:", lista)  # [0, 2, 3, 3, 4, 5]

# --- ESEMPIO DI TUPLE (elenco ordinato, IMMUTABILE, consente duplicati) ---
print("\n--- TUPLE ---")
tupla = (1, 2, 2, 3)
print("Tuple iniziale:", tupla)

# Tentativo di modifica (genererà errore se scommentato)
# tupla[0] = 0  # TypeError: 'tuple' object does not support item assignment

# Duplicati
print("Elemento duplicato (2) conservato:", tupla.count(2))

# Unpacking
a, b, c, d = tupla
print("Dopo unpacking:", a, b, c, d)  # 1 2 2 3

# --- ESEMPIO DI SET (insieme non ordinato, mutabile, NO duplicati) ---
print("\n--- SET ---")
insieme = {1, 2, 2, 3}
print("Set iniziale (duplicati rimosse):", insieme)  # {1, 2, 3}
