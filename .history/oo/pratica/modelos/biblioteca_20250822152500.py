from .avaliacao import Avaliacao

class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self._ativo = False # o __ indica que é privado
        self._avaliacoes = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod #Anotation que indica que é um class method
    def listar_bibliotecas(cls): #cls referente a classe
        title = f"{'Nome da biblioteca'.ljust(25)} | {'Status'} |{'Nota média'.ljust(25)}"
        print(title)
        print("-" * len(title))
        [print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo} | {str(biblioteca.media_avaliacoes).ljust(25)}") for biblioteca in Biblioteca.bibliotecas]

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

