import sqlite3

conexao = sqlite3.connect("18-banco_de_dados/titulo.db")

cursor = conexao.cursor()

# Inserindo dados
cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Super Mario Bros', 2022, 9.5);
    """
)

conexao.commit() # Só salva a alteração no banco quando tudo estiver pronto (ou tudo ou nada)

conexao.close()

print("Dados inseridos na tabela")