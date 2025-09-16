import psycopg2

try:
    # Conexão com o banco
    conn = psycopg2.connect(
        database="postgres",
        user="eduardo",
        password="eduardo",
        host="localhost",
        port="5432"
    )

    # Cria um cursor
    cur = conn.cursor()

    # Executa um comando SQL de teste
    cur.execute("SELECT version();")

    # Pega o resultado
    versao = cur.fetchone()
    print("Versão do PostgreSQL:", versao)

    # Fecha cursor e conexão
    cur.close()
    conn.close()

except Exception as e:
    print("Erro:", e)
