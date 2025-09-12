# Mapeamento Objeto-Relacional - Usado para usar o banco de dados junto com o paradigma orientado a objetos de forma a não usar SQL no código
# pip install SQLAlchemy

# Configuração inicial (default)

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///18-banco_de_dados/banco.db", echo=True)

Base = declarative_base()

# Herdar de Base faz com que a Classe possa ser convertida em tabela
class Filme(Base):
    __tablename__ = "filmes"
    
    id = Column(Integer, primary_key=True) # Column(tipo de sqlalchemy)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    
# Cria a tabela sem SQL
Base.metadata.create_all(engine)

# Inserir dados
def adiciona_filme(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    filme = Filme(nome=nome, ano=ano, nota=nota)
    
    session.add(filme)
    session.commit()
    session.close()
