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

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        #setting minor window details
        self.setWindowTitle("Joke Generator")
        self.setFixedSize(QSize(550, 400))

        #create layout
        main_layout = QGridLayout()

        #title label
        title_label = QLabel("Welcome To Joke Generator!")

        #align the title label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | 
                                 Qt.AlignmentFlag.AlignTop)
        
        #coloring title label
        """
        BROKEN:
        title_label.setAutoFillBackground(True)
        pal = title_label.palette()
        pal.setColor("195, 171, 208")
        title_label.setPalette(pal) 
        
        #QColor(195, 171, 208)
        """
        #add title label
        main_layout.addWidget(title_label, 0, 1)

        #explaning the use of joke number slider
        explanation_number_label = QLabel("Select amount of jokes (1 or 10)")

        #adding the explanation label
        main_layout.addWidget(explanation_number_label, 1, 0)

        #joke number slider
        joke_number_slider = QSlider(Qt.Orientation.Horizontal)
        joke_number_slider.setMinimum(1)
        joke_number_slider.setMaximum(10) 
        joke_number_slider.setSingleStep(10)

        #adding the joke number slider
        main_layout.addWidget(joke_number_slider, 1, 3)

        #explanation_type_label
        explanation_type_label = QLabel("Enter the type of joke:")

        #adding the explanation label
        main_layout.addWidget(explanation_type_label, 2, 0)
        self.setLayout(main_layout)

        #joke type input box
        joke_type_input = QLineEdit()
        joke_type_input.setMaxLength(15)
        joke_type_input.setPlaceholderText("Type here!")
        
        joke_type_input.returnPressed.connect(self.return_pressed)
        joke_type_input.selectionChanged.connect(self.selection_changed)
        joke_type_input.textChanged.connect(self.text_changed)
        joke_type_input.textEdited.connect(self.text_edited)
        
        #aligning input box
        
        #adding the joke type input box
        main_layout.addWidget(joke_type_input, 2, 3)

        #Go button (should switch between layouts)
        go_button = QPushButton("Go!")

        #aligning go_button
        

        #adding go_button
        main_layout.addWidget(go_button, 3, 2)


        

    #Works with joke_type_input line edit widget
    def return_pressed(self):
        print("Return pressed!")
        self.joke_type_input().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.joke_type_input().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
app.setStyle("Fusion")

window = MainWindow()
window.show()

app.exec()