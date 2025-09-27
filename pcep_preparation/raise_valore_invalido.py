class ValoreInvalidoError(Exception):
  pass
  
def calcola_media(valori):
  if len(valori) == 0:
    raise ValoreInvalidoError("Lista di valori vuota")
    media = sum(valori) / len(valori)
    return media
