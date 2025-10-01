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
    "id, nome, email"
)