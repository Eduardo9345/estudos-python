import pytest
import sqlite3

@pytest.fixture
def db_connection():
    """
    Fixture que configura uma conexão com um banco de dados SQLite
    temporário e garante a limpeza dos recursos após o teste
    """
    
    conn = sqlite3.connect(":memory:") #Cria em memória
    cursor = conn.cursor()
    
    cursor.execute("""
    
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    
    """)
    
    conn.commit()
    
    yield conn, cursor
    
    conn.close()
    
def test_database_insert(db_connection):
    """ 
    Testa a inserção de um usuário na tabela users
    """
    
    conn, cursor = db_connection
    cursor.execute("""
                   INSERT INTO users (name, email)
                   VALUES (?, ?)
                   """, ("joão", "joão@email.com"))
    conn.commit()
    
    cursor.execute(
        """
        SELECT * FROM users WHERE email = ?
        """, ("joão@email.com",)
    )
    user = cursor.fetchone()
    assert(user is not None)
    assert(user[1] == "joão")
    assert(user[2] == "joão@email.com")
    