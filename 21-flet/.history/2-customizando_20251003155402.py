# flet run 1-fundamentos.py (Desktop)
# flet run 1-fundamentos.py --web (WEB)

import flet as ft
def main(page : ft.Page):
    page.title = "Flet Example!"
    page.update()

ft.app(target=main)