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

# Modificabilità
insieme.add(4)
insieme.discard(2)  # Rimuovi elemento
print("Dopo modifica:", insieme)

# Duplicati
print("Duplicati sono stati rimosse:", {1, 1, 2})  # {1, 2}


# Operazioni di insiemi
insieme2 = {3, 4, 5}
print("Unione:", insieme.union(insieme2))          # {1, 3, 4, 5}
print("Intersezione:", insieme.intersection(insieme2))  # {3,4}
# --- CONFRONTO TRA I TIPI ---
print("\n--- CONFRONTO ---")

# Lista vs Tuple vs Set
print(f"""
Lista:     [1, 2, 3]      → Ordinato, mutabile, duplicati OK
Tuple:     (1, 2, 3)      → Ordinato, immutabile, duplicati OK
Set:       {{1, 2, 3}}    → Non ordinato, mutabile, unici elementi
""")

# Frozenset (insieme IMMUTABILE)
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # AttributeError: 'frozenset' object has no attribute 'add'

# --- USO COMUNE ---
print("\n--- ESEMPIO DI USO ---")

# Lista: per elenchi ordinati che cambiano
cibo_preferito = ["pasta", "pizza", "sushi"]
cibo_preferito[0] = "tacos"  # Modifica consentita

# Tuple: per dati fissi (es. coordinate)
coordinate = (10.5, 20.3)
# coordinate[0] = 100  # Errore

# Set: per raccogliere elementi unici
parole = set()
parole.add("casa")
parole.add("casa")  # Ignorato
print("Set di parole uniche:", parole)  # {"casa"}



    def calcola(operazione, a, b):
        """Funzione principale di calcolo"""
        nonlocal storia_operazioni  # Per modificare la storia locale
        
        # Variabili locali
        risultato = 0
        operazione_valida = True
        
        traccia_chiamata(f"calcola({operazione}, {a}, {b})")
        
