import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

# Inserindo dados
cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Sonic', 2020, 8.0);
    """
)

conexao.commit() # Só salva a alteração no banco quando tudo estiver pronto (ou tudo ou nada)

conexao.close()

print("Dados inseridos na tabela")