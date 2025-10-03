# flet run 1-fundamentos.py (Desktop)
# flet run 1-fundamentos.py --web (WEB)

import flet as ft
def main(page : ft.Page):
    page.title = "Flet Example!"
    # page.bgcolor = "#C79030" ou ft.Colors.{cor}
    page.bgcolor = ft.Colors.GREEN_400
    page.update()
    
    page.add(
        ft.Text(value = "Olá mundo!")
    )

ft.app(target=main)