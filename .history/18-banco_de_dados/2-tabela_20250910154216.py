import sqlite3

# 2 - Conectando no BD
conexao = sqlite3.connect('18-banco_de_dados/titulo.db')

# 3 - Criando o cursor (serve para realizar operações no banco)
cursor = conexao.cursor()

# 4 - Criando a tabela
cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)

# 5 - Fecha conexão
conexao.close()
print("Tabela foi criada!")