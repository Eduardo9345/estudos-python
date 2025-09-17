from sqlalchemy import create_engine # Criar o banco vazio ou conecta com um existente (Varia de cada banco)

from sqlalchemy.orm import sessionmaker, declarative_base # Criador de sessoes e ocriador de tabelas

#Sqlite
db = create_engine("sqlite:///meubanco.db")

#Postgres
# db = create_engine("postgresql+psycopg2://user:senha@localhost:5432/meubanco") precisa do driver psycopg2

# Toda edição no banco ocorre em uma sessão e commita ela
Session = sessionmaker(bind = db) # bind é o db
session = Session() # Carrega a sessão em uma variável