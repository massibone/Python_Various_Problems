e# Gestione di un contatore globale con scope locale e globale
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

# Esempio 1
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
    
    def set_config(chiave, valore):
        """Modifica la configurazione usando nonlocal"""
        nonlocal configurazione  # Necessario per modificare
        configurazione[chiave] = valore
        print(f"Configurazione aggiornata: {chiave} = {valore}")
    
    def cambia_livello_log(nuovo_livello):
        """Modifica il livello di log usando nonlocal"""
        nonlocal livello_log  # Senza questo, creerebbe una variabile locale
        vecchio_livello = livello_log
        livello_log = nuovo_livello
        print(f"Livello log cambiato da {vecchio_livello} a {livello_log}")
    
    def get_livello_log():
        """Legge il livello di log corrente"""
        return livello_log
    
    def reset_config():
        """Reset completo della configurazione"""
        nonlocal configurazione, livello_log
        configurazione = {
            "debug": False,
            "max_connessioni": 100,
            "timeout": 30
        }
        livello_log = "INFO"
        print("Configurazione resettata ai valori predefiniti")
    
    # Restituisce un dizionario con tutte le funzioni
    return {
        "get": get_config,
        "set": set_config,
        "log_level": get_livello_log,
        "set_log_level": cambia_livello_log,
        "reset": reset_config
    }

# Test dell'esempio 2
print("=== ESEMPIO 2: Nonlocal con configuratore ===")
config = crea_configuratore()
print("Configurazione iniziale:", config["get"]())
print("Livello log iniziale:", config["log_level"]())

config["set"]("debug", True)
config["set"]("max_connessioni", 200)
config["set_log_level"]("DEBUG")

print("Dopo le modifiche:")
print("Debug mode:", config["get"]("debug"))
print("Max connessioni:", config["get"]("max_connessioni"))
print("Livello log:", config["log_level"]())

config["reset"]()
print("Dopo reset:", config["get"]())
print()

# Esempio 3: Simulatore di stack di chiamate con tutti i tipi di scope
stack_chiamate = []  # Variabile globale per tracciare le chiamate


def crea_calcolatrice():
    """Esempio complesso che combina tutti i tipi di scope"""
    # Variabili dell'enclosing scope
    storia_operazioni = []
    precisione = 2
def traccia_chiamata(nome_funzione):
    """Aggiunge una chiamata al stack globale"""
    global stack_chiamate
    stack_chiamate.append(nome_funzione)
    print(f"→ Chiamata: {nome_funzione}")


        # Nested function che usa tutti i tipi di scope
        def esegui_operazione():
            nonlocal risultato, operazione_valida  # Variabili della funzione parent
            global stack_chiamate  # Variabile globale
            
            # Variabili locali di questa funzione
            messaggio_debug = f"Eseguendo {operazione}"
            
            if operazione == "+":
                risultato = a + b
            elif operazione == "-":
                risultato = a - b
            elif operazione == "*":
                risultato = a * b
            elif operazione == "/":
                if b != 0:
                    risultato = a / b
                else:
                    risultato = float('inf')
                    operazione_valida = False
            else:
                operazione_valida = False
           
            # Usa la variabile dell'enclosing scope (precisione)
            if operazione_valida and isinstance(risultato, float):
                risultato = round(risultato, precisione)
            
            # Modifica variabile nonlocal della funzione parent
            if operazione_valida:
                storia_operazioni.append(f"{a} {operazione} {b} = {risultato}")
            
            print(f"  {messaggio_debug}: {'OK' if operazione_valida else 'ERRORE'}")
        
        esegui_operazione()
        
        return risultato if operazione_valida else None
    
def mostra_storia():
        """Mostra la storia delle operazioni"""
        nonlocal storia_operazioni
        print(f"Storia operazioni (precisione: {precisione} decimali):")
        for i, op in enumerate(storia_operazioni, 1):
            print(f"  {i}. {op}")
    
def cambia_precisione(nuova_precisione):
        """Cambia la precisione dei calcoli"""
        nonlocal precisione
        vecchia = precisione
        precisione = nuova_precisione
        print(f"Precisione cambiata da {vecchia} a {precisione} decimali")


    def mostra_stack():
        """Mostra lo stack delle chiamate globale"""
        global stack_chiamate
        print("Stack chiamate globale:")
        for chiamata in stack_chiamate:
            print(f"  - {chiamata}")
    
    return {
        "calcola": calcola,
        "storia": mostra_storia,
        "precisione": cambia_precisione,
        "stack": mostra_stack
    }  
