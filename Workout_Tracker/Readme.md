# Workout Tracker – Fitloop Phase 2

Tracker grafico (PySide6) per il programma calisthenics Fitloop, Phase 2 (W5–W8).

## Funzionalità

- Tabella con 9 esercizi × 12 sessioni (4 settimane × 3 allenamenti)
- **QComboBox** per selezionare il rung (progressione) di ogni esercizio
- Celle di tracking editabili (rep + RIR)
- Salvataggio / caricamento in JSON
- Regola di progressione visualizzata in fondo

## Regola di progressione

| RIR | Azione |
|-----|--------|
| ≥ 3 | +1 rep |
| 2 | Stesso |
| ≤ 1 | −1 rep |
| Top range | Salta di rung (cambia combo) |
| W8 | Scarico −20% |

## Setup


pip install -r requirements.txt
