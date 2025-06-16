# Gestione di un contatore globale con scope locale e globale
contatore_globale = 0  # Variabile globale
nome_app = "Sistema Contatori"  # Variabile globale


def incrementa_contatore():
    """Dimostra l'uso di variabili globali e locali"""
    global contatore_globale  # Dichiara che vogliamo modificare la variabile globale
