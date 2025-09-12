import sqlite3

# 1 - Conectar no BD
def conecta_db():
    conexao = sqlite3.connect("./titulo.db")
    return conexao

# 2 - Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conecta_db()

    cursor = conexao.cursor()

    cursor.execute(
        """
            INSERT INTO filmes(nome, ano, nota)
            VALUES ('Sonic', 2020, 8.0);
        """, 
        (nome, ano, nota)
    )
    
    conexao.commit()
    
    conexao.close()

# 3 - Obter os dados
def obter_dados():
    conexao = conecta_db()
    
    cursor = conexao.cursor()
    dados = cursor.execute("SELECT * FROM filmes")
    
    conexao.close()
    
    return dados.fetchall()

