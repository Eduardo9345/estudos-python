
from .avaliacao import Avaliacao

class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self._ativo = False # o __ indica que é privado
        self._avaliacoes = []
        self._itens = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod #Anotation que indica que é um class method
    def listar_bibliotecas(cls): #cls referente a classe
        title = f"{'Nome da biblioteca'.ljust(25)}|{'Nota média'.ljust(25)}| {'Status'} |"
        print(title)
        print("-" * len(title))
        [print(f"{biblioteca.nome.ljust(25)}|{str(biblioteca.media_avaliacoes).ljust(25)}| {biblioteca.ativo} |") for biblioteca in Biblioteca.bibliotecas]

    def alterna_estado(self):
        self._ativo = not self._ativo

    @property #retornar - getter usa - se como se fosse um atributo, mas é um método
    def ativo(self):
        return "ativada" if self._ativo else "desativada"

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        return round(soma / len(self._avaliacoes), 1)

    def adicionar_item(self, item):
        if isinstance(item, ItemBiblioteca):
            self._itens.append(item)

    def exibir_itens(self):
        print(f"Itens da biblioteca {self.nome}\n")

        for i, item in enumerate(self._itens, start=1):
            msg = str(item)
            print(msg)
