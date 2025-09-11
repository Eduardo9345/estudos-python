import streamlit as st

# streamlit biblioteca para criar apps com poucas linhas de código

# streamlit run .\form.py roda a aplicação

st.title("Filmes")

nome = st.text_input("Nome do filme:")

ano = st.number_input("Insira o ano do filme:")