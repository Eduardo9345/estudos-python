import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
