import gradio as gr
import numpy as np
from PIL import Image
import io
import base64

def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo =(
        f"background-color: {cor_fundo};"
        f"color: {cor_texto};"
        f"text-aling: center;"
        f"padding: 20px;"
    )

    imagem_html = ""

    if imagem is not None:
        buffered = io.BytesIO()
        Image.fromarray(imagem).save(buffered)