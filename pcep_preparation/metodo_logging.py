'''
modulo logging per aggiungere messaggi diagnostici al codice.
Identifica colli di bottiglia e ottimizza codice inefficiente.
'''
"""
Sistema completo di logging e profiling per identificare e ottimizzare
colli di bottiglia nelle prestazioni del codice Python.

Autore: Versione Ottimizzata
Data: 2025
"""

import logging
import time
import cProfile
import pstats
from io import StringIO
from functools import wraps
from contextlib import contextmanager
from typing import List, Any, Callable
import numpy as np


# ============================================================================
# CONFIGURAZIONE LOGGING
# ============================================================================

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


# ============================================================================
# DECORATORI E UTILITY
# ============================================================================

def log_execution_time(func: Callable) -> Callable:
    """
    Decoratore che misura e registra il tempo di esecuzione di una funzione.
    
    Args:
        func: Funzione da decorare
        
    Returns:
        Funzione wrapper che misura il tempo
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logger.debug(f"Inizio esecuzione: {func.__name__}")
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        logger.info(f"{func.__name__} completata in {execution_time:.4f} secondi")
        
        return result
    return wrapper


@contextmanager
def timer(nome_operazione: str):
    """
    Context manager per misurare il tempo di blocchi di codice.
    
    Args:
        nome_operazione: Nome descrittivo dell'operazione
        
    Yields:
        None
        
    Example:
        with timer("Elaborazione dati"):
            # codice da misurare
            process_data()
    """
    logger.info(f"⏱️  Inizio: {nome_operazione}")
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        logger.info(f"✅ Fine: {nome_operazione} - Tempo: {elapsed:.4f}s")


def profile_function(func: Callable) -> Callable:
    """
    Decoratore che esegue il profiling dettagliato di una funzione con cProfile.
    
    Args:
        func: Funzione da profilare
        
    Returns:
        Funzione wrapper che esegue il profiling
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        
        result = func(*args, **kwargs)
        
        profiler.disable()
        
        # Stampa statistiche
        s = StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(10)  # Top 10 funzioni
        
        logger.info(f"\n📊 Profiling di {func.__name__}:\n{s.getvalue()}")
        
        return result
    return wrapper


# ============================================================================
# SEZIONE A: FUNZIONI BASE CON LOGGING
# ============================================================================

@log_execution_time
def funzione_lenta():
    """
    Simula un'operazione lenta (es: query database, chiamata API).
    """
    time.sleep(2)
    logger.debug("Operazione lenta completata con successo")


@log_execution_time
def funzione_veloce():
    """
    Simula un'operazione veloce (es: calcolo in memoria).
    """
    risultato = sum(range(1000))
    logger.debug(f"Operazione veloce completata - Risultato: {risultato}")


# ============================================================================
# SEZIONE B: ELABORAZIONE DATI - VERSIONI DIVERSE
# ============================================================================

def process_data_inefficiente(data: List[List[int]]) -> List[int]:
    """
    Versione inefficiente con cicli annidati - O(n²) apparente.
    Nota: In realtà è O(n*m) dove n=righe, m=colonne.
    
    Args:
        data: Lista bidimensionale di numeri
        
    Returns:
        Lista piatta con valori raddoppiati
    """
    result = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            result.append(data[i][j] * 2)
    return result


def process_data_ottimizzata_v1(data: List[List[int]]) -> List[int]:
    """
    Versione ottimizzata con list comprehension - O(n).
    Più veloce e pythonica.
    
    Args:
        data: Lista bidimensionale di numeri
        
    Returns:
        Lista piatta con valori raddoppiati
    """
    return [elemento * 2 for riga in data for elemento in riga]


def process_data_ottimizzata_v2(data: List[List[int]]) -> List[int]:
    """
    Versione ottimizzata con NumPy - O(n) ma molto più veloce.
    Ideale per grandi dataset.
    
    Args:
        data: Lista bidimensionale di numeri
        
    Returns:
        Lista piatta con valori raddoppiati
    """
    arr = np.array(data)
    return (arr * 2).flatten().tolist()


def process_data_ottimizzata_v3(data: List[List[int]]) -> List[List[int]]:
    """
    Versione che mantiene la struttura bidimensionale.
    
    Args:
        data: Lista bidimensionale di numeri
        
    Returns:
        Lista bidimensionale con valori raddoppiati
    """
    return [[elemento * 2 for elemento in riga] for riga in data]


# ============================================================================
# FUNZIONI DI BENCHMARK
# ============================================================================

