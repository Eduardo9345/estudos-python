from sqlalchemy import create_engine # Criar o banco vazio ou conecta com um existente (Varia de cada banco)

from sqlalchemy.orm import sessionmaker, declarative_base # Criador de sessoes e ocriador de tabelas

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey #, Double

#Sqlite
db = create_engine("sqlite:///meubanco.db")

#Postgres
# db = create_engine("postgresql+psycopg2://user:senha@localhost:5432/meubanco") precisa do driver psycopg2

# Toda edição no banco ocorre em uma sessão e commita ela
Session = sessionmaker(bind = db) # bind é o db
session = Session() # Carrega a sessão em uma variável (é a sessão oficialmente)

# Criar as tabelas
# Sem tabelas
Base = declarative_base() # Base é a superclasse que descreve as tabelas, toda classe que for virar tabela deve herdar de Base
# "Traduz a classe para SQL"

# Tabelas=================================================================================================

class Usuario(Base):
    
    __tablename__ = "usuarios" #Variavel interna de Base
    
    # Todas os atributos viram colunas
    id = Column("id", Integer, primary_key = True, autoincrement = True) # Nome do campo, tipo
    nome = Column("nome", String, nullable = False)
    email = Column("email", String, nullable = False)
    senha = Column("senha", String, nullable = False)
    ativo = Column("ativo", Boolean, nullable = False)
    
    def __init__(self, nome, email, senha, ativo = True): # Construtor declarado
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo

class Livro(Base):
    
    __tablename__ = "livros"
    
    id = Column("id", Integer, primary_key = True, autoincrement = True)
    titulo = Column("titulo", String)
    qtde_paginas = Column("qtde_paginas", Integer)
    dono = Column("dono", ForeignKey("usuarios.id")) # Relacionamento NX1 (um usuario tem vários livros) (chave estrangeira referencia a tabela no bd)
    
    def __init__(self, titulo, qtde_paginas, dono):
        self.titulo = titulo
        self.qtde_paginas = qtde_paginas
        self.dono = dono


Base.metadata.create_all(bind = db) # Cria todas as tabelas armazenadas em Base no banco de dados (db)