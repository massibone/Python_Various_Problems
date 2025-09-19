class FormatoFileNonSupportatoError(Exception):
  pass

def leggi_file(nome_file):
  if not nome_file.endswith(".txt"):
    raise FormatoFileNonSupportatoError("Solo file di testo sono supportati")
with open(nome_file, "r") as file:
contenuto = file.read()
return contenuto

try:
nome_file = "esempio.pdf"
contenuto = leggi_file(nome_file)
print("Contenuto del file:", contenuto)
except FormatoFileNonSupportatoError as e:
print("Errore:", e)
