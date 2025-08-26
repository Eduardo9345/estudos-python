from .item_biblioteca import ItemBiblioteca


class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self._isbn = isbn
    
    def __str__(self):
        return super().__str__() + f"| ISBN : {self._isbn}"