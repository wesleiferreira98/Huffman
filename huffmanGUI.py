import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from collections import defaultdict
import heapq
# Importações: collections e heapq são módulos usados para trabalhar com coleções e filas de prioridade (heap), respectivamente.

class NoHuffman:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.frequencia < outro.frequencia

# Classe NoHuffman: Define uma classe para representar um nó na árvore de Huffman. Cada nó possui um caractere, uma frequência, 
# uma referência para o nó filho esquerdo e uma referência para o nó filho direito. A função __lt__ é usada para comparar nós com
# base em suas frequências.

def construir_arvore_huffman(texto):
    frequencias = defaultdict(int)

    # Cria um dicionário padrão onde as chaves são caracteres e os valores são inicializados com zero.

    for char in texto:
        frequencias[char] += 1

    # Conta a frequência de cada caractere no texto, incrementando os valores no dicionário.

    fila_prioridade = [NoHuffman(caractere, frequencia) for caractere, frequencia in frequencias.items()]

    # Cria uma lista de nós NoHuffman com base nas frequências de caracteres no dicionário.

    heapq.heapify(fila_prioridade)

    # Transforma a lista de nós em uma fila de prioridade (heap) usando a função heapify.

    while len(fila_prioridade) > 1:
        no_esquerda = heapq.heappop(fila_prioridade)
        no_direita = heapq.heappop(fila_prioridade)
        no_pai = NoHuffman(None, no_esquerda.frequencia + no_direita.frequencia)
        no_pai.esquerda = no_esquerda
        no_pai.direita = no_direita
        heapq.heappush(fila_prioridade, no_pai)

    # Combina os nós de menor frequência em um novo nó pai, repetindo o processo até que reste apenas um nó na fila.

    return fila_prioridade[0]

    # Retorna o nó raiz da árvore de Huffman construída.

def codificar_texto(arvore_huffman, texto):
    codigos = {}

    # Cria um dicionário para armazenar os códigos de Huffman de cada caractere.

    def gerar_codigos(no, codigo_atual=""):
        if no is not None:
            if no.caractere is not None:
                codigos[no.caractere] = codigo_atual
            gerar_codigos(no.esquerda, codigo_atual + "0")
            gerar_codigos(no.direita, codigo_atual + "1")

    # Função recursiva para gerar os códigos de Huffman a partir da árvore.

    gerar_codigos(arvore_huffman)

    # Gera os códigos de Huffman para cada caractere na árvore.

    codigo_final = ""
    for char in texto:
        codigo_final += codigos[char]

    # Codifica o texto substituindo cada caractere pelo seu código de Huffman.

    return codigo_final

    # Retorna o texto codificado.

class HuffmanGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Codificação de Huffman")
        self.setFixedSize(600, 400)  # Define o tamanho fixo da janela
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)  # Remove o botão de maximizar


        # Janela principal
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        # Título e campo de entrada de texto
        input_label = QLabel("Texto a ser codificado:")
        layout.addWidget(input_label)

        self.text_edit = QTextEdit()
        self.text_edit.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 8px;")
        layout.addWidget(self.text_edit)

        # Botão para codificar o texto
        encode_button = QPushButton("Codificar")
        encode_button.clicked.connect(self.codificar)
        layout.addWidget(encode_button)

        # Título e área de exibição do texto codificado com cor ligeiramente mais escura
        result_label = QLabel("Texto resultante:")
        layout.addWidget(result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: #1E90FF; color: white; border-radius: 8px;")
        layout.addWidget(self.result_text)

        main_widget.setLayout(layout)

        # Aplicar estilo CSS à janela principal
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
        arvore_huffman = construir_arvore_huffman(texto_original)
        codigo_comprimido = codificar_texto(arvore_huffman, texto_original)
        self.result_text.setPlainText(codigo_comprimido)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HuffmanGUI()
    window.show()
    sys.exit(app.exec_())
