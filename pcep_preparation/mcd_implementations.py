import math
import time
from functools import reduce

def mcd_euclide_iterativo(a, b):
    """
    Calcola il MCD usando l'algoritmo di Euclide (versione iterativa)
    
    Args:
        a, b: due numeri interi
    
    Returns:
        int: il massimo comune divisore di a e b
    """
    # Gestisce numeri negativi
    a, b = abs(a), abs(b)
    
    # Assicura che a >= b per efficienza
    if a < b:
        a, b = b, a
    
    while b != 0:
        resto = a % b
        a, b = b, resto
    
    return a


def mcd_euclide_ricorsivo(a, b):
    """
    Calcola il MCD usando l'algoritmo di Euclide (versione ricorsiva)
    
    Args:
        a, b: due numeri interi
    
    Returns:
        int: il massimo comune divisore di a e b
    """
    # Gestisce numeri negativi
    a, b = abs(a), abs(b)
    
    # Caso base
    if b == 0:
        return a
    
    # Chiamata ricorsiva
    return mcd_euclide_ricorsivo(b, a % b)


def mcd_sottrazione(a, b):
    """
    Calcola il MCD usando il metodo della sottrazione ripetuta
    (meno efficiente ma più intuitivo)
    
    Args:
        a, b: due numeri interi
    
    Returns:
        int: il massimo comune divisore di a e b
    """
    # Gestisce numeri negativi
    a, b = abs(a), abs(b)
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    return a


def mcd_fattorizzazione(a, b):
    """
    Calcola il MCD trovando tutti i divisori comuni
    (metodo didattico, inefficiente per numeri grandi)
    
    Args:
        a, b: due numeri interi
    
    Returns:
        int: il massimo comune divisore di a e b
    """
    a, b = abs(a), abs(b)
    
    if a == 0 or b == 0:
        return max(a, b)
    
    # Trova tutti i divisori del numero più piccolo
    min_num = min(a, b)
    divisori_comuni = []
    
    for i in range(1, min_num + 1):
        if a % i == 0 and b % i == 0:
            divisori_comuni.append(i)
    
    return max(divisori_comuni) if divisori_comuni else 1


def mcd_multipli(a, b):
    """
    Calcola il MCD per più di due numeri
    
    Args:
        a, b: primi due numeri
        *args: numeri aggiuntivi (opzionali)
    
    Returns:
        int: il massimo comune divisore di tutti i numeri
    """
    risultato = mcd_euclide_iterativo(a, b)
    return risultato


def mcd_lista(numeri):
    """
    Calcola il MCD di una lista di numeri
    
    Args:
        numeri: lista di numeri interi
    
    Returns:
        int: il massimo comune divisore di tutti i numeri
    """
    if not numeri:
        return 0
    if len(numeri) == 1:
        return abs(numeri[0])
    
    # Usa reduce per applicare mcd_euclide_iterativo a tutti i numeri
    return reduce(mcd_euclide_iterativo, [abs(n) for n in numeri])


def mcd_esteso(a, b):
    """
    Algoritmo di Euclide esteso: trova MCD e i coefficienti di Bézout
    Trova x, y tali che ax + by = mcd(a, b)
    
    Args:
        a, b: due numeri interi
    
    Returns:
        tuple: (mcd, x, y) dove ax + by = mcd
    """
    a_orig, b_orig = a, b
    a, b = abs(a), abs(b)
    
    if b == 0:
        return a, 1, 0
    
    # Coefficienti per l'identità di Bézout
    x1, x2 = 1, 0
    y1, y2 = 0, 1
    
    while b != 0:
        quoziente = a // b
        
        # Aggiorna i valori
        a, b = b, a % b
        x1, x2 = x2, x1 - quoziente * x2
        y1, y2 = y2, y1 - quoziente * y2
    
    # Gestisce segni per numeri negativi originali
    if a_orig < 0:
        x1 = -x1
    if b_orig < 0:
        y1 = -y1
    
    return a, x1, y1


