import tkinter as tk
from tkinter import ttk


ventana = tk.Tk()

ventana.title("Proyecto Escuela")
ventana.geometry("700x500")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")

def saludar():
    texto = txt1.get()

    print(f"El texto escrito es: {texto}")
    etiquetas2['text'] = texto


etiquetas = tk.Label(ventana, text="Sistema Escolar", bg="lightblue", font=("Calibri", 32), fg="black")
etiquetas.pack(pady=20)

txt1 = ttk.Entry(ventana, font=("Calibri", 14))
txt1.pack(pady=10)

btn1 = ttk.Button(ventana, text="Saludar", command=saludar)
btn1.pack(pady=10)

etiquetas2 = ttk.Label(ventana, text="Aqui")
etiquetas2.pack(pady=10)

ventana.mainloop()