"Ecco uno script che legge un file di testo, analizza i dati e restituisce statistiche 
data,valore
2022-01-01,10.5
2022-01-02,12.3
2022-01-03,11.7
"
import datetime

def leggi_file(nome_file):
  try:
    with open(nome_file, 'r') as file:
    dati = file.readlines()
    return dati
  except FileNotFoundError:
    print("Il file non esiste")
    return None
