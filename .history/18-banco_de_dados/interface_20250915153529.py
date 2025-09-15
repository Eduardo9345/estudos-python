import tkinter as tk
import orm
from tkinter import messagebox

# Interface gráfica

root = tk.Tk()

root.title("Gerenciador de Filmes")

#Rótulos e campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="ID:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=0, column=1, padx=10, pady=5)


root.mainloop()