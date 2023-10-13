my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

mi da come risultato 4 se metto i+1 mi da 5
------------------------------------------------------
for number in giocati:
    if number in estratti:
        hits += 1

print(hits)
'''
stampa quanti numeri sono usciti da estratti su quelli giocati
'''
