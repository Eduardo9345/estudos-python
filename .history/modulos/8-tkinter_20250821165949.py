import tkinter as tk

window = tk.Tk()

window.geometry("300x150")
window.title("Gerencia Frases")

frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='x', expand=True)

label = tk.Label(frame, text="Olá Mundo!")
label.pack(fill='x', expand=True)

window.mainloop()