import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Proyecto Escuela")
ventana.geometry("700x500")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")


etiquetas = tk.Label(ventana, text="Sistema Escolar", bg="lightblue", font=("Calibri", 32), fg="black")
etiquetas.pack(pady=20)

def saludar(nombre):
    print(f"Hola, {nombre}, bienvenido al sistema escolar")

btn1 = ttk.Button(ventana, text="Saludar", command= lambda: saludar('Marwin'))
btn1.pack(pady=20)




ventana.mainloop()