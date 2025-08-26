class Biblioteca():
    bibliotecas = []

    def __init__(self, nome="", ativo=False):
        self.nome = nome
        self.ativo = ativo

    def __str__(self):
        return self.nome
    

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Bilioteca da cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()
biblioteca_shopping.nome = "Bilioteca do shopping"
biblioteca_shopping.ativo = True

print(biblioteca_cidade)