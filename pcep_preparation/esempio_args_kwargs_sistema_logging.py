
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
