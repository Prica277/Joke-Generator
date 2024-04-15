"""
controller.py
by Prica277
Python code to make API connections.
"""

import requests as re
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import QSize, Qt

base_url = "https://official-joke-api.appspot.com"
endpoint = "/random_joke"

#building the url
url = base_url + endpoint
response = re.get(url)

if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")

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