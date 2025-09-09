'''
L'operatore di concatenazione (+) funziona solo tra stringhe. 
Se tenti di concatenare una stringa con un numero intero (int) o un altro tipo di dato non stringa, 
Python genera un errore (TypeError):

numero = 100
print('Il risultato è: ' + numero)  # ❌ ERRORE!
Per far funzionare l'esempio sopra con la concatenazione, 
devi esplicitamente convertire il numero in stringa usando str():

print('Il risultato è: ' + str(numero)) # ✅ Funziona, ma è meno pulito

Le f-string non richiedono questa conversione manuale. 
Le f-string convertono automaticamente qualsiasi tipo di dato in stringa al momento della formattazione:


numero = 100
print(f'Il risultato è: {numero}')  # ✅ Funziona senza str()

'''
