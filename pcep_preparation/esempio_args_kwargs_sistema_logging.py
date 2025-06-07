
#Sistema di logging personalizzabile

def log_messaggio(messaggio, livello="INFO", timestamp=True, *tag, **metadata):
    """
    Sistema di logging con parametri flessibili
    
    Args:
        messaggio: il messaggio da loggare
        livello: livello di log (default "INFO")
        timestamp: se includere il timestamp (default True)
        *tag: tag aggiuntivi per categorizzare il log
        **metadata: metadati aggiuntivi (utente, IP, etc.)
    """
 import datetime
    
    log_parts = []
    
    # Aggiungi timestamp se richiesto
    if timestamp:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_parts.append(f"[{now}]")
    
    # Aggiungi livello
    log_parts.append(f"[{livello}]")
    
    # Aggiungi tag se presenti
    if tag:
        tags_str = " ".join(f"#{t}" for t in tag)
        log_parts.append(f"[{tags_str}]")
    
    # Aggiungi messaggio
    log_parts.append(messaggio)
    
    # Aggiungi metadata se presenti
    if metadata:
        meta_str = " | ".join(f"{k}={v}" for k, v in metadata.items())
        log_parts.append(f"({meta_str})")
    
    print(" ".join(log_parts))
# Test dell'esempio 2
print("=== ESEMPIO 2: Sistema di logging ===")
log_messaggio("Applicazione avviata")
log_messaggio("Errore nella connessione", "ERROR", True, "database", "connection")
log_messaggio("Login effettuato", "INFO", False, "auth", "security", 
              utente="mario.rossi", ip="192.168.1.10", sessione="abc123")
print()
