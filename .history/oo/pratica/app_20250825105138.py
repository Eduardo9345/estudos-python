from modelos.biblioteca import Biblioteca
from pratica.modelos.itens.livro import Livro
from pratica.modelos.itens.revista import Revista #o .biblioteca entra no arquivo




biblioteca_cidade = Biblioteca("Biblioteca da cidade")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

livro1 = Livro("1984", "George Orwell", 30.0, "084-3245")
revista1 = Revista("National Geographic", "Jonh Doe", 15.0, "Quinta")

biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
biblioteca_cidade.receber_avaliacao("Sicrano", 9.5)

def main():
    Biblioteca.listar_bibliotecas()
    print(vars(livro1))
    print(vars(revista1))

if __name__ == "__main__": # Se o ponto de execução for esse arquivo
    main()