'''
Calcolo prezzo finale: dimostra come combinare parametri con valori predefiniti 
(sconto=0, tassa=0.22), *args per costi variabili e **kwargs per opzioni aggiuntive. 
'''
# Funzione per calcolare il prezzo finale con sconto e tasse
def calcola_prezzo_finale(prezzo_base, sconto=0, tassa=0.22, *extra_costi, **opzioni):
    """
    Calcola il prezzo finale di un prodotto
    
    Args:
        prezzo_base: prezzo base del prodotto
        sconto: percentuale di sconto (default 0)
        tassa: percentuale di tassa (default 22%)
        *extra_costi: costi aggiuntivi variabili
        **opzioni: opzioni aggiuntive (spedizione, assicurazione, etc.)
    """
