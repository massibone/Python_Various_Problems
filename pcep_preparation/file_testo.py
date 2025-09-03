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

def analizza_dati(dati):
    statistiche = {}
    for linea in dati:
        linea = linea.strip()
        if linea:
            try:
                data_str, valore_str = linea.split(',')
                data = datetime.datetime.strptime(data_str, '%Y-%m-%d')
                valore = float(valore_str)
                if data not in statistiche:
                    statistiche[data] = []
                statistiche[data].append(valore)
            except ValueError as e:
                print(f"Errore nella riga: {linea}. Errore: {e}")
    return statistiche 
