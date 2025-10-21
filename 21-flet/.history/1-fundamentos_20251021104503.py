# flet run 1-fundamentos.py (Desktop)
# flet run 1-fundamentos.py --web (WEB)

import flet as ft

def main(page : ft.Page):
    
    msg = ft.Text(value="Hello World!") # Cria a variável (elemento da página)
    page.add(msg) # Adiciona na página
    
    

ft.app(target=main)