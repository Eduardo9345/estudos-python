import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):

    estilo = (
        f"color: {cor_texto};",
        f"background-color: {cor_fundo};",
        f"font-size: {tamanho_fonte};",
        f"font-family: {estilo_fonte};"
    )

    return f'<div style="{estilo}">{texto}</div>'
