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
    
    def funzione_interna():
        x = 20  # Questa è una nuova variabile locale
        print(f"x dentro funzione_interna: {x}")
    
    funzione_interna()
    print(f"x nella funzione esterna: {x}")  # Rimane 10

# Test dell'esempio 1
print("=== ESEMPIO 1: Scope globale e locale ===")
print(f"Contatore iniziale: {contatore_globale}")
incrementa_contatore()
incrementa_contatore()
leggi_contatore()
print(f"Contatore dopo leggi_contatore(): {contatore_globale}")  # Rimane invariato
esempio_scope_locale()
print()

# Esempio Sistema di configurazione con nonlocal
def crea_configuratore():
    """Factory function che dimostra l'uso di nonlocal"""
    # Variabili della funzione esterna (enclosing scope)
    configurazione = {
        "debug": False,
        "max_connessioni": 100,
        "timeout": 30
    }
    livello_log = "INFO"
    
 def get_config(chiave=None):
        """Accede alla configurazione senza modificarla"""
        if chiave:
            return configurazione.get(chiave)
        return configurazione.copy()
    
