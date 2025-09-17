from sqlalchemy import create_engine # Criar o banco vazio ou conecta com um existente

db = create_engine("sqlite:///meubanco.db")