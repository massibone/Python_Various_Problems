'''
Analizza un testo e calcola la frequenza di ogni parola.
Per ordinare i risultati per frequenza:
for parola, count in sorted(frequenze.items(), key=lambda x: -x[1]):
    print(f"{parola}: {count}")
'''

testo = """Ciao mondo! Ciao Python. Python è fantastico. 
           Mi piace programmare in Python, ma c'è di meglio."""

# Passo 1: Pre-elaborazione del testo
testo = testo.lower()  # Tutto minuscolo
testo = testo.replace("\n", " ")  # Rimuovi a capo

# Rimuovi punteggiatura (es. !, ., ", etc.)
import string
testo_pulito = testo.translate(str.maketrans("", "", string.punctuation))

# Dividi in parole
parole = testo_pulito.split()

# Passo 2: Conteggio frequenza
frequenze = {}
for parola in parole:
    if parola in frequenze:
        frequenze[parola] += 1
    else:
        frequenze[parola] = 1
