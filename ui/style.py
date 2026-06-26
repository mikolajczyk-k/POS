"""Plik stylów dla main_window.py"""


class Color:
    """PALETA KOLORÓW"""

    BG = "#20242c"   # tło
    SURFACE = "#2b303a"   # panele, nagłówki
    TEXT = "#eeeeee" 
    TEXT_MUTED  = "#9aa3b2" #dla nieakwynych

    PASS = "#1f7a3d"   # zielony — test zaliczony
    FAIL = "#a32424"   # czerwony — błąd / abort
    RUNNING = "#1f4f7a"   # aktualna faza procesu
    ACCENT = "#3a4150"   # przyciski neutralne

STYLE=f"""
QMainWindow, QWidget {{
    background: {Color.BG};
    color: {Color.TEXT};
}}

QPushButton#start {{
    background: {Color.PASS};
}}
QPushButton#abort {{
    background: {Color.FAIL};
}}

QPushButton#export {{
    text: {Color.TEXT_MUTED};

}}

QLabel#step[active="true"] {{
    background: {Color.RUNNING};
    color: white;
}}

QTableWidget {{
    background: {Color.SURFACE};
    gridline-color: {Color.BG};
}}

QTableWidget::item {{
    padding: 4px;
    color: {Color.TEXT};
}}

QHeaderView::section {{
    background: {Color.SURFACE};
    color: {Color.TEXT};
    padding: 4px;
    border: none;
}}
"""