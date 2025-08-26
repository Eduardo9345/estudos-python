from .avaliacao import Avaliacao

class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.__ativo = False # o __ indica que é privado
        self.__avaliacoes = []
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    @classmethod #Anotation que indica que é um class method
    def listar_bibliotecas(cls): #cls referente a classe
        title = f"{'Nome da biblioteca'.ljust(25)} | {'Status'} |{'Nota média'.ljust(25)}"
        print(title)
        print("-" * len(title))
        [print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo} | {biblioteca.media_avaliacoes.ljust(25)}") for biblioteca in Biblioteca.bibliotecas]

    def alterna_estado(self):
        self.__ativo = not self.__ativo

    @property #retornar - getter usa - se como se fosse um atributo, mas é um método
    def ativo(self):
        return "ativada" if self.__ativo else "desativada"
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self.__avaliacoes.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        if not self.__avaliacoes:
            return "-"
        soma = sum(avaliacao._nota for avaliacao in self.__avaliacoes)
        return round(soma / len(self.__avaliacoes), 1)

