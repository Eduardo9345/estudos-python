import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

# Excluindo dados
id = (1, 2)

cursor.execute(
    """
        DELETE from filmes
        WHERE id in (?, ?)
    """,
    id # Parâmetros da query aonde serão adicionados onde tem ?
)

conexao.commit() # Salvar as alterações no banco

conexao.close()