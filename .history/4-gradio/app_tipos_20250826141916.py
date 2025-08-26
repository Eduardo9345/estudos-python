import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
    mensagem = "Imagem recebida" if imagem else "Imagem não recebida"


    lista_processada = [[item] for item in lista_texto.splitlines()] if lista_texto else []

    return (
        texto_revertido,
        dobro_numero,
        mensagem,
        lista_processada,
        f"Cor selecionada: {cor}",
        opcoes
    )