from collections import defaultdict
import heapq
from NoHuffman import *

class ArvoreHuffman:
    def __init__(self, texto):
        self.texto = texto
        self.arvore = self.construir_arvore_huffman()

    def construir_arvore_huffman(self):
        frequencias = defaultdict(int)
        for char in self.texto:
            frequencias[char] += 1

        fila_prioridade = [NoHuffman(caractere, frequencia) for caractere, frequencia in frequencias.items()]
        heapq.heapify(fila_prioridade)

        while len(fila_prioridade) > 1:
            no_esquerda = heapq.heappop(fila_prioridade)
            no_direita = heapq.heappop(fila_prioridade)
            no_pai = NoHuffman(None, no_esquerda.frequencia + no_direita.frequencia)
            no_pai.esquerda = no_esquerda
            no_pai.direita = no_direita
            heapq.heappush(fila_prioridade, no_pai)

        return fila_prioridade[0]

    def codificar_texto(self, texto):
        codigos = {}

        def gerar_codigos(no, codigo_atual=""):
            if no is not None:
                if no.caractere is not None:
                    codigos[no.caractere] = codigo_atual
                gerar_codigos(no.esquerda, codigo_atual + "0")
                gerar_codigos(no.direita, codigo_atual + "1")

        gerar_codigos(self.arvore)

        codigo_final = ""
        for char in texto:
            codigo_final += codigos[char]

        return codigo_final
