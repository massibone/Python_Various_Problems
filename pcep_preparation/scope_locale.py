# Gestione di un contatore globale con scope locale e globale
contatore_globale = 0  # Variabile globale
nome_app = "Sistema Contatori"  # Variabile globale


def incrementa_contatore():
    """Dimostra l'uso di variabili globali e locali"""
    global contatore_globale  # Dichiara che vogliamo modificare la variabile globale
    
    # Variabile locale
    messaggio = "Incrementando contatore..."  # Locale alla funzione
    print(messaggio)
    
    # Modifica la variabile globale
    contatore_globale += 1
    print(f"Contatore globale: {contatore_globale}")
