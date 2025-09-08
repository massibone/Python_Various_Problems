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

def calcola_statistiche(statistiche):
  media = {}
  minimo = {}
  massimo = {}
  for data, valori in statistiche.items():
    media[data] = sum(valori) / len(valori)
    minimo[data] = min(valori)
    massimo[data] = max(valori)
    return media, minimo, massimo

def calcola_differenza_date(data1, data2):
  return (data2 - data1).days

def stampa_statistiche(media, minimo, massimo, dati):
  print("Statistiche:")
    for data, valore in media.items():
      print(f"Data: {data.date()}, Media: {valore:.2f}")
      print("\nMinimi:")
    for data, valore in minimo.items():
    print(f"Data: {data.date()}, Minimo: {valore:.2f}")
    print("\nMassimi:")
    for data, valore in massimo.items():
    print(f"Data: {data.date()}, Massimo: {valore:.2f}")
    print("\nDifferenza tra le date:")
    for i in range(len(dati) - 1):
    data1 = datetime.datetime.strptime(dati[i].split(',')[0], '%Y-%m-%d')
    data2 = datetime.datetime.strptime(dati[i + 1].split(',')[0], '%Y-%m-%d')
    print(f"Differenza tra {data1.date()} e {data2.date()}: {calcola_differenza_date(data1, data2)} giorni")
