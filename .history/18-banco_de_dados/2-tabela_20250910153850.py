import sqlite3

# 2 - Conectando no BD
conexao = sqlite3.connect('18-banco_de_dados/titulo.db')

# 3 - Criando o cursor (serve para realizar operações no banco)
cursor = conexao.cursor()