'''
Apri un file, leggi le righe e chiudilo correttamente.
'''

with open('file.txt', 'r') as f:
    for line in f:
        try:
            # Processa la linea
        except ValueError:
            print("Errore nella linea:", line)
    else:
        print("File elaborato correttamente.")
finally:
    f.close()
