import gradio as gr

def soma(num1, num2):
    return num1 + num2

iface = gr.Interface(
    fn = soma,
    inputs = ["number", "number"],
    outputs = "number",
    title = "Soma números"
)

iface.launch()