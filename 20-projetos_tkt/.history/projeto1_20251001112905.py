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

# Frames
top_frame = Frame(window,
                  width=310, 
                  height=140,
                  pady=0,
                  padx=0,
                  relief="flat",
                  bg=color2)

top_frame.grid(row=0, column=0)

bottom_frame = Frame(window,
                  width=310, 
                  height=140,
                  pady=0,
                  padx=0,
                  relief="flat",
                  bg=color1)

bottom_frame.grid(row=1, column=0, sticky=NW)

window.mainloop()
