# flet run 1-fundamentos.py (Desktop)
# flet run 1-fundamentos.py --web (WEB)

import flet as ft

def main(page : ft.Page):
    t1 =ft.Text(
        value = "Utilizando elemento de texto",
        theme_style = ft.TextThemeStyle.DISPLAY_LARGE
    )
    page.add(t1)
    page.update()

ft.app(target=main)