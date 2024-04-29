"""
interface.py
by Prica277
Notes: User interface segment of the program.
"""

import sys
from PyQt6.QtGui import QPalette, QColor, QFontDatabase, QFont
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QGridLayout,
    QVBoxLayout,
    QStackedLayout,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QSlider,
)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        #setting minor window details
        self.setWindowTitle("Joke Generator")
        self.setFixedSize(QSize(550, 200))
        self.setContentsMargins(20, 20, 20, 20)

        #create layouts
        #self.layout = QVBoxLayout()
        main_layout = QGridLayout()
        results_layout = QGridLayout()
        self.stacked_layout = QStackedLayout()
        # self.layout.addLayout(main_layout)
        #self.stacked_layout.addStretch()

        #creating first screen
        self.main_screen = QWidget()
        self.main_screen.setLayout(main_layout)
        self.stacked_layout.addWidget(self.main_screen)

        #title label
        title_label = QLabel("Welcome To Joke Generator!")
        title_label.setFont(QFont("Calibri", 20, 800))

        #align & size the title label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        #coloring title label
        title_label.setStyleSheet("background-color:#C3ABD0; border-radius:4px; padding:10px; height:30px;")
        
        #add title label
        main_layout.addWidget(title_label, 0, 0, 1, 4)

        #explaning the use of joke number slider
        explanation_number_label = QLabel("Select amount of jokes (1 or 10)")

        #coloring explanation label
        explanation_number_label.setStyleSheet("background-color:#FFE599;")

        #adding the explanation label
        main_layout.addWidget(explanation_number_label, 1, 0)

        #joke number slider
        self.joke_number_slider = QSlider(Qt.Orientation.Horizontal)
        self.joke_number_slider.setMinimum(1)
        self.joke_number_slider.setMaximum(10) 
        self.joke_number_slider.setSingleStep(10)

        #adding the joke number slider
        main_layout.addWidget(self.joke_number_slider, 1, 1, 1, 3)

        #explanation_type_label
        explanation_type_label = QLabel("Enter the type of joke:")

        #coloring explanation label
        explanation_type_label.setStyleSheet("background-color:#FFE599")

        #adding the explanation label
        main_layout.addWidget(explanation_type_label, 2, 0)

        #joke type input box
        self.joke_type_input = QLineEdit()
        self.joke_type_input.setMaxLength(15)
        self.joke_type_input.setPlaceholderText("Type here!")
        
        self.joke_type_input.returnPressed.connect(self.return_pressed)
        self.joke_type_input.selectionChanged.connect(self.selection_changed)
        self.joke_type_input.textChanged.connect(self.text_changed)
        self.joke_type_input.textEdited.connect(self.text_edited)
        
        #adding the joke type input box
        main_layout.addWidget(self.joke_type_input, 2, 1, 1, 3)

        #Go button (should switch between layouts)
        go_button = QPushButton("Go!")

        #coloring go button
        go_button.setStyleSheet("background-color:#97D077")

        #adding functionality to go button
        go_button.clicked.connect(self.next_page)

        #adding go_button
        main_layout.addWidget(go_button, 3, 1)

        #creating results page
        self.results_page = QWidget()
        self.results_page.setLayout(results_layout)
        self.stacked_layout.addWidget(self.results_page)

        #title label
        title_label = QLabel("Welcome To Joke Generator!")
        title_label.setFont(QFont("Calibri", 20, 800))

        #align & size the title label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        #coloring title label
        title_label.setStyleSheet("background-color:#C3ABD0; border-radius:4px; padding:10px; height:30px;")
        
        #add title label
        results_layout.addWidget(title_label, 0, 0, 1, 4)

        # results explanation label
        explanation_type_label = QLabel("Response: ")

        #coloring explanation label
        explanation_type_label.setStyleSheet("background-color:#FFE599")

        #adding the explanation label
        results_layout.addWidget(explanation_type_label, 1, 0)

        # prints resulting joke (label?)
        joke_result = QLabel("What do you call a troublesome Canadian high schooler? A poutine")

        #adding the explanation label
        results_layout.addWidget(joke_result, 1, 1, 1, 3)

        # reset button
        reset_button = QPushButton("Reset")
        reset_button.setStyleSheet("background-color:#97D077")
        reset_button.clicked.connect(self.previous_page)
        results_layout.addWidget(reset_button, 2, 1)

        self.setLayout(self.stacked_layout)


    #Works with self.joke_type_input line edit widget
    def return_pressed(self):
        print("Return pressed!")
        self.joke_type_input().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.joke_type_input.text())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def next_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() + 1)
        
    def previous_page(self):
        self.stacked_layout.setCurrentIndex(
            self.stacked_layout.currentIndex() - 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()
