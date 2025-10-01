from tkinter import *
from tkinter import ttk

from tkcalendar import Calendar, DateEntry

from dateutil.relativedelta import relativedelta

from datetime import date

# cores
color1 = "#3b3b3b" # preto / escuro
color2 = "#333333" # preto
color3 = "#FFFFFF" # branco
color4 = "#fcc058" # laranja

window = Tk()

window.title("Calculadora de idade")
window.geometry("310x410")
window.configure(bg=color1)

style = ttk.Style(window)
style.theme_use("clam")

window.mainloop()
