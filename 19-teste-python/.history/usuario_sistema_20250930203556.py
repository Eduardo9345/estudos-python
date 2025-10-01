def adicionar_usuario(cursor, id, nome, email):
    """Adiciona um usuario ao banco de dados"""
    cursor.execute(
        '''
            INSERT INTO usuarios(id, nome, email)
            VALUES (?, ?, ?)
        ''', (id, nome, email))
