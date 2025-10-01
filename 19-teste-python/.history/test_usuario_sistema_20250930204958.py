import pytest
import sqlite3

from usuario_sistema import adicionar_usuario, buscar_usuario

@pytest.mark.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute(
        """
        CREATE TABLE usuarios(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """)
    
    conn.commit()
    yield conn, cursor
    conn.close
    
@pytest.mark.parametrize(
    "id, nome, email, esperado_nome",
    [
        (1, "Alice", "alice@gmail.com", "Alice"),
        (2, "João", "joão@example.com", "João"),
        (3, "José", "jose@example.com", "José"),
        (4, "Carol", "carol@example.com", "Carol")
    ]
)
@pytest.mark.unit
def test_adicionar_usuario(db_connection, id, nome, email, esperado_nome):
    conn, cursor = db_connection
    adicionar_usuario(cursor, id, nome, email)
    resultado = buscar_usuario(cursor, email)
    
    assert(resultado is not None)
    assert(resultado[1] == esperado_nome)