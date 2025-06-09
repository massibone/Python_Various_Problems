# Builder per query SQL dinamiche
def costruisci_query(tabella, operazione="SELECT", colonne=None, *condizioni, **parametri):
    """
    Costruisce query SQL dinamiche
    
    Args:
        tabella: nome della tabella
        operazione: tipo di operazione (default "SELECT")
        colonne: liste delle colonne (default tutte con *)
        *condizioni: condizioni WHERE multiple
        **parametri: parametri aggiuntivi (LIMIT, ORDER BY, etc.)
    """
    query_parts = []
    
