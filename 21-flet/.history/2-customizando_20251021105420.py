# flet run 1-fundamentos.py (Desktop)
# flet run 1-fundamentos.py --web (WEB)

import flet as ft
def main(page : ft.Page):
    page.title = "Flet Example!"
    # page.bgcolor = "#C79030" ou ft.Colors.{cor}
    page.bgcolor = ft.Colors.GREEN_400
    
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    page.padding = ft.padding.all(100)
    
    page.add(
        ft.Text(value = "Olá mundo!"),
        ft.Container(
            ft.Text(
                value = "Hello World 2",
                bgcolor = "black"
            )
        )
    )
    
    #Desktop
    page.window_height = 300
    page.window_width = 600
    page.window.resizable = False #Não redimensionável
    
    page.update()

ft.app(target=main)