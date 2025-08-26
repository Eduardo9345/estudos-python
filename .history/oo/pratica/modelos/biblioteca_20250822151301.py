import Avaliacao

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
        title = f"{'Nome da biblioteca'.ljust(25)} | {'Status'}"
        print(title)
        print("-" * len(title))
        [print(f"{biblioteca.nome.ljust(25)} | {biblioteca.ativo}") for biblioteca in Biblioteca.bibliotecas]

    def alterna_estado(self):
        self.__ativo = not self.__ativo

    @property #retornar - getter
    def ativo(self):
        return "ativada" if self.__ativo else "desativada"
    
    def receber_avaliacao(self, cliente, nota):

