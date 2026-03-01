import customtkinter as ctk

# 1. Configuración de apariencia (Opcional pero recomendado)
ctk.set_appearance_mode("System")  # Modos: "System" (estándar), "Dark", "Light"
ctk.set_default_color_theme("blue") # Temas: "blue" (estándar), "green", "dark-blue"

# 2. Crear la ventana principal
app = ctk.CTk()
app.geometry("400x240")
app.title("Mi App Moderna")

# 3. Añadir widgets
boton = ctk.CTkButton(app, text="Hola Mundo", command=lambda: print("Clic!"))
boton.pack(pady=20)

app.mainloop()