from functools import reduce
import math

# =============================================================================
# ESEMPIO 1: ELABORAZIONE DATI VENDITE CON LAMBDA, MAP E FILTER
# =============================================================================

def esempio_vendite():
    """Elaborazione dati di vendita usando lambda, map e filter"""
    print("=== ESEMPIO 1: ELABORAZIONE DATI VENDITE ===\n")
    
    # Dataset di vendite: (prodotto, quantità, prezzo_unitario, categoria)
    vendite = [
        ("Laptop", 5, 800.0, "elettronica"),
        ("Mouse", 25, 15.5, "elettronica"),
        ("Scrivania", 3, 250.0, "mobili"),
        ("Smartphone", 12, 600.0, "elettronica"),
        ("Sedia", 8, 120.0, "mobili"),
        ("Tablet", 7, 300.0, "elettronica"),
        ("Libreria", 2, 180.0, "mobili"),
        ("Cuffie", 20, 45.0, "elettronica"),
    ]
    
    print("Dati originali:")
    for vendita in vendite:
        print(f"  {vendita}")
    print()
    
    # 1. MAP: Calcola il totale per ogni vendita
    print("1. Calcolo totali con map() e lambda:")
    totali = list(map(lambda x: (x[0], x[1] * x[2]), vendite))
    for prodotto, totale in totali:
        print(f"  {prodotto}: €{totale:.2f}")
    print()
    
    # 2. FILTER: Filtra solo prodotti elettronici
    print("2. Filtro prodotti elettronici con filter() e lambda:")
    elettronica = list(filter(lambda x: x[3] == "elettronica", vendite))
    for prodotto in elettronica:
        print(f"  {prodotto[0]}: {prodotto[1]} pz × €{prodotto[2]} = €{prodotto[1] * prodotto[2]:.2f}")
    print()
    
    # 3. Combinazione MAP + FILTER: Vendite elettroniche > €500
    print("3. Combinazione filter + map - Vendite elettroniche > €500:")
    vendite_grandi = list(
        map(lambda x: f"{x[0]}: €{x[1] * x[2]:.2f}", 
            filter(lambda x: x[3] == "elettronica" and x[1] * x[2] > 500, vendite))
    )
    for vendita in vendite_grandi:
        print(f"  {vendita}")
    print()
    
    # 4. REDUCE: Calcola il fatturato totale
    print("4. Calcolo fatturato totale con reduce() e lambda:")
    fatturato_totale = reduce(
        lambda acc, x: acc + (x[1] * x[2]), 
        vendite, 
        0
    )
    print(f"  Fatturato totale: €{fatturato_totale:.2f}")
    print()


# =============================================================================
# ESEMPIO 2: ELABORAZIONE TESTI E STRINGHE
# =============================================================================

def esempio_testi():
    """Elaborazione di testi usando lambda con map e filter"""
    print("=== ESEMPIO 2: ELABORAZIONE TESTI ===\n")
    
    frasi = [
        "Python è un linguaggio potente",
        "Le lambda sono funzioni anonime",
        "Map applica una funzione a tutti gli elementi",
        "Filter seleziona elementi in base a una condizione",
        "Reduce combina tutti gli elementi in un singolo valore"
    ]
    
    print("Frasi originali:")
    for i, frase in enumerate(frasi, 1):
        print(f"  {i}. {frase}")
    print()
    
    # 1. MAP: Converti tutto in maiuscolo e conta caratteri
    print("1. Conversione maiuscolo e conteggio caratteri:")
    info_frasi = list(map(lambda x: (x.upper(), len(x)), frasi))
    for frase_upper, lunghezza in info_frasi:
        print(f"  [{lunghezza:2} char] {frase_upper}")
    print()
    
    # 2. FILTER: Solo frasi che contengono "funzione" o "elemento"
    print("2. Frasi che contengono 'funzione' o 'elemento':")
    parole_chiave = ["funzione", "elemento"]
    frasi_filtrate = list(filter(
        lambda x: any(parola in x.lower() for parola in parole_chiave), 
        frasi
    ))
    for frase in frasi_filtrate:
        print(f"  • {frase}")
    print()
    
    # 3. MAP: Estrai le prime tre parole di ogni frase
    print("3. Prime tre parole di ogni frase:")
    prime_parole = list(map(lambda x: " ".join(x.split()[:3]) + "...", frasi))
    for frase_breve in prime_parole:
        print(f"  {frase_breve}")
    print()
    
    # 4. Combinazione complessa: Analisi parole
    print("4. Analisi parole (lunghezza > 5 caratteri):")
    parole_lunghe = list(
        map(lambda frase: list(filter(lambda parola: len(parola) > 5, frase.split())), 
            frasi)
    )
    for i, parole in enumerate(parole_lunghe, 1):
        print(f"  Frase {i}: {parole}")
    print()


# =============================================================================
# ESEMPIO 3: ELABORAZIONE DATI NUMERICI E MATEMATICI
# =============================================================================

