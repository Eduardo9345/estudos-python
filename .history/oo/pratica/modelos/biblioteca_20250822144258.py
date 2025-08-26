class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.__ativo = False # o __ indica que é privado
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        [print(f"{biblioteca.nome} - {biblioteca.ativo}") for biblioteca in Biblioteca.bibliotecas]

    def alterna_estado(self):
        self.ativo = not self.ativo

    @property #retornar - getter
    def ativo(self):
        return "ativada" if self.__ativo else "desativada"

biblioteca_cidade = Biblioteca("Biblioteca da cidade")

biblioteca_shopping = Biblioteca("Biblioteca do shopping")

print(biblioteca_cidade)
biblioteca_cidade.alterna_estado()
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()