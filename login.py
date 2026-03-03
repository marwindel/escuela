import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import bcrypt
from escuela_gui_custom import App
from tkinter import messagebox

class LoginApp(ctk.CTk):

# 1. Configuración de apariencia (Opcional pero recomendado)
    ctk.set_appearance_mode("System")  # Modos: "System" (estándar), "Dark", "Light"
    ctk.set_default_color_theme("blue")
    
    def __init__(self):
        super().__init__()
        self.mostrar_login() # Temas: "blue" (estándar), "green", "dark-blue"

    def mostrar_login(self):    # 2. Crear la ventana principal
      #  app = ctk.CTk()
        self.geometry("800x600")
        self.title("Inicio de Sesión")
        self.configure(fg_color="#e2e0e0")
        self.resizable(width=False, height=False) # El fondo gris oscuro de la ventana

        # Crear el cuadro blanco central (el formulario)
        # fg_color="white" le da el fondo blanco
        # corner_radius=10 le da bordes redondeados estéticos
        self.login_frame = ctk.CTkFrame(master=self, width=700, height=500, fg_color="#7AAACE", corner_radius=15, border_width=1.5, border_color="#768896")

        # Centrar el frame usando place
        # relx y rely de 0.5 significan el 50% de la ventana (el centro)
        # anchor="center" asegura que el punto de anclaje sea el centro del frame
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # --- Ejemplo de elementos dentro del cuadro blanco ---
        label = ctk.CTkLabel(self.login_frame, text="Bienvenido", text_color="black", font=("Roboto", 28))
        label.pack(pady=40)

        self.entry_user = ctk.CTkEntry(self.login_frame, placeholder_text="Usuario", width=220)
        self.entry_user.pack(pady=12, padx=70)

        self.entry_pass = ctk.CTkEntry(self.login_frame, placeholder_text="Contraseña", show="*", width=220)
        self.entry_pass.pack(pady=12, padx=70)

        user = self.entry_user.get()
        password = self.entry_pass.get()

        btn_login = ctk.CTkButton(self.login_frame, text="Entrar", width=220, command=lambda: self.autenticacion(user, password))
        btn_login.pack(pady=40)
    
    def autenticacion(self, email, password):
        user = self.entry_user.get()
        password = self.entry_pass.get()

      # print(f"Intentando login con email: {user} y password: {password}")

        if self.validar_login(user, password):
            
            app_p = App()
            app_p.mainloop()
        else:
            messagebox.showerror("Error de Login", "Usuario o clave incorrectos.")
    
    def validar_login(self, email, password):
        
        
        if email == "marwin" and password == "marwin":
            return True
        else:
            return False


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()