from modelos.biblioteca import Biblioteca #o .biblioteca entra no arquivo


biblioteca_cidade = Biblioteca("Biblioteca da cidade")

biblioteca_shopping = Biblioteca("Biblioteca do shopping")


biblioteca_cidade.alterna_estado()
biblioteca_shopping.alterna_estado()

biblioteca_cidade.receber_avaliacao("Fulano", 8.5)
biblioteca_cidade.receber_avaliacao("Sicrano", 9.5)

def main():
    Biblioteca.listar_bibliotecas()

if __name__ == "__main__": # Se o ponto de execução for esse arquivo
    main()