def confronta_implementazioni(data: List[List[int]]):
    """
    Confronta le prestazioni delle diverse implementazioni.
    
    Args:
        data: Dataset di test
    """
    logger.info("\n" + "="*70)
    logger.info("📊 BENCHMARK DELLE IMPLEMENTAZIONI")
    logger.info("="*70)
    
    implementazioni = [
        ("Versione Inefficiente", process_data_inefficiente),
        ("Versione Ottimizzata v1 (list comprehension)", process_data_ottimizzata_v1),
        ("Versione Ottimizzata v2 (NumPy)", process_data_ottimizzata_v2),
    ]
    
    risultati = {}
    
    for nome, func in implementazioni:
        with timer(nome):
            start = time.perf_counter()
            result = func(data)
            elapsed = time.perf_counter() - start
            risultati[nome] = elapsed
    
    # Calcola miglioramenti
    logger.info("\n📈 RISULTATI COMPARATIVI:")
    tempo_base = risultati["Versione Inefficiente"]
    
    for nome, tempo in risultati.items():
        if nome == "Versione Inefficiente":
            logger.info(f"  {nome}: {tempo:.6f}s (baseline)")
        else:
            speedup = tempo_base / tempo
            miglioramento = ((tempo_base - tempo) / tempo_base) * 100
            logger.info(
                f"  {nome}: {tempo:.6f}s "
                f"(🚀 {speedup:.2f}x più veloce, {miglioramento:.1f}% migliore)"
            )


@profile_function
def esegui_elaborazione_con_profiling(data: List[List[int]]):
    """
    Esegue l'elaborazione con profiling dettagliato.
    
    Args:
        data: Dataset da elaborare
    """
    return process_data_inefficiente(data)


# ============================================================================
# FUNZIONE PRINCIPALE
# ============================================================================

def main():
    """
    Funzione principale che esegue tutti i test e dimostrazioni.
    """
    logger.info("="*70)
    logger.info("🚀 INIZIO PROGRAMMA - Sistema di Logging e Profiling")
    logger.info("="*70)
    
    # Test 1: Funzioni base
    logger.info("\n📋 TEST 1: Funzioni Base con Logging")
    logger.info("-"*70)
    with timer("Esecuzione funzioni base"):
        funzione_lenta()
        funzione_veloce()
    
    # Test 2: Elaborazione dati - piccolo dataset
    logger.info("\n📋 TEST 2: Elaborazione Dati - Dataset Piccolo")
    logger.info("-"*70)
    data_piccolo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    logger.info(f"Dataset: {data_piccolo}")
    
    result = process_data_ottimizzata_v1(data_piccolo)
    logger.info(f"Risultato: {result}")
    
    # Test 3: Benchmark con dataset medio
    logger.info("\n📋 TEST 3: Benchmark - Dataset Medio")
    logger.info("-"*70)
    data_medio = [[i + j for j in range(100)] for i in range(100)]
    logger.info(f"Dimensioni dataset: {len(data_medio)}x{len(data_medio[0])} = {len(data_medio) * len(data_medio[0])} elementi")
    
    confronta_implementazioni(data_medio)
    
    # Test 4: Profiling dettagliato
    logger.info("\n📋 TEST 4: Profiling Dettagliato con cProfile")
    logger.info("-"*70)
    data_profiling = [[i + j for j in range(50)] for i in range(50)]
    esegui_elaborazione_con_profiling(data_profiling)
    
    # Test 5: Context manager
    logger.info("\n📋 TEST 5: Uso di Context Manager")
    logger.info("-"*70)
    with timer("Operazione complessa"):
        time.sleep(0.5)
        result = process_data_ottimizzata_v2(data_piccolo)
        logger.debug(f"Elaborazione completata: {len(result)} elementi")
    
    logger.info("\n" + "="*70)
    logger.info("✅ FINE PROGRAMMA - Tutti i test completati")
    logger.info("="*70)


# ============================================================================
# ESEMPI AGGIUNTIVI
# ============================================================================

def esempio_logging_avanzato():
    """
    Dimostra l'uso avanzato del logging con diversi livelli.
    """
    logger.debug("Messaggio DEBUG - Dettagli per sviluppatori")
    logger.info("Messaggio INFO - Informazioni generali")
    logger.warning("Messaggio WARNING - Attenzione richiesta")
    logger.error("Messaggio ERROR - Si è verificato un errore")
    logger.critical("Messaggio CRITICAL - Errore critico!")


def esempio_gestione_errori():
    """
    Dimostra la gestione degli errori con logging.
    """
    try:
        # Operazione che potrebbe fallire
        result = 10 / 0
    except ZeroDivisionError as e:
        logger.error(f"Errore matematico: {e}", exc_info=True)
    except Exception as e:
        logger.critical(f"Errore inaspettato: {e}", exc_info=True)


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
    
    # Decommentare per eseguire esempi aggiuntivi
    # print("\n" + "="*70)
    # print("ESEMPI AGGIUNTIVI")
    # print("="*70)
    # esempio_logging_avanzato()
    # esempio_gestione_errori()
