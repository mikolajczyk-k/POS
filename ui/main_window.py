"""
main_window.py - Statyczny plik z definicją okna głównego aplikacji (GUI)

Zawiera wszystkie elementy okna głównego (baner statusu, pasek etapów, przyciski sterujące i okno komunikatów)

"""
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
    QTextEdit, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QAbstractItemView,
)

from ui.style import STYLE, Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Controller")
        self.resize(820, 640)
        self._build_ui()
    
    def _build_ui(self):
        central = QWidget()
        root = QVBoxLayout(central)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)
 
        root.addWidget(self._build_banner())
        root.addWidget(self._build_stepper())
        root.addLayout(self._build_controls())
 
        lbl_results = QLabel("Wyniki testów")
        lbl_results.setObjectName("section")
        root.addWidget(lbl_results)
        root.addWidget(self._build_table(), stretch=2)

        lbl_log = QLabel("Komunikaty")
        lbl_log.setObjectName("section")
        root.addWidget(lbl_log)
        root.addWidget(self._build_log(), stretch=1)
 
        self.setCentralWidget(central)

        self.setStyleSheet(STYLE)

 

    def _build_banner(self) -> QLabel:
        """Duży baner statusu u góry okna."""
        banner = QLabel("Gotowy — umieść mikrokontroler i naciśnij Start")
        banner.setObjectName("banner")
        banner.setAlignment(Qt.AlignCenter)
        banner.setMinimumHeight(64)
        f = QFont()
        f.setPointSize(15)
        f.setBold(True)
        banner.setFont(f)
        self.status_banner = banner
        return banner
 
    def _build_stepper(self) -> QWidget:
        """Status bar: Flashowanie → Testowanie → Zakończenie."""
        wrap = QWidget()
        row = QHBoxLayout(wrap)
        row.setContentsMargins(0, 0, 0, 0)
        steps = ["1. Flashowanie", "2. Testowanie", "3. Zakończenie"]
        for i, name in enumerate(steps):
            lbl = QLabel(name)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setObjectName("step")
            lbl.setProperty("active", i == 0)
            row.addWidget(lbl)
            if i < len(steps) - 1:
                arrow = QLabel("-->")
                arrow.setObjectName("arrow")
                row.addWidget(arrow)
        return wrap
 
    def _build_controls(self) -> QHBoxLayout:
        """Przyciski sterujące"""
        controls = QHBoxLayout()
        self.start_btn = QPushButton("Start")
        self.start_btn.setObjectName("start")
        self.abort_btn = QPushButton("Abort")
        self.abort_btn.setObjectName("abort")
        self.export_btn = QPushButton("Eksportuj raport CSV")
        self.export_btn.setObjectName("export")
        self.export_btn.setEnabled(False)  # aktywne dopiero po zakończeniu testów
 
        for b in (self.start_btn, self.abort_btn, self.export_btn):
            b.setMinimumHeight(40)
            b.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
 
        controls.addWidget(self.start_btn)
        controls.addWidget(self.abort_btn)
        controls.addWidget(self.export_btn)

        return controls
 
    def _build_table(self) -> QTableWidget:
        """Tabela wyników"""
        table = QTableWidget(0, 4)
        table.setHorizontalHeaderLabels(
            ["Test", "Wynik", "Wartość / szczegóły", "Czas"])
        table.verticalHeader().setVisible(False)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)
 
        """Przykładowe dane i wyniki"""
        sample = [
            ("Test (I/O)", "PASS", "Stany logiczne zgodne", "12:00:01"),
            ("Test komunikacji SPI", "PASS", "Brak błędów", "12:00:02"),
            ("Test ADC/DAC", "FAIL", "Błąd 16.6%", "12:00:03"),
        ]
        for r, (test, result, detail, t) in enumerate(sample):
            table.insertRow(r)
            table.setItem(r, 0, QTableWidgetItem(test))
            item = QTableWidgetItem(result)
            item.setTextAlignment(Qt.AlignCenter)
            # Zielony dla pass czerwony dla fail
            if result == "PASS":
                item.setBackground(QColor(Color.PASS))
            elif result == "FAIL":
                item.setBackground(QColor(Color.FAIL))
            table.setItem(r, 1, item)
            table.setItem(r, 2, QTableWidgetItem(detail))
            t_item = QTableWidgetItem(t)
            t_item.setTextAlignment(Qt.AlignCenter)
            table.setItem(r, 3, t_item)
 
        self.table = table
        return table
    

    def _build_log(self) -> QTextEdit:
        """Okno komunikatów"""
        log = QTextEdit()
        log.setReadOnly(True)
        log.setObjectName("log")
        log.setPlainText(
            "[12:00:00]  Aplikacja uruchomiona.\n"
            "[12:00:00]  Oczekiwanie na podłączenie testera...")
        self.log = log
        return log
 