import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

# Lendo os dados
dados = cursor.execute(
    """
    SELECT * FROM filmes
    """
)

print(dados)

conexao.close()