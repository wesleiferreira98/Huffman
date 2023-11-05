import sys
from PyQt5.QtWidgets import QApplication
from huffman_GUI import HuffmanGUI
from arvore_huffman import ArvoreHuffman

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HuffmanGUI()
    window.show()
    sys.exit(app.exec_())
