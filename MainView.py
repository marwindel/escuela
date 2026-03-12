import customtkinter as ctk
from src.project.gui.aula_gui_custom import AppAula
from src.project.gui.escuela_gui_custom import App
from src.project.gui.user_gui_custom import AppUser
from src.project.gui.user_gui_view import VentanaUsuario
from src.project.gui.escuela_gui_view import VentanaMateriales
from src.project.gui.aula_gui_view import VentanaAula
from src.project.gui.grid import Ventana

class MiApp(ctk.CTk):
    def __init__(self, id_user):
        super().__init__()

        # Configuración de la ventana principal
        self.id_user = id_user
        self.title("Panel Principal")
        self.after(0, lambda: self.state('zoomed'))
        self.configure(fg_color="#ECF2F4") # Fondo de la ventana principal

        # Configurar el sistema de cuadrícula (Grid)
        # Columna 0 para sidebar, Columna 1 para panel central
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR (Panel Izquierdo) ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=15, fg_color="#9CD5FF", border_width=2) # Celeste
        self.sidebar.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.sidebar.grid_propagate(False) # Mantiene el ancho fijo

        # Título o botones en el sidebar
        self.label_sidebar = ctk.CTkLabel(self.sidebar, text="Menú", font=("Calibri", 20, "bold"))
        self.label_sidebar.pack(pady=20, padx=10)

        self.btn_1 = ctk.CTkButton(self.sidebar, text="Usuario", fg_color="#355872", hover_color="#538CB2", command=lambda: self.abrir_v(VentanaUsuario))
        self.btn_1.pack(pady=10, padx=20)

        self.btn_2 = ctk.CTkButton(self.sidebar, text="Aula", fg_color="#355872", hover_color="#538CB2", command=lambda: self.abrir_v(VentanaAula))
        self.btn_2.pack(pady=10, padx=20)

        self.btn_3 = ctk.CTkButton(self.sidebar, text="Materiales", fg_color="#355872", hover_color="#538CB2", command=lambda: self.abrir_v(VentanaMateriales))
        self.btn_3.pack(pady=10, padx=20)

        self.btn_4 = ctk.CTkButton(self.sidebar, text="prueba", fg_color="#355872", hover_color="#538CB2", command=lambda: self.abrir_v(Ventana))
        self.btn_4.pack(pady=10, padx=20)

        # --- PANEL CENTRAL ---
        # Usamos un Frame "contenedor" blanco para dejar un margen si deseas, 
        # o directamente el panel celeste.
        self.main_panel = ctk.CTkFrame(self, corner_radius=15, fg_color="#9CD5FF", border_width=2) # Celeste
        self.main_panel.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.frame_actual = None

    def abrir_v(self, clase_frame):
       ## """Limpia el panel central y carga un nuevo frame"""
        
        # 1. Destruir el frame que esté actualmente visible
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        # 2. Instanciar el nuevo frame dentro del contenedor
        self.frame_actual = clase_frame(master=self.main_panel, id_user=self.id_user)
        
        # 3. Empaquetarlo para que ocupe todo el espacio
        self.frame_actual.pack(fill="both", expand=True)
    
    def abrir_v_aula(self):

                # self.withdraw()  # Oculta la ventana actual
        app_aula = AppAula()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()  # Inicia el bucle de eventos de la nueva ventana
        # self.deiconify()  # Vuelve a mostrar la ventana actual cuando se cierra la nueva ventana

    def abrir_v_usuario(self):

                # self.withdraw()  # Oculta la ventana actual
        app_aula = AppUser()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()  # Inicia el bucle de eventos de la nueva ventana
        # self.deiconify()  # Vuelve a mostrar la ventana actual cuando se cierra la nueva ventana

    def abrir_v_materiales(self):


                # self.withdraw()  # Oculta la ventana actual
        app_aula = App()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()  # Inicia el bucle de eventos de la nueva ventana
        # self.deiconify()  # Vuelve a mostrar la ventana actual cuando se cierra la nueva ventana

if __name__ == "__main__":
    app = MiApp()
    app.mainloop()