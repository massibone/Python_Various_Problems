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