def esempio_matematico():
    """Operazioni matematiche complesse con lambda"""
    print("=== ESEMPIO 3: ELABORAZIONE MATEMATICA ===\n")
    
    numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 20, 25]
    print(f"Numeri originali: {numeri}\n")
    
    # 1. MAP: Operazioni matematiche multiple
    print("1. Operazioni matematiche con map():")
    
    # Quadrati
    quadrati = list(map(lambda x: x**2, numeri))
    print(f"  Quadrati: {quadrati[:8]}...")
    
    # Radici quadrate arrotondate
    radici = list(map(lambda x: round(math.sqrt(x), 2), numeri))
    print(f"  Radici: {radici[:8]}...")
    
    # Operazione complessa: (x^2 + 1) / 2
    complessa = list(map(lambda x: (x**2 + 1) / 2, numeri))
    print(f"  (x²+1)/2: {complessa[:8]}...")
    print()
    
    # 2. FILTER: Filtri numerici
    print("2. Filtri numerici con filter():")
    
    # Numeri pari
    pari = list(filter(lambda x: x % 2 == 0, numeri))
    print(f"  Pari: {pari}")
    
    # Numeri primi (implementazione semplice)
    def è_primo(n):
        if n < 2:
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    
    primi = list(filter(lambda x: è_primo(x), numeri))
    print(f"  Primi: {primi}")
    
    # Numeri perfetti (somma divisori = numero)
    def è_perfetto(n):
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    perfetti = list(filter(lambda x: è_perfetto(x), numeri))
    print(f"  Perfetti: {perfetti}")
    print()
    
    # 3. REDUCE: Aggregazioni
    print("3. Aggregazioni con reduce():")
    
    # Somma
    somma = reduce(lambda acc, x: acc + x, numeri, 0)
    print(f"  Somma: {somma}")
    
    # Prodotto
    prodotto = reduce(lambda acc, x: acc * x, numeri[:5], 1)  # Solo primi 5
    print(f"  Prodotto (primi 5): {prodotto}")
    
    # Massimo (alternativa a max())
    massimo = reduce(lambda acc, x: acc if acc > x else x, numeri)
    print(f"  Massimo: {massimo}")
    
    # Media usando reduce in modo creativo
    somma_count = reduce(
        lambda acc, x: (acc[0] + x, acc[1] + 1), 
        numeri, 
        (0, 0)
    )
    media = somma_count[0] / somma_count[1]
    print(f"  Media: {media:.2f}")
    print()


# =============================================================================
# ESEMPIO 4: ELABORAZIONE DATI STRUTTURATI (DIZIONARI)
# =============================================================================

def esempio_dizionari():
    """Elaborazione di liste di dizionari con lambda"""
    print("=== ESEMPIO 4: ELABORAZIONE DIZIONARI ===\n")
    
    # Dataset studenti
    studenti = [
        {"nome": "Alice", "età": 22, "voti": [85, 92, 78, 95], "corso": "Informatica"},
        {"nome": "Bob", "età": 21, "voti": [72, 68, 84, 79], "corso": "Matematica"},
        {"nome": "Charlie", "età": 23, "voti": [95, 89, 92, 97], "corso": "Informatica"},
        {"nome": "Diana", "età": 20, "voti": [88, 91, 85, 90], "corso": "Fisica"},
        {"nome": "Eve", "età": 22, "voti": [76, 82, 79, 85], "corso": "Matematica"},
    ]
    
    print("Dati studenti:")
    for studente in studenti:
        print(f"  {studente}")
    print()
    
    # 1. MAP: Calcola media voti per ogni studente
    print("1. Calcolo medie con map():")
    medie = list(map(
        lambda s: {
            "nome": s["nome"], 
            "media": sum(s["voti"]) / len(s["voti"])
        }, 
        studenti
    ))
    for student_media in medie:
        print(f"  {student_media['nome']}: {student_media['media']:.1f}")
    print()
    
    # 2. FILTER: Studenti con media > 85
    print("2. Studenti con media > 85:")
    bravi_studenti = list(filter(
        lambda s: sum(s["voti"]) / len(s["voti"]) > 85, 
        studenti
    ))
    for studente in bravi_studenti:
        media = sum(studente["voti"]) / len(studente["voti"])
        print(f"  {studente['nome']} ({studente['corso']}): {media:.1f}")
    print()
    
    # 3. Combinazione: Studenti di Informatica con voto massimo > 90
    print("3. Studenti Informatica con voto max > 90:")
    informatica_top = list(
        map(lambda s: f"{s['nome']}: max={max(s['voti'])}", 
            filter(lambda s: s["corso"] == "Informatica" and max(s["voti"]) > 90, 
                   studenti))
    )
    for info in informatica_top:
        print(f"  {info}")
    print()
    
    # 4. REDUCE: Statistiche generali
    print("4. Statistiche generali con reduce():")
    
    # Media generale di tutti i voti
    tutti_voti = reduce(lambda acc, s: acc + s["voti"], studenti, [])
    media_generale = sum(tutti_voti) / len(tutti_voti)
    print(f"  Media generale: {media_generale:.2f}")
    
    # Studente con media più alta
    migliore = reduce(
        lambda acc, s: s if sum(s["voti"])/len(s["voti"]) > sum(acc["voti"])/len(acc["voti"]) else acc,
        studenti
    )
    print(f"  Migliore studente: {migliore['nome']} ({sum(migliore['voti'])/len(migliore['voti']):.1f})")
    print()


