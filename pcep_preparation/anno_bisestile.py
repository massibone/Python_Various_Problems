def e_bisestile(anno):
  
  """Determina se un anno è bisestile.

  Args:
    anno: L'anno da verificare.

  Returns:
    True se l'anno è bisestile, False altrimenti.
  """

  return anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0)

# Imposta l'intervallo di anni
anno_iniziale = 1900
anno_finale = 2024  # Puoi modificare questo valore per un intervallo diverso

print("Anni bisestili dal", anno_iniziale, "al", anno_finale, ":")
for anno in range(anno_iniziale, anno_finale + 1):
  if e_bisestile(anno):
    print(anno)

