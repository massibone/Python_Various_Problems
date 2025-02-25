'''
Esempio:

Supponiamo di voler calcolare il punteggio in una partita di basket, considerando punti segnati, assist e palle perse. Potremmo definire le seguenti regole:

1 punto per ogni canestro segnato.
0.5 punti per ogni assist.
-0.25 punti per ogni palla persa.
Bonus di 2 punti se il giocatore ha segnato più di 20 punti.
'''
def calcola_punteggio_basket(punti, assist, palle_perse):
  """Calcola il punteggio di un giocatore di basket.

  Args:
    punti: Numero di punti segnati.
    assist: Numero di assist.
    palle_perse: Numero di palle perse.

  Returns:
    Il punteggio totale del giocatore.
  """

  punteggio_base = punti + (assist * 0.5) - (palle_perse * 0.25)

  if punti > 20:
    punteggio_base += 2

  return punteggio_base

# Esempio d'uso:
giocatore1_punti = 25
giocatore1_assist = 5
giocatore1_palle_perse = 3

punteggio_giocatore1 = calcola_punteggio_basket(giocatore1_punti, giocatore1_assist, giocatore1_palle_perse)
print("Il punteggio del giocatore 1 è:", punteggio_giocatore1)
