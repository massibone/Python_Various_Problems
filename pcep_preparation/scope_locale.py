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


def leggi_contatore():
    """Accede alla variabile globale senza modificarla"""
    # Non serve 'global' se leggiamo soltanto
    print(f"App: {nome_app}")
    print(f"Valore attuale del contatore: {contatore_globale}")
    
    # Questa è una variabile locale con lo stesso nome
    contatore_globale = 999  # Questa è LOCALE, non modifica quella globale
    print(f"Contatore locale nella funzione: {contatore_globale}")
def esempio_scope_locale():
    """Dimostra il comportamento delle variabili locali"""
    x = 10  # Variabile locale
