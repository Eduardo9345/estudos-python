class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.ativo = True
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        [print(f"{biblioteca.nome} - {biblioteca.ativo}") for biblioteca in Biblioteca.bibliotecas]

biblioteca_cidade = Biblioteca("Biblioteca da cidade")

biblioteca_shopping = Biblioteca("Biblioteca do shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()