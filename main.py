from PyQt6.QtWidgets import QApplication, QWidget, \
    QPushButton, QMainWindow, QVBoxLayout, QTextEdit

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Morse Code ")
        self.setFixedSize(600, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Type Here to Convert: ")
        self.input_box.setFixedHeight(200)
        layout.addWidget(self.input_box)

        self.convert_button = QPushButton("Convert")
        layout.addWidget(self.convert_button)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        self.output_box.setPlaceholderText("Morse Code")
        layout.addWidget(self.output_box)

        self.convert_button.clicked.connect(self.to_convert)

        central_widget.setLayout(layout)

    def to_convert(self):
        morse_code = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
            'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
            's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'
        }

        morse_code_list = []
        for text in self.input_box.toPlainText():
            if text == " ":
                morse_code_list.append("/")

            elif text in morse_code:
                my_morse_code = morse_code[text]
                morse_code_list.append(my_morse_code)
            else:
                morse_code_list.append("?")
        morse_code_to_text = "  ".join(morse_code_list)
        self.output_box.setText(morse_code_to_text)


app = QApplication(sys.argv)
code = MainWindow()
code.show()
sys.exit(app.exec())
