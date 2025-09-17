from sqlalchemy import create_engine # Criar o banco vazio ou conecta com um existente

#Sqlite
db = create_engine("sqlite:///meubanco.db")

#Postgres
# db = create_engine("postgresql+psycopg2://user:senha@localhost:5432/meubanco") precisa do driver psycopg2

