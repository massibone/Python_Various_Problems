'''
Operazioni con insiemi: 
unione, intersezione e differenza.
'''

# Definizione di due insiemi di esempio
insieme_A = {1, 2, 3, 4, 5}
insieme_B = {4, 5, 6, 7, 8}

print("Insieme A:", insieme_A)
print("Insieme B:", insieme_B)

# 1. Unione (elementi presenti in A o B)
unione = insieme_A.union(insieme_B)          # Oppure: insieme_A | insieme_B
print("\nUnione (A ∪ B):", unione)

# 2. Intersezione (elementi comuni a A e B)
intersezione = insieme_A.intersection(insieme_B)  # Oppure: insieme_A & insieme_B
print("Intersezione (A ∩ B):", intersezione)


# 3. Differenza (elementi in A ma non in B)
differenza_A_B = insieme_A.difference(insieme_B)  # Oppure: insieme_A - insieme_B
print("Differenza (A - B):", differenza_A_B)

# Differenza inversa (elementi in B ma non in A)
differenza_B_A = insieme_B.difference(insieme_A)  # Oppure: insieme_B - insieme_A
print("Differenza (B - A):", differenza_B_A)
