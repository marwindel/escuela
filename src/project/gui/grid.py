import customtkinter as ctk

class Ventana(ctk.CTkFrame):
    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)
        self.configure(fg_color="lightblue")

        self.btn1 = ctk.CTkButton(self, text="Boton 1")
        self.btn2 = ctk.CTkButton(self, text="Boton 2")
        self.btn3 = ctk.CTkButton(self, text="Boton 3")

        self.btn1.grid(row=1, column=1, padx=10, pady=10)
        self.btn2.grid(row=1, column=3, padx=10)
        self.btn3.grid(row=1, column=5, padx=10)

