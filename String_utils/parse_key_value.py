def parse_key_value(text):
    """
    Estrae coppie chiave=valore da un testo multilinea.

    Args:
        text (str): Testo multilinea contenente coppie chiave=valore, una per riga.

    Returns:
        dict: Dizionario con chiavi e valori estratti come stringhe.
    """
    result = {}
    lines = text.splitlines()
    for line in lines:
        # Ignora righe vuote o senza '='
        if '=' not in line:
            continue
        key, value = line.split('=', 1)  # split solo alla prima occorrenza di '='
        key = key.strip()
        value = value.strip()
        result[key] = value
    return result

# Esempio d'uso
text = "name=Marco\nage=50"
parsed = parse_key_value(text)
print(parsed)  # Output: {'name': 'Marco', 'age': '50'}

