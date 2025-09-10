import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

# Atualizando dados
id = 1
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Homem Aranha", id) # Parâmetros da query aonde serão adicionados onde tem ?
)

conexao.close()