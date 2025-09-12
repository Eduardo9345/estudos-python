# Mapeamento Objeto-Relacional - Usado para usar o banco de dados junto com o paradigma orientado a objetos de forma a não usar SQL no código
# pip install SQLAlchemy

# Configuração inicial

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///banco.db", echo=True)

