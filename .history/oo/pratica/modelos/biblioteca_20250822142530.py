class Biblioteca():
    nome = ""
    ativo = False
    

biblioteca_cidade = Biblioteca()
biblioteca_cidade.nome = "Bilioteca da cidade"
biblioteca_cidade.ativo = True

biblioteca_shopping = Biblioteca()
biblioteca_shopping.nome = "Bilioteca do shopping"
biblioteca_shopping.ativo = True

bibliotecas = [biblioteca_cidade, biblioteca_shopping]

print(vars(biblioteca_cidade))
print(vars(biblioteca_shopping))

[print(vars(biblioteca)) for biblioteca in bibliotecas]