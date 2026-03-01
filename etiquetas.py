import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Proyecto Escuela")
ventana.geometry("700x500")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")


etiquetas = tk.Label(ventana, text="Sistema escolar", bg="lightblue", font=("Arial", 32), fg="black")

etiquetas.pack(pady=20)




ventana.mainloop()