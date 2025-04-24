'''
Creare un elenco di studenti con nome, materia, e voto, ordinare gli studenti per voto decrescente, e stampare una tabella con posizione, nome, materia, e voto.
Esempio che combinerà zip(), enumerate(), e sorted() con una funzione personalizzata per il key, in un unico programma
'''

# Dati di esempio
nomi = ["Alice", "Bob", "Charlie", "Diana"]
materie = ["Matematica", "Inglese", "Storia", "Scienze"]
voti = [88, 92, 75, 95]

# 1. Usare `zip()` per combinare le liste in una lista di tuple (nome, materia, voto)
studenti_tuple = list(zip(nomi, materie, voti))

# 2. Convertire in una lista di dizionari per maggiore chiarezza
studenti = [
    {"nome": nome, "materia": materia, "voto": voto}
    for nome, materia, voto in studenti_tuple
]

# 3. Ordinare gli studenti per voto decrescente (da più alto a più basso)
studenti_ordinati = sorted(
    studenti, 
    key=lambda studente: studente["voto"],  # Chiave di ordinamento
    reverse=True                           # Ordine decrescente
)

# 4. Stampa con `enumerate()` per aggiungere la posizione (rank)
print("Classifica degli studenti:")
print("Posizione | Nome    | Materia    | Voto")
print("----------------------------------------")

for posizione, studente in enumerate(studenti_ordinati, start=1):
    print(f"{posizione:8} | {studente['nome']:8} | {studente['materia']:10} | {studente['voto']:3}")
