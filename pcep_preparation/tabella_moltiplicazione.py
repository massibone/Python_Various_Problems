'''
Crea:
1   2   3   4   5   6   7   8   9   10
2   4   6   8   10  12  14  16  18  20
3   6   9   12  15  18  21  24  27  30
4   8   12  16  20  24  28  32  36  40
5   10  15  20  25  30  35  40  45  50
6   12  18  24  30  36  42  48  54  60
7   14  21  28  35  42  49  56  63  70
8   16  24  32  40  48  56  64  72  80
9   18  27  36  45  54  63  72  81  90
10  20  30  40  50  60  70  80  90  100
'''
for i in range(1, 11):
    for j in range(1, 11):
        prodotto = i * j
        print(prodotto, end='\t')
    print()

# Definisci la dimensione della tabella di moltiplicazione
dimensione = 10

# Stampa l'intestazione della tabella
print("   |", end="")
for i in range(1, dimensione + 1):
    print(f"{i:4}", end="")
print()
print("-" * (dimensione * 5 + 3))

# Stampa la tabella di moltiplicazione
for i in range(1, dimensione + 1):
    print(f"{i:3} |", end="")
    for j in range(1, dimensione + 1):
        print(f"{i * j:4}", end="")
    print()
