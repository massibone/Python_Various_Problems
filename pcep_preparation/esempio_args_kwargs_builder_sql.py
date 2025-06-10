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
    
    # Parte principale della query
    if operazione.upper() == "SELECT":
        cols = ", ".join(colonne) if colonne else "*"
        query_parts.append(f"SELECT {cols}")
        query_parts.append(f"FROM {tabella}")
    elif operazione.upper() == "DELETE":
        query_parts.append(f"DELETE FROM {tabella}")
    elif operazione.upper() == "UPDATE":
        query_parts.append(f"UPDATE {tabella}")
    

    # Aggiungi condizioni WHERE
    if condizioni:
        where_clause = " AND ".join(condizioni)
        query_parts.append(f"WHERE {where_clause}")
    
    # Aggiungi parametri aggiuntivi
    if "order_by" in parametri:
        query_parts.append(f"ORDER BY {parametri['order_by']}")
    
    if "limit" in parametri:
        query_parts.append(f"LIMIT {parametri['limit']}")
    
    if "group_by" in parametri:
        query_parts.append(f"GROUP BY {parametri['group_by']}")
    
    return " ".join(query_parts)
