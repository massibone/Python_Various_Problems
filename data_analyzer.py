import os
import shutil
import logging
from pathlib import Path
from typing import Union, List, Dict, Optional
from datetime import datetime
import warnings

# Librerie di analisi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import chardet # 🚨 NUOVO: Rilevamento encoding più robusto

# Configurazione warnings (meno aggressiva)
warnings.filterwarnings('ignore', category=UserWarning) 

# ============================================================================
# CONFIGURAZIONE
# ============================================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

sns.set_style("whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'font.size': 10})

ENCODINGS = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252'] # Rimosso utf-16 per semplicità

# ============================================================================
# CLASSE PRINCIPALE: CSVDataFrameAnalyzer
# ============================================================================

class CSVDataFrameAnalyzer:
    """Analizzatore completo per file CSV con Pandas."""
    
    def __init__(self, csv_path: Union[str, Path], backup: bool = True):
        self.file_path = Path(csv_path)
        self.df: Optional[pd.DataFrame] = None
        self.stats: Dict = {}
        self.report: List[str] = []
        
        # 🚨 NUOVO: Caching delle colonne per l'efficienza
        self._numeric_cols: List[str] = []
        self._cat_cols: List[str] = []
        
        logger.info(f"Inizializzazione analizzatore per: {self.file_path}")
        
        if not self.file_path.exists():
            raise FileNotFoundError(f"File non trovato: {self.file_path}")
        
        if backup:
            self._create_backup()

    def _create_backup(self) -> None:
        """Crea backup del file CSV originale."""
        # ... (Logica backup invariata - OK)
        backup_dir = self.file_path.parent / "backups"
        backup_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{self.file_path.stem}_backup_{timestamp}{self.file_path.suffix}"
        backup_path = backup_dir / backup_name
        shutil.copy2(self.file_path, backup_path)
        logger.info(f"✅ Backup creato: {backup_path}")


    def _detect_encoding(self) -> str:
        """Rileva l'encoding usando chardet per maggiore robustezza."""
        # 🚨 OTTIMIZZAZIONE: Usa chardet per la rilevazione sui byte
        with open(self.file_path, 'rb') as f:
            raw_data = f.read(1024 * 10)  # Leggi 10KB di dati binari
        
        result = chardet.detect(raw_data)
        detected_enc = result['encoding'] or 'utf-8' # Fallback
        
        logger.debug(f"Encoding rilevato (chardet): {detected_enc} (confidenza: {result['confidence']:.2f})")
        
        # Tenta i preferiti, altrimenti usa chardet
        for enc in ENCODINGS:
            if enc.lower() == detected_enc.lower():
                 return enc
        
        # Fallback a chardet o utf-8
        return detected_enc if result['confidence'] > 0.5 else 'utf-8'


    def _detect_separator(self, encoding: str) -> str:
        """Rileva automaticamente il separatore basato sulla prima riga."""
        # ... (Logica separatore invariata - OK, ma vedi nota su sniff)
        with open(self.file_path, 'r', encoding=encoding) as f:
            first_line = f.readline()
        
        separators = {
            ',': first_line.count(','),
            ';': first_line.count(';'),
            '\t': first_line.count('\t'),
        }
        
        # Sceglie il separatore con il conteggio massimo
        sep = max(separators, key=separators.get)
        
        # Verifica che il separatore non sia troppo raro
        if separators[sep] < 1:
             logger.warning("Separatore non chiaro, usa virgola come default.")
             return ','
        
        logger.debug(f"Separatore rilevato: '{sep}'")
        return sep


    def load_csv(self, **kwargs) -> pd.DataFrame:
        """Carica CSV con detection automatica encoding e separatore."""
        logger.info("Caricamento CSV in corso...")
        
        encoding = self._detect_encoding()
        sep = self._detect_separator(encoding)
        
        try:
            self.df = pd.read_csv(
                self.file_path,
                sep=sep,
                encoding=encoding,
                **kwargs
            )
            
            # 🚨 OTTIMIZZAZIONE: Caching dei tipi di colonna
            self._numeric_cols = self.df.select_dtypes(include=np.number).columns.tolist()
            self._cat_cols = self.df.select_dtypes(include=['object', 'category']).columns.tolist()

            logger.info(f"✅ CSV caricato: {self.df.shape[0]} righe, {self.df.shape[1]} colonne. Encoding: {encoding}, Separatore: '{sep}'")
            
            self._add_report(f"File caricato: {self.file_path.name}")
            self._add_report(f"Dimensioni: {self.df.shape[0]} righe × {self.df.shape[1]} colonne")
            
            return self.df
        except Exception as e:
            logger.error(f"❌ Errore caricamento CSV: {e}")
            raise

    # ----------------------------------------------------------------------
    # METODI DI ANALISI 
    # ----------------------------------------------------------------------

    def analyze(self, generate_plots: bool = True) -> Dict:
        """Esegue analisi statistica completa del DataFrame."""
        if self.df is None:
            raise ValueError("Caricare prima un CSV con load_csv()")
        
        # ... (logica invariata)
        self._analyze_general_info()
        self._analyze_missing_values()
        self._analyze_duplicates()
        self._analyze_descriptive_stats()
        self._analyze_correlations()
        
        if generate_plots:
             self._generate_visualizations()
             
        logger.info("✅ Analisi completata")
        return self.stats


    def _analyze_descriptive_stats(self) -> None:
        """Calcola statistiche descrittive (usa colonne cachate)."""
        self._add_report("\n📈 STATISTICHE DESCRITTIVE")
        
        if self._numeric_cols:
            desc = self.df[self._numeric_cols].describe()
            self.stats['descriptive_numeric'] = desc.to_dict()
            self._add_report("\nColonne numeriche:")
            self._add_report(desc.to_string()) # Usa to_string() per un report pulito
        
        if self._cat_cols:
            self._add_report("\nColonne categoriche:")
            for col in self._cat_cols:
                value_counts = self.df[col].value_counts()
                self._add_report(f" • {col} (Unici: {len(value_counts)}): Top 3 Valori:\n{value_counts.head(3).to_string()}")


    def _analyze_correlations(self) -> None:
        """Calcola matrice di correlazione (usa colonne cachate)."""
        self._add_report("\n🔗 CORRELAZIONI")
        
        if len(self._numeric_cols) < 2:
            self._add_report("⚠️ Meno di 2 colonne numeriche, correlazione non calcolabile")
            return
        
        corr_matrix = self.df[self._numeric_cols].corr()
        self.stats['correlation_matrix'] = corr_matrix.to_dict()
        
        # Logica di strong_corr mantenuta ma snellita
        strong_corr = corr_matrix.unstack().sort_values(ascending=False)
        strong_corr = strong_corr[strong_corr.index.get_level_values(0) != strong_corr.index.get_level_values(1)]
        strong_corr = strong_corr[abs(strong_corr) > 0.7].drop_duplicates()

        if not strong_corr.empty:
            self._add_report("Correlazioni forti (|r| > 0.7):")
            for (col1, col2), val in strong_corr.items():
                 self._add_report(f" • {col1} ↔ {col2}: {val:.3f}")
        else:
            self._add_report("Nessuna correlazione forte rilevata")
            

    # ----------------------------------------------------------------------
    # METODI DI VISUALIZZAZIONE 
    # ----------------------------------------------------------------------

    def _generate_visualizations(self) -> None:
        """Genera visualizzazioni automatiche (usa colonne cachate)."""
        logger.info("Generazione visualizzazioni...")
        
        output_dir = self.file_path.parent / "plots"
        output_dir.mkdir(exist_ok=True)
        
        if len(self._numeric_cols) >= 2:
            self._plot_correlation_matrix(output_dir)
        
        if self._numeric_cols:
            # 🚨 Semplificato: combina distribuzioni e boxplots in un unico metodo
            self._plot_univariate_numeric(output_dir) 
        
        if self.df.isnull().sum().sum() > 0:
            self._plot_missing_values(output_dir)
            
        logger.info(f"✅ Visualizzazioni salvate in: {output_dir}")

    
    def _plot_univariate_numeric(self, output_dir: Path) -> None:
        """Genera istogrammi e boxplots per le variabili numeriche in un unico file."""
        fig, axes = plt.subplots(len(self._numeric_cols), 2, 
                                 figsize=(15, 4 * len(self._numeric_cols)))
        
        if len(self._numeric_cols) == 1:
            axes = [axes] # Gestisce il caso di una sola colonna per l'indexing
        
        for idx, col in enumerate(self._numeric_cols):
            # Istogramma
            sns.histplot(self.df[col], kde=True, ax=axes[idx][0] if len(self._numeric_cols) > 1 else axes[0])
            axes[idx][0].set_title(f'Distribuzione: {col}')
            
            # Boxplot
            sns.boxplot(x=self.df[col], ax=axes[idx][1] if len(self._numeric_cols) > 1 else axes[1])
            axes[idx][1].set_title(f'Outliers: {col}')

        plt.tight_layout()
        plt.savefig(output_dir / 'univariate_numeric.png', dpi=300)
        plt.close()

    # ----------------------------------------------------------------------
    # PULIZIA DATI 
    # ----------------------------------------------------------------------

    def clean_data(
        self,
        # ... (Argomenti invariati)
        handle_missing: str = 'drop',
    ) -> pd.DataFrame:
        """Pulisce il DataFrame."""
        df_clean = self.df.copy()
        
        # ... (Logica Duplicati invariata)
        
        # 2. Valori mancanti (logica potenziata per categorie)
        if handle_missing == 'drop':
             df_clean = df_clean.dropna()
        
        elif handle_missing in ['fill_mean', 'fill_median']:
            fill_func = df_clean[self._numeric_cols].mean() if handle_missing == 'fill_mean' else df_clean[self._numeric_cols].median()
            df_clean[self._numeric_cols] = df_clean[self._numeric_cols].fillna(fill_func)
            logger.info(f" • Valori numerici mancanti riempiti con {handle_missing.split('_')[1]}")
            
        elif handle_missing == 'fill_mode':
            # Riempie i numerici con la mediana e i categorici con la moda
            for col in self._numeric_cols:
                df_clean[col].fillna(df_clean[col].median(), inplace=True)
            for col in self._cat_cols:
                df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
            logger.info(" • Valori mancanti riempiti: Mediana (numerici), Moda (categorici)")

        # ... (Logica Outliers invariata)
        
        return df_clean

    # ... (Metodi _add_report, _format_bytes e export_report invariati)
