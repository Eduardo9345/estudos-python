import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

dados = cursor.execute(
    """
    
    """
)

conexao.close()