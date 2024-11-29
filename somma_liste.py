'''
Scrivere un programma che, 
date due liste di interi di uguale lunghezza ne crei una che contenga la somma di ogni elemento, 
indice per indice (quindi l'i-esimo elemento della lista somma è 
l'addizione fra l'i-esimo elemento della prima lista e della seconda)
'''

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l_sum = []

for i in range(len(l1)):
    l_sum.append(l1[i] + l2[i])

print(l_sum)
