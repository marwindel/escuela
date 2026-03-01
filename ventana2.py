import tkinter as tk
from tkinter import font

root = tk.Tk()

# Obtener todas las familias de fuentes disponibles
fuentes_disponibles = font.families()

# Imprimirlas en orden alfabético
for f in sorted(fuentes_disponibles):
    print(f)

root.withdraw()