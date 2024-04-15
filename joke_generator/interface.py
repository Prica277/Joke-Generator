"""
interface.py
by Prica277
Notes: User interface segment of the program.
"""

import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QGridLayout,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QSlider,
)

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Joke Generator")

        layout = QGridLayout

        btn = QPushButton("blue")
        layout.addWidget(btn)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()