from modelos.biblioteca import Biblioteca

biblioteca_cidade = Biblioteca("Biblioteca da cidade")

biblioteca_shopping = Biblioteca("Biblioteca do shopping")


biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()


Biblioteca.listar_bibliotecas()


