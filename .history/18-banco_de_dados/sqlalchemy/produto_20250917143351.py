from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Double

db = create_engine("sqlite:///produto.db")

Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Produto(Base):
    
    __tablename__ = "tb_produtos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    qtd_produto = Column(Integer, nullable=False)
    preco_unitario = Column(Double, nullable=False)
    
    def __init__(self, nome, qtd_produto, preco_unitario):
        self.nome = nome
        self.qtd_produto = qtd_produto
        self.preco_unitario = preco_unitario
    
    def __valor_total__(self):
        return self.qtd_produto * self.preco_unitario

Base.metadata.create_all(bind = db)

def adiciona_produto(nome, qtd_produto, preco_unitario):
    produto = Produto(nome, qtd_produto, preco_unitario)
    session.add(produto)
    session.commit()

