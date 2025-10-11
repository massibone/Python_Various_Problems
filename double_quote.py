# La funzione validate_account_number prende un numero di account come input e applica le regole descritte (raddoppiare ogni altra cifra, sommare le cifre a due caratteri, ecc.) per validare il numero
def validate_account_number(account_number):
    """
    Valida un numero di account secondo le regole fornite:
    1. Raddoppia ogni altra cifra (partendo dalla prima).
    2. Somma le cifre dei numeri a due caratteri (es. 18 -> 1 + 8 = 9).
    3. Somma tutte le cifre risultanti.

    Args:
        account_number (str): Numero di account da validare (es. "7992739871x").

    Returns:
        int: Somma finale delle cifre.
    """
    # Rimuovi eventuali caratteri non numerici (tranne l'ultimo se è 'x')
    cleaned = [c for c in account_number[:-1] if c.isdigit()]
    check_char = account_number[-1].lower()

    # Applica il raddoppio ogni altra cifra
    doubled = []
    for i, digit in enumerate(cleaned):
        num = int(digit)
        if i % 2 == 0:  # Raddoppia ogni altra cifra (partendo dalla prima)
            doubled.append(num * 2)
        else:
            doubled.append(num)

    # Somma le cifre dei numeri a due caratteri
    sum_digits = []
    for num in doubled:
        if num >= 10:
            sum_digits.append(sum(int(d) for d in str(num)))
        else:
            sum_digits.append(num)

    # Calcola la somma totale
    total = sum(sum_digits)

    return total

# Esempio di utilizzo:
account_number = "7992739871x"
result = validate_account_number(account_number)
print(f"Somma finale: {result}")