def benchmark_mcd(a, b, iterazioni=10000):
    """
    Confronta le prestazioni dei diversi algoritmi di MCD
    
    Args:
        a, b: numeri da testare
        iterazioni: numero di iterazioni per il benchmark
    """
    algoritmi = [
        ("Euclide Iterativo", mcd_euclide_iterativo),
        ("Euclide Ricorsivo", mcd_euclide_ricorsivo),
        ("Sottrazione", mcd_sottrazione),
        ("Fattorizzazione", mcd_fattorizzazione),
        ("Built-in math.gcd", math.gcd)
    ]
    
    print(f"Benchmark MCD({a}, {b}) - {iterazioni} iterazioni:")
    print("-" * 60)
    
    for nome, funzione in algoritmi:
        start_time = time.time()
        
        for _ in range(iterazioni):
            risultato = funzione(a, b)
        
        end_time = time.time()
        tempo = (end_time - start_time) * 1000  # in millisecondi
        
        print(f"{nome:20}: {risultato:6} | {tempo:8.3f} ms")


def test_mcd():
    """Test completo delle funzioni MCD"""
    print("=== TEST DELLE FUNZIONI MCD ===\n")
    
    # Test casi base
    test_cases = [
        (48, 18),      # Caso classico
        (100, 25),     # Uno divide l'altro
        (17, 13),      # Numeri primi tra loro
        (0, 5),        # Uno è zero
        (-12, 8),      # Numeri negativi
        (1071, 462),   # Numeri più grandi
    ]
    
    for a, b in test_cases:
        print(f"MCD({a}, {b}):")
        print(f"  Iterativo:     {mcd_euclide_iterativo(a, b)}")
        print(f"  Ricorsivo:     {mcd_euclide_ricorsivo(a, b)}")
        print(f"  Sottrazione:   {mcd_sottrazione(a, b)}")
        print(f"  Fattorizzazione: {mcd_fattorizzazione(a, b)}")
        print(f"  Built-in:      {math.gcd(a, b)}")
        print()
    
    # Test MCD esteso
    print("=== TEST MCD ESTESO ===")
    a, b = 240, 46
    mcd, x, y = mcd_esteso(a, b)
    print(f"MCD esteso di {a} e {b}:")
    print(f"MCD = {mcd}")
    print(f"Coefficienti di Bézout: x={x}, y={y}")
    print(f"Verifica: {a}×{x} + {b}×{y} = {a*x + b*y}")
    print()
    
    # Test MCD di più numeri
    print("=== TEST MCD DI PIÙ NUMERI ===")
    numeri = [48, 18, 24, 12]
    risultato = mcd_lista(numeri)
    print(f"MCD di {numeri} = {risultato}")
    print()
    
    # Benchmark
    print("=== BENCHMARK ===")
    benchmark_mcd(1071, 462, 1000)


# Esempi di utilizzo pratico
def esempi_pratici():
    """Esempi di applicazioni pratiche del MCD"""
    print("\n=== ESEMPI PRATICI ===\n")
    
    # 1. Semplificazione di frazioni
    print("1. Semplificazione di frazioni:")
    numeratore, denominatore = 48, 18
    divisore = mcd_euclide_iterativo(numeratore, denominatore)
    print(f"   {numeratore}/{denominatore} = {numeratore//divisore}/{denominatore//divisore}")
    print()
    
    # 2. Distribuzione equa
    print("2. Distribuzione equa di oggetti:")
    mele, arance = 24, 18
    gruppi = mcd_euclide_iterativo(mele, arance)
    print(f"   {mele} mele e {arance} arance possono essere divise in {gruppi} gruppi")
    print(f"   Ogni gruppo avrà {mele//gruppi} mele e {arance//gruppi} arance")
    print()
    
    # 3. Frequenza di eventi
    print("3. Frequenza di eventi periodici:")
    evento_a, evento_b = 12, 8  # ogni 12 e 8 giorni
    prossimo_insieme = (evento_a * evento_b) // mcd_euclide_iterativo(evento_a, evento_b)
    print(f"   Eventi ogni {evento_a} e {evento_b} giorni si ripeteranno insieme ogni {prossimo_insieme} giorni")


if __name__ == "__main__":
    test_mcd()
    esempi_pratici()