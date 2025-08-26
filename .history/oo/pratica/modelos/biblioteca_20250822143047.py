class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.ativo = True
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    

biblioteca_cidade = Biblioteca("Bilioteca da cidade")

biblioteca_shopping = Biblioteca("Bilioteca do shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)