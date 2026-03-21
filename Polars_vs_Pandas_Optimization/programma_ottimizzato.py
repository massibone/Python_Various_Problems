import polars as pl
import os

def crea_dati_esempio():
    """Crea file CSV di esempio per dimostrare il funzionamento del programma."""
    dati = {
        "id": [1, 2, 3, 4, 5],
        "nome": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "età": [25, 35, 45, 28, 32],
        "città": ["Roma", "Milano", "Roma", "Napoli", "Milano"],
        "reddito": [30000, 45000, 55000, 28000, 42000]
    }
    pl.DataFrame(dati).write_csv("dati.csv")
    
    dati_altro = {
        "id": [1, 2, 3, 4, 5],
        "settore": ["IT", "Finanza", "IT", "Marketing", "Finanza"]
    }
    pl.DataFrame(dati_altro).write_csv("dati_altro.csv")

def esegui_analisi_ottimizzata():
    """Esegue l'analisi dei dati utilizzando Polars in modalità Lazy."""
    
    # 1. Caricamento Lazy (Scansione invece di Lettura)
    # Questo non carica i dati in memoria, ma crea un piano di esecuzione ottimizzato.
    query = (
        pl.scan_csv("dati.csv")
        
        # 2. Filtraggio (Pushdown del filtro: Polars legge solo le righe necessarie)
        .filter(pl.col("età") > 30)
        
        # 3. Selezione (Projection pushdown: Polars legge solo le colonne necessarie)
        .select(["id", "nome", "età", "città", "reddito"])
        
        # 4. Join con un altro dataset (sempre in modalità Lazy)
        .join(
            pl.scan_csv("dati_altro.csv"),
            on="id",
            how="inner"
        )
        
        # 5. Aggregazione complessa in parallelo
        .group_by("città")
        .agg([
            pl.col("età").mean().alias("età_media"),
            pl.col("reddito").sum().alias("reddito_totale"),
            pl.col("settore").first().alias("settore_principale")
        ])
        
        # 6. Ordinamento finale
        .sort("reddito_totale", descending=True)
    )
    
    # 7. Esecuzione effettiva (Collect)
    # Solo a questo punto Polars ottimizza il piano e processa i dati.
    risultato = query.collect()
    
    print("--- Risultato dell'analisi ottimizzata con Polars ---")
    print(risultato)
    return risultato

if __name__ == "__main__":
    # Setup dei dati di test
    crea_dati_esempio()
    
    # Esecuzione del programma
    esegui_analisi_ottimizzata()
    
    print("\nNota: I file 'dati.csv' e 'dati_altro.csv' sono stati creati nella cartella corrente.")
