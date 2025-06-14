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

    # Applica sconto
    prezzo_scontato = prezzo_base * (1 - sconto)
    
    # Aggiungi costi extra
    costi_extra = sum(extra_costi)
    
    # Aggiungi opzioni a pagamento
    costi_opzioni = sum(opzioni.values())
    
    # Calcola prezzo finale con tasse
    prezzo_finale = (prezzo_scontato + costi_extra + costi_opzioni) * (1 + tassa)
    
    return round(prezzo_finale, 2)
# Test dell'esempio 1
print("=== ESEMPIO 1: Calcolo prezzo finale ===")
print(f"Prezzo base: {calcola_prezzo_finale(100)}")
print(f"Con sconto 10%: {calcola_prezzo_finale(100, 0.1)}")
print(f"Con sconto e costi extra: {calcola_prezzo_finale(100, 0.1, 0.22, 15, 8)}")
print(f"Completo: {calcola_prezzo_finale(100, 0.1, 0.22, 15, 8, spedizione=12, assicurazione=5)}")
print()