# =============================================================================
# ESEMPIO 5: LAMBDA ANNIDATE E OPERAZIONI COMPLESSE
# =============================================================================

def esempio_avanzato():
    """Esempi avanzati con lambda annidate e operazioni complesse"""
    print("=== ESEMPIO 5: LAMBDA AVANZATE ===\n")
    
    # Dataset transazioni finanziarie
    transazioni = [
        {"id": 1, "tipo": "entrata", "importo": 1500, "categoria": "stipendio"},
        {"id": 2, "tipo": "uscita", "importo": 800, "categoria": "affitto"},
        {"id": 3, "tipo": "uscita", "importo": 200, "categoria": "spesa"},
        {"id": 4, "tipo": "entrata", "importo": 300, "categoria": "freelance"},
        {"id": 5, "tipo": "uscita", "importo": 150, "categoria": "bollette"},
        {"id": 6, "tipo": "uscita", "importo": 80, "categoria": "spesa"},
        {"id": 7, "tipo": "entrata", "importo": 500, "categoria": "bonus"},
    ]
    
    print("Transazioni:")
    for t in transazioni:
        print(f"  {t}")
    print()
    
    # 1. Lambda con condizioni multiple annidate
    print("1. Classificazione transazioni:")
    classificate = list(map(
        lambda t: {
            **t,
            "segno": 1 if t["tipo"] == "entrata" else -1,
            "rilevanza": "alta" if t["importo"] > 500 else "media" if t["importo"] > 200 else "bassa",
            "importo_signed": t["importo"] if t["tipo"] == "entrata" else -t["importo"]
        },
        transazioni
    ))
    
    for t in classificate:
        print(f"  ID{t['id']}: €{t['importo_signed']:+.0f} - {t['rilevanza']} rilevanza")
    print()
    
    # 2. Filtri complessi con lambda
    print("2. Uscite significative (> €100):")
    uscite_significative = list(filter(
        lambda t: t["tipo"] == "uscita" and t["importo"] > 100,
        transazioni
    ))
    for t in uscite_significative:
        print(f"  {t['categoria'].title()}: €{t['importo']}")
    print()
    
    # 3. Raggruppamento per categoria usando reduce
    print("3. Totali per categoria:")
    totali_categoria = reduce(
        lambda acc, t: {
            **acc,
            t["categoria"]: acc.get(t["categoria"], 0) + 
                           (t["importo"] if t["tipo"] == "entrata" else -t["importo"])
        },
        transazioni,
        {}
    )
    for categoria, totale in totali_categoria.items():
        print(f"  {categoria.title()}: €{totale:+.0f}")
    print()
    
    # 4. Pipeline complessa: filtra, trasforma, aggrega
    print("4. Pipeline complessa - Analisi uscite per categoria:")
    
    # Step 1: Filtra solo uscite
    # Step 2: Raggruppa per categoria  
    # Step 3: Calcola statistiche
    
    pipeline_result = reduce(
        lambda acc, categoria: {
            **acc,
            categoria: {
                "totale": acc.get(categoria, {"totale": 0, "count": 0, "media": 0})["totale"] + 
                         list(filter(lambda t: t["categoria"] == categoria and t["tipo"] == "uscita", transazioni))[0]["importo"],
                "count": acc.get(categoria, {"totale": 0, "count": 0, "media": 0})["count"] + 1
            }
        },
        set(map(lambda t: t["categoria"], filter(lambda t: t["tipo"] == "uscita", transazioni))),
        {}
    )
    
    # Calcola medie
    for categoria in pipeline_result:
        if pipeline_result[categoria]["count"] > 0:
            pipeline_result[categoria]["media"] = pipeline_result[categoria]["totale"] / pipeline_result[categoria]["count"]
    
    for categoria, stats in pipeline_result.items():
        print(f"  {categoria.title()}: €{stats['totale']:.0f} totale, "
              f"{stats['count']} transazioni, €{stats['media']:.0f} media")
    print()


# =============================================================================
# FUNZIONE MAIN PER ESEGUIRE TUTTI GLI ESEMPI
# =============================================================================

def main():
    """Esegue tutti gli esempi"""
    esempi = [
        esempio_vendite,
        esempio_testi, 
        esempio_matematico,
        esempio_dizionari,
        esempio_avanzato
    ]
    
    for i, esempio in enumerate(esempi):
        esempio()
        if i < len(esempi) - 1:  # Non stampare separatore dopo l'ultimo
            print("=" * 70)
            print()


if __name__ == "__main__":
    main()