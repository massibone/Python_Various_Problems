'''
Trova tutte le coppie di numeri primi minori di 100
'''
def primi_coppie(n):
    primi = []
    for i in range(2, n):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            primi.append(i)
    return [(x, y) for x in primi for y in primi if x < y]
