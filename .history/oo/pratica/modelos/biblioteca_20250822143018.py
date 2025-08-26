class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.ativo = True
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    

biblioteca_cidade = Biblioteca("Bilioteca da cidade")

biblioteca_shopping = Biblioteca()
biblioteca_shopping.nome = "Bilioteca do shopping"
biblioteca_shopping.ativo = True

print(biblioteca_cidade)