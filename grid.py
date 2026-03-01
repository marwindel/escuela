import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Proyecto Escuela")
ventana.geometry("700x500")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")

btn1 = ttk.Button(ventana, text="Boton 1")
btn2 = ttk.Button(ventana, text="Boton 2")
btn3 = ttk.Button(ventana, text="Boton 3")

btn1.grid(row=1, column=1, padx=10, pady=10)
btn2.grid(row=1, column=3, padx=10)
btn3.grid(row=1, column=5, padx=10)

ventana.mainloop()