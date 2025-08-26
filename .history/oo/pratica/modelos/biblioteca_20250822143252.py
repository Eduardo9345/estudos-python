class Biblioteca():
    bibliotecas = []

    def __init__(self, nome=""):
        self.nome = nome
        self.ativo = True
        Biblioteca.bibliotecas.append(self)

    def __str__(self):
        return self.nome
    
    def listar_bibliotecas():
        return [str(biblioteca) for biblioteca in Biblioteca.bibliotecas]
    
    

biblioteca_cidade = Biblioteca("Bilioteca da cidade")

biblioteca_shopping = Biblioteca("Bilioteca do shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)

print(Biblioteca.listar_bibliotecas())