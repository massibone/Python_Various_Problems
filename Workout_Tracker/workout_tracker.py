import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QLabel, QHeaderView, QComboBox, QWidget,
    QHBoxLayout, QAbstractItemView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

# ─── Progressioni dal gist RR ───────────────────────────────────
PROGRESSIONS = {
    "Prone Y-T-W-A": [
        "No band",
        "Light band",
        "Medium band",
        "Heavy band",
    ],
    "Reverse snow angel": [
        "No band",
        "Light band",
        "Medium band",
    ],
    "Pull-up": [
        "Dead hang",
        "Scapular pull",
        "Negative (3-5s)",
        "Negative (4-5s)",
        "Band-assisted",
        "Full pull-up",
        "Chest-to-bar",
    ],
    "Push-up A": [
        "Wall",
        "Incline (alto)",
        "Incline (basso)",
        "Knee",
        "Full",
        "Feet-elevated",
        "Archer",
    ],
    "Push-up B": [
        "Knee diamond",
        "Full diamond",
        "Feet-elevated diamond",
        "Archer push-up",
    ],
    "Squat": [
        "Sit-to-stand",
        "BW Squat",
        "Split squat",
        "Bulgarian split",
        "Pistol (assisted)",
        "Pistol",
    ],
    "Row": [
        "Vertical row",
        "Incline row (45°)",
        "Incline row (30°)",
        "Horizontal row",
        "Feet-elevated row",
        "Archer row",
    ],
    "Bridge": [
        "Glute bridge",
        "Single-leg bridge",
        "Single-leg elevated",
        "Hip thrust BW",
    ],
    "Core (Dead bug / Hollow)": [
        "Dead bug",
        "Hollow body hold",
        "Tuck L-sit",
        "L-sit",
    ],

}

# ─── Config scheda ──────────────────────────────────────────────
ESERCIZI = list(PROGRESSIONS.keys())
SETTIMANE = ["W5", "W6", "W7", "W8"]
SESSIONI = ["S1", "S2", "S3"]


class WorkoutTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calisthenics – Phase 2 · W5–8")
        self.resize(1200, 520)
        self._build()

    def _build(self):
        layout = QVBoxLayout()

        title = QLabel("CALISTHENICS – PHASE 2 · WEEKS 5–8")
        title.setFont(QFont("Arial", 13, weight=75))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Colonne: Esercizio | Rung | W5S1..W8S3 (12) = 14
        n_track = len(SETTIMANE) * len(SESSIONI)
        n_cols = 2 + n_track
        n_rows = len(ESERCIZI)

        table = QTableWidget(n_rows, n_cols)
        table.verticalHeader().setVisible(False)

        # ── Intestazioni ──
        headers = ["Esercizio", "Rung (progressione)"]
        for w in SETTIMANE:
            for s in SESSIONI:
                headers.append(f"{w}\n{s}")
        for c, h in enumerate(headers):
            item = QTableWidgetItem(h)
            item.setTextAlignment(Qt.AlignCenter)
            table.setHorizontalHeaderItem(c, item)

        # ── Righe ──
        for r, ex in enumerate(ESERCIZI):
            # Col 0: nome
            name_item = QTableWidgetItem(ex)
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            table.setItem(r, 0, name_item)

            # Col 1: QComboBox (rung)
            combo = QComboBox()
            combo.addItems(PROGRESSIONS[ex])
            combo.setFont(QFont("Arial", 9))
            # Posiziona il combo nella cella
            table.setCellWidget(r, 1, combo)

            # Col 2+: tracking (editable)
            for c in range(2, n_cols):
                item = QTableWidgetItem("")
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(r, c, item)

        # ── Larghezze colonne ──
        table.setColumnWidth(0, 160)
        table.setColumnWidth(1, 180)
        for c in range(2, n_cols):
            table.setColumnWidth(c, 65)

        # Altezza righe
        for r in range(n_rows):
            table.setRowHeight(r, 32)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)

        layout.addWidget(table)

        # ── Regola ──
        regola = QLabel(
            "RIR≥3 → +1 rep  |  RIR=2 → stesso  |  RIR≤1 → −1  |  "
            "Top range → salta di rung (cambia combo)  |  W8 = scarico −20%"
        )
        regola.setFont(QFont("Arial", 8, italic=True))
        regola.setStyleSheet("color: #555;")
        layout.addWidget(regola)

        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def save(self, path="workout.json"):
        import json
        data = {}
        for r in range(self.table.rowCount()) if hasattr(self, 'table') else range(0):
            pass
        # Nota: per il save completo serve tenere un ref alla table
        # (vedi estensione sotto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WorkoutTracker()
    win.show()
    sys.exit(app.exec())   
