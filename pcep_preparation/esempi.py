'''
Esempio di script Python che utilizza vari moduli standard come 
os, sys, math, e datetime per eseguire diverse operazioni. 
'''

import os
import sys
import math
import datetime

def esegui_operazioni_os():
    print("Esempio os:")
    print("Directory corrente:", os.getcwd())

    # Crea una nuova directory
    nuova_dir = "nuova_directory"
    if not os.path.exists(nuova_dir):
        os.mkdir(nuova_dir)
        print(f"Directory '{nuova_dir}' creata con successo.")
    else:
        print(f"La directory '{nuova_dir}' esiste già.")

    # Cambia directory
    os.chdir(nuova_dir)
    print("Lista dei file e delle directory nella directory corrente:", os.listdir())

    # Operazione di ritorno alla directory precedente
    os.chdir("..")

def esegui_operazioni_sys():
    print("\nEsempio sys:")
    print("Lista degli argomenti della riga di comando:", sys.argv)
    print("Piattaforma su cui è in esecuzione il programma:", sys.platform)
    print("Versione di Python in uso:", sys.version)
    # sys.exit(0) rimosso per continuare l'esecuzione del codice
