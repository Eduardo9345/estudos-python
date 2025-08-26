class ItemBiblioteca:

    def __init__(self, titulo, autor, preco):
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
    
    def __str__(self):
        return f"Titulo: {self._titulo} | Autor: {self._autor} | Preco: {self._preco}"