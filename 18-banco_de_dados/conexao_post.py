import psycopg2


# Conexão com o banco
conn = psycopg2.connect(
    database="postgres",
    user="eduardo",
    password="eduardo",
    host="localhost",
    port="5432"
)



