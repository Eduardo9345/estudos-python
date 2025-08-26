class Biblioteca():
    nome = ""
    ativo = False
    

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Bilioteca da cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()

bibliotecas = [biblioteca_cidade, biblioteca_shopping]

print(vars(biblioteca_cidade))
print(vars(biblioteca_shopping))

[print(vars(biblioteca)) for biblioteca in bibliotecas]