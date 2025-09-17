from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Double

db = create_engine("sqlite:///18-banco_de_dados/sqlalchemy/produto.db")

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
    
    def get_valor_total(self):
        return self.qtd_produto * self.preco_unitario
    
    def __str__(self):
        return f"{self.nome} Preco: {self.preco_unitario} Quantidade: {self.qtd_produto} Total: {self.get_valor_total()}"

Base.metadata.create_all(bind = db)

def adiciona_produto(nome, qtd_produto, preco_unitario):
    produto = Produto(nome, qtd_produto, preco_unitario)
    session.add(produto)
    session.commit()

def update_produto(id, nome, qtd_produto, preco_unitario):
    produto = get_produto_by_id(id)
    produto.nome = nome
    produto.qtd_produto = qtd_produto
    produto.preco_unitario = preco_unitario
    session.add(produto)
    session.commit()

def delete_produto(id):
    produto = get_produto_by_id(id)
    session.delete(produto)
    session.commit()

def get_produto_by_id(id):
    return session.query(Produto).filter_by(id = id).first()

def get_produto_by_name(name):
    return session.query(Produto).filter_by(name = name).first()

def get_all_produtos_string():
    lista = session.query(Produto).all()
    produtos_str = "Lista produtos:\n"
    [produtos_str + (str(prod), "\n") for prod in lista]
    return produtos_str