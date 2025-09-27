class ValoreInvalidoError(Exception):
  pass
  
def calcola_media(valori):
  if len(valori) == 0:
    raise ValoreInvalidoError("Lista di valori vuota")
    media = sum(valori) / len(valori)
    return media

try:
  valori = []
  media = calcola_media(valori)
  print("La media è:", media)
  except ValoreInvalidoError as e:
  print("Errore:", e)
