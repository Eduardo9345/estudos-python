import gradio as gr

def converter_temperatura(temperatura, escala):

    if escala == "Celsius":
        return (temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9
