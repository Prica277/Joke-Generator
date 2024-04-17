"""
interface.py
by Prica277
Notes: User interface segment of the program.
"""

import sys
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize, Qt
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
        self.setFixedSize(QSize(550, 400))

        layout = QGridLayout()

        widget = QLabel("Welcome To Joke Generator!")
        layout.addWidget(widget)

        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Joke Generator")

        self.setFixedSize(QSize(400, 300))

        layout = QGridLayout()
        layout.addWidget(Color('red'), 0,0)
        layout.addWidget(Color('green'), 1,0)

        widget = QWidget
        widget.setLayout(layout)
        self.setCentralWidget(widget)

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

"""