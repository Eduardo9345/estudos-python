import streamlit as st

import dados_compras

st.title("Produtos")

nome_produto = st.text_input("Nome do produto:")

preco_produto = st.number_input("Insira o preço do produto:", format="%0.2f")

quantidade = st.number_input("Insira a quantidade do produto:")