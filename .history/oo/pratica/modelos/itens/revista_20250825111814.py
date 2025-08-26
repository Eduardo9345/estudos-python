from .item_biblioteca import ItemBiblioteca


class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self._edicao = edicao

    def __str__(self):
        return super().__str__() + f" | Edicao : {self._edicao}"