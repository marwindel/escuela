from datetime import datetime

import customtkinter as ctk
from pathlib import Path
from PIL import Image
#from customtkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data.cliente_dao import ClienteDAO
from data.esquema.materiales import Materiales
from data.esquema.aula import Aula
from data.esquema.usuario import Usuario
from src.project.gui.user_gui_custom import AppUser



class VentanaUsuario(ctk.CTkFrame):

    ctk.set_appearance_mode("System")  
    ctk.set_default_color_theme("blue")

    COLOR_VENTANA = "lightblue"

    def __init__(self, master, id_user, **kwargs ):
        super().__init__(master, **kwargs)
        self.id_user = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()


    def configurar_ventana(self):

        self.configure(fg_color="#9CD5FF", corner_radius=15, border_width=2, bg_color="#ECF2F4")


    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = ctk.CTkLabel(self, text="Administrar Usuarios", bg_color="#9CD5FF", font=("Calibri", 32, "bold"), text_color="black")

        etiqueta.grid(row=0, column=0, columnspan=2, pady=20)

    def mostrar_formulario(self):
        
        self.frame_forma = ctk.CTkFrame(self, corner_radius=15, fg_color="#9CD5FF")

        nombre = ctk.CTkLabel(self.frame_forma, text="Nombre y Apellido:", font=("Calibri", 18, "bold"), text_color="black")
        nombre.grid(row=0, column=0, sticky=ctk.W, pady=20, padx=5)
        self.nombre_t =ctk.CTkEntry(self.frame_forma)
        self.nombre_t.grid(row=0, column=1)

        usuario = ctk.CTkLabel(self.frame_forma, text="Usuario:", font=("Calibri", 18, "bold"), text_color="black")
        usuario.grid(row=1, column=0, sticky=ctk.W, pady=20, padx=5)
        self.usuario_t =ctk.CTkEntry(self.frame_forma)
        self.usuario_t.grid(row=1, column=1)

        clave = ctk.CTkLabel(self.frame_forma, text="Contraseña:", font=("Calibri", 18, "bold"), text_color="black")
        clave.grid(row=2, column=0, sticky=ctk.W, pady=20, padx=5)
        self.clave_t =ctk.CTkEntry(self.frame_forma, show="*")
        self.clave_t.grid(row=2, column=1)

        clave2 = ctk.CTkLabel(self.frame_forma, text="Confirmar Contraseña:", font=("Calibri", 18, "bold"), text_color="black")
        clave2.grid(row=3, column=0, sticky=ctk.W, pady=20, padx=5)
        self.clave2_t =ctk.CTkEntry(self.frame_forma, show="*")
        self.clave2_t.grid(row=3, column=1)

        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure(self, background="#9CD5FF",
                              foreground="black", font=("Arial", 12))
        self.frame_tabla = tk.Frame(self)
        self.estilo.configure('Treeview', background='#355872', foreground='white', fieldbackground='#355872', rowheight=35, font=('Calibri', 12))
        self.estilo.configure('Treeview.Heading', background="#E1EDF7", foreground='black', font=('Calibri', 12, 'bold'))

        columnas = ('Id', 'Nombre', 'Usuario')

        self.tabla = ttk.Treeview(self.frame_tabla, columns= columnas, show='headings')

        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.CENTER)
        self.tabla.heading('Usuario', text='Usuario', anchor=tk.CENTER)

    
        self.tabla.column('Id', width=50, anchor=tk.CENTER)
        self.tabla.column('Nombre', width=350,  anchor=tk.CENTER)
        self.tabla.column('Usuario', width=350,  anchor=tk.CENTER)

    

        usuario = ClienteDAO.seleccionarUsuario()

        if not usuario:
            self.tabla.insert(parent='', index=tk.END, values=("(vacio)", "(vacio)", "(vacio)"))
        else: 
            for cliente in usuario:
                self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.nombre, cliente.usuario))


        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.tabla.bind('<<TreeviewSelect>>', self.seleccionar_usuario)


        self.tabla.grid(row=0, column=0)

        self.frame_tabla.grid(row=1, column=1, padx=20, pady=20)

    def mostrar_botones(self):
        self.frame_botones = tk.Frame(self, bg="#9CD5FF")

        insertar_btn = ctk.CTkButton(self.frame_botones, text="Guardar", fg_color="#51D465", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.validar_user)
        insertar_btn.grid(row=0, column=0, padx=10)

        actualizar_btn = ctk.CTkButton(self.frame_botones, text="Limpiar", fg_color="#E6EBE8", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.limpiar_datos)
        actualizar_btn.grid(row=0, column=1, padx=10)

        eliminar_btn = ctk.CTkButton(self.frame_botones, text="Eliminar", fg_color="#AD3131", text_color="white", font=("Calibri", 18, "bold"), border_width=1, command=self.eliminar_user)
        eliminar_btn.grid(row=0, column=2, padx=10)

        
        self.icon_ven = ctk.CTkImage(light_image=Image.open(Path(__file__).parent.parent / "assets" / "icon" / "extraer_ventana.png"), dark_image=Image.open(Path(__file__).parent.parent / "assets" / "icon" / "extraer_ventana.png"), size=(20, 20))
        ventanas_btn = ctk.CTkButton(self.frame_botones, text="", fg_color="#FFFFFF", text_color="black", font=("Calibri", 18, "bold"), border_width=1, image=self.icon_ven, compound="left", command=self.abrir_ventana)
        ventanas_btn.grid(row=1, column=1, pady=(100,0))


        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
    
    def abrir_ventana(self):
        app_aula = AppUser()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()

    def validar_user(self):

        if(self.nombre_t.get() and self.usuario_t.get()):


            if (self.clave_t.get() and self.clave2_t.get()):

                if self.clave_t.get() == self.clave2_t.get():

                    if self.id_user is None:

                        self.guardar_user()
                        messagebox.showinfo("Exito", "Usuario creado exitosamente")
                        self.limpiar_datos()

                    else:

                        self.actualizar_user_clave()
                        messagebox.showinfo("Exito", "Clave actualizarda correctamente")
                        self.limpiar_datos()

                else:
                    messagebox.showerror("Error", "Las contraseñas no coinciden.")
                    self.clave_t.delete(0, tk.END)
                    self.clave2_t.delete(0, tk.END)
                    self.clave_t.focus_set()
            else:
                self.actualizar_user_datos()

        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            self.nombre_t.delete(0, tk.END)
            self.usuario_t.delete(0, tk.END)
            self.clave_t.delete(0, tk.END)
            self.clave2_t.delete(0, tk.END)
            self.nombre_t.focus_set()


    def guardar_user(self):
        nombre = self.nombre_t.get()
        usuario = self.usuario_t.get()
        clave = self.clave_t.get()

        if self.id_user is None:

            users = Usuario(None, nombre, usuario, clave)
            ClienteDAO.insertarUsuario(users)
            

        self.recargar_datos()

    def actualizar_user_datos(self):
        nombre = self.nombre_t.get()
        usuario = self.usuario_t.get()


        if self.id_user:

            users = Usuario(self.id_user, usuario, nombre, None, None)
            ClienteDAO.actualizarUsuarioDatos(users)
            messagebox.showinfo("Éxito", "Datos del usuario actualizados correctamente.")


        self.recargar_datos()

    
    def actualizar_user_clave(self):
        nombre = self.nombre_t.get()
        usuario = self.usuario_t.get()
        clave = self.clave_t.get()

      
        if self.id_user:

            users = Usuario(self.id_user, usuario, nombre, clave, None)
            ClienteDAO.actualizarUsuarioClave(users)
            messagebox.showinfo("Éxito", "Clave del usuario actualizados correctamente marwin.")


        self.recargar_datos()

    def seleccionar_usuario(self, event):
        item_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(item_seleccionado)
        usuarios = elemento['values']

        self.id_user = usuarios[0]
        nombre_t = usuarios[1]
        usuario_t = usuarios[2]



        self.limpiar_datos_formulario()

        self.nombre_t.insert(0, nombre_t)
        self.usuario_t.insert(0, usuario_t)

    def recargar_datos(self):
        self.mostrar_tabla()

        self.limpiar_datos()

    def eliminar_user(self):
        if self.id_user is None:
            messagebox.showerror("Error", "Debes seleccionar un usuario para eliminarlo")

        else:

            validar_usuario = ClienteDAO.userValid(self.id_user)
            if validar_usuario > 0:
                messagebox.showerror("Error", "No se puede eliminar el usuario porque tiene materiales asociados.")
                return
            else:
                usuario = Usuario(self.id_aula, None, None, None, None)
                ClienteDAO.eliminarUsuario(usuario)
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_datos_formulario()
        self.id_aula = None

    def limpiar_datos_formulario(self):
        self.usuario_t.delete(0, tk.END)
        self.clave_t.delete(0, tk.END) 
        self.nombre_t.delete(0, tk.END)
        self.clave2_t.delete(0, tk.END)     
        self.nombre_t.focus_set()


