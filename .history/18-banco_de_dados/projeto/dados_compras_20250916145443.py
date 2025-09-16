import sqlite3

def conectar():
    conexao = sqlite3.connect("18-banco_de_dados/projeto/dados.db")
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        """
        CREATE TABLE produtos(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        );
        """
    )
    conexao.close()

def insere_produto(nome, preco, quantidade=0):
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute(
        """
        INSERT INTO produtos(nome, preco, quantidade)
        VALUES (?, ?, ?)
        """, (nome, preco, quantidade)
    )
    
    conexao.commit()
    conexao.close()

