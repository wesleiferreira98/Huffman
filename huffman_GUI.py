from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from arvore_huffman import ArvoreHuffman  # Importe a classe ArvoreHuffman

class HuffmanGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codificação de Huffman")
        self.setFixedSize(600, 400)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        input_label = QLabel("Texto a ser codificado:")
        layout.addWidget(input_label)

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 8px;")
        layout.addWidget(self.text_edit)

        encode_button = QPushButton("Codificar")
        encode_button.clicked.connect(self.codificar)
        layout.addWidget(encode_button)

        result_label = QLabel("Texto resultante:")
        layout.addWidget(result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 8px;")
        layout.addWidget(self.result_text)

        main_widget.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #9dcfff;
                border-radius: 70px;
            }
            QPushButton {
                background-color: #1E90FF;
                border: none;
                color: white;
                text-align: center;
                font-size: 16px;
                padding: 10px 20px;
                margin: 4px 2px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1C86EE;
            }
        """)

    def codificar(self):
        texto_original = self.text_edit.toPlainText()
        arvore_huffman = ArvoreHuffman(texto_original)  # Crie uma instância da classe ArvoreHuffman
        codigo_comprimido = arvore_huffman.codificar_texto(texto_original)  # Chame o método da instância
        self.result_text.setPlainText(codigo_comprimido)
