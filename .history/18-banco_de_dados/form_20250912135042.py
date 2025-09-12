import streamlit as st
import dados

# streamlit biblioteca para criar apps com poucas linhas de código

# streamlit run .\form.py roda a aplicação

st.title("Filmes")

nome = st.text_input("Nome do filme:")

ano = st.number_input("Insira o ano do filme:", min_value=2010, max_value=2024)

nota_filme = st.slider("Nota do filme:", min_value=0.0, max_value=10.0)