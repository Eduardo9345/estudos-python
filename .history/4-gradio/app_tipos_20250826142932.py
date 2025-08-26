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

iface = gr.Interface(
    fn = processar_dados,
    inputs=[
        gr.Textbox(label="Texto", placeholder = "Digite um texto aqui..."),
        gr.Slider(minimum = 0, maximum = 100, label = "N", value = 0),
        gr.Image(type = "pil", label = "Imagem"),
        gr.Textbox(label= "Lista de Itens", lines=4, placeholder="Item 1\nItem 2"),
        gr.ColorPicker(label="Selecione uma cor"),
        gr.CheckboxGroup(
            choices=["Opção 1", "Opção 2", "Opção 3"],
            label = "Escolha suas opção: "
        )
    ],
    outputs=[
        gr.Textbox(label="Texto revertido"),
        gr.Number(label = "Dobro do número"),
        gr.Textbox(label = "Mensagem sobre a imagem"),
        gr.DataFrame(label="Itens da lista", headers=["Itens"]),
        gr.Textbox(label = "Cor escolhida"),
        gr.Textbox(label = "Opções selecionadas")
    ]
    title = "Verificandor de tipos de entrada e saida"
)

iface.launch()