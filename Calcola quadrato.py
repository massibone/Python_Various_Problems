'''
Calcola quadrato. Es 25**2= 5**2+(2+1)**2=925
'''
def calcola_quadrato(numero):
    cifre = [int(digito) for digito in str(numero)]
    primo_digito = cifre[0]
    secondo_digito = cifre[1] if len(cifre) > 1 else 0

    risultato = primo_digito**2 + (secondo_digito + 1)**2
    return f"{numero}**2 = {primo_digito}**2 + ({secondo_digito} + 1)**2 = {risultato}"

for num in range(10, 100):
    print(calcola_quadrato(num))

