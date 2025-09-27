class ValoreInvalidoError(Exception):
    pass
    
def calcola_media(valori):
    # Controlla se la lista è vuota (caso in cui si vuole sollevare l'eccezione)
    if len(valori) == 0:
        raise ValoreInvalidoError("Lista di valori vuota")
    
    # Se la lista NON è vuota, il codice prosegue qui
    media = sum(valori) / len(valori)
    return media

# --- Blocco di Test ---
try:
    valori = [] # Lista di valori vuota per testare l'errore
    media = calcola_media(valori)
    print("La media è:", media)
except ValoreInvalidoError as e:
    print("Errore:", e)

# Esempio per testare il funzionamento corretto:
try:
    valori_ok = [10, 20, 30]
    media_ok = calcola_media(valori_ok)
    print(f"La media è: {media_ok}")
except ValoreInvalidoError as e:
    print("Errore:", e)
