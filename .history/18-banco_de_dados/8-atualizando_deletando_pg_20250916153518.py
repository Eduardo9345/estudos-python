from conexao_post import conn

cursor = conn.cursor()

# sql = """
#     UPDATE games
#     SET NAME = %s
#     WHERE ID = %s
# """

# cursor.execute(sql, ("Fifa", 3))

# conn.commit()
# print("Dados atualizados!")

sql = """
    DELETE FROM games
    WHERE id == %s
"""

cursor.execute(sql, (5, ))
conn.commit()
print("Dados deletados!")