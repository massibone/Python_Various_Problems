def check_gregorian_leap_year(year: int) -> str:
    """
    Restituisce una stringa che descrive se 'year' è:
    - "Leap year" (anno bisestile),
    - "Common year" (anno comune),
    - "Not within the Gregorian calendar period" (se < 1582).
    """
    if year < 1582:
        return "Not within the Gregorian calendar period"

    # Regole del calendario gregoriano
    if year % 4 != 0:
        return "Common year"
    if year % 100 != 0:
        return "Leap year"
    if year % 400 != 0:
        return "Common year"
    return "Leap year"


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: ").strip())
    except ValueError:
        print("Input non valido: inserisci un numero intero.")
    else:
        print(check_gregorian_leap_year(year))

