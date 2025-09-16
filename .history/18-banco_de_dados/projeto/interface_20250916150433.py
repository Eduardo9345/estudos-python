import streamlit as st

import dados_compras

st.title("Produtos")

nome_produto = st.text_input("Nome do produto:")

preco_produto = st.number_input("Insira o preço do produto:", format="%0.2f")

quantidade = st.number_input("Insira a quantidade do produto:")

btn_adicionar = st.button("Adicionar produto")

if btn_adicionar:
    dados_compras.insere_produto(nome_produto, preco_produto, quantidade)
    st.success("Produto cadastrado!")
    
    
produtos = dados_compras.obter_produtos()

if produtos:
    st.header("Lista de produtos:")
    st.table(produtos)