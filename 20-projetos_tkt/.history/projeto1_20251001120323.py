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

# Frames==============================================================================================
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
                  height=250,
                  pady=0,
                  padx=0,
                  relief="flat",
                  bg=color1)

bottom_frame.grid(row=1, column=0, sticky=NW)

# Labels Top Frame==============================================================================
app_calculator = Label(top_frame, text="Calcula idade", width=25, height=1, padx=3,
                       relief="flat", anchor="center", font = ("Ivy 15 bold"),
                       bg=color2, fg=color3)
app_calculator.place(x=0, y=30)

app_of_rage = Label(top_frame, text="Idade", width=25, height=1, padx=0,
                       relief="flat", anchor="center", font = ("Arial 15 bold"),
                       bg=color2, fg=color4)
app_of_rage.place(x=0, y=70)

# Labels Bottom Frame===============================================================================
l_initial_date = Label(bottom_frame, text="Data Inicial: ", height=1, padx=0, pady=0,
                       relief="flat", anchor=NW, font = ("Ivy 9"), bg=color1, fg=color3)
l_initial_date.place(x=50, y=30)

cal_initial_date = DateEntry(bottom_frame, width=10, background='darkblue', foreground='white',
                             borderwidht=2, date_pattern="dd/mm/y", year = 2025)
cal_initial_date.place(x=170, y=30)

l_birth_date = Label(bottom_frame, text="Data Nascimento: ", height=1, padx=0, pady=0,
                       relief="flat", anchor=NW, font = ("Ivy 9"), bg=color1, fg=color3)
l_birth_date.place(x=50, y=70)

cal_birth_date = DateEntry(bottom_frame, width=10, background='darkblue', foreground='white',
                             borderwidht=2, date_pattern="dd/mm/y", year = 2000)
cal_birth_date.place(x=170, y=70)

app_years = Label(bottom_frame, text="27", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 25 bold"), bg=color1, fg=color3)
app_years.place(x=60, y=135)

app_label_years = Label(bottom_frame, text="Years", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 11 bold"), bg=color1, fg=color3)
app_label_years.place(x=50, y=175)

app_months = Label(bottom_frame, text="27", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 25 bold"), bg=color1, fg=color3)
app_months.place(x=140, y=135)

app_label_months = Label(bottom_frame, text="Months", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 11 bold"), bg=color1, fg=color3)
app_label_months.place(x=130, y=175)

app_days = Label(bottom_frame, text="27", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 25 bold"), bg=color1, fg=color3)
app_days.place(x=210, y=135)

app_label_days = Label(bottom_frame, text="Days", height=1, padx=0,
                       relief="flat", anchor="center", font = ("Ivy 11 bold"), bg=color1, fg=color3)
app_label_days.place(x=210, y=175)

# Main loop=========================================================================================
window.mainloop()
