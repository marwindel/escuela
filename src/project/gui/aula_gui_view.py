from datetime import datetime

import customtkinter as ctk
#from customtkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from data.cliente_dao import ClienteDAO
from data.esquema.materiales import Materiales
from data.esquema.aula import Aula
from pathlib import Path
from PIL import Image
from src.project.gui.aula_gui_custom import AppAula



class VentanaAula(ctk.CTkFrame):

    ctk.set_appearance_mode("System")  
    ctk.set_default_color_theme("blue")

    COLOR_VENTANA = "lightblue"

    def __init__(self, master, id_user, **kwargs ):
        super().__init__(master, **kwargs )
        self.id_aula = None
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
        etiqueta = ctk.CTkLabel(self, text="Registrar Aulas", bg_color="#9CD5FF", font=("Calibri", 32, "bold"), text_color="black")

        etiqueta.grid(row=0, column=0, columnspan=2, pady=20)

    def mostrar_formulario(self):
        
        self.frame_forma = tk.Frame(self, bg="#9CD5FF")

        grado = ctk.CTkLabel(self.frame_forma, text="Grado:", font=("Calibri", 18, "bold"), text_color="black")
        grado.grid(row=0, column=0, sticky=ctk.W, pady=20, padx=5)
        self.grado_t =ctk.CTkEntry(self.frame_forma)
        self.grado_t.grid(row=0, column=1)

        seccion = ctk.CTkLabel(self.frame_forma, text="Seccion:", font=("Calibri", 18, "bold"), text_color="black")
        seccion.grid(row=1, column=0, sticky=ctk.W, pady=20, padx=5)
        self.seccion_t =ctk.CTkEntry(self.frame_forma)
        self.seccion_t.grid(row=1, column=1)

        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure(self, background="#9CD5FF",
                              foreground="black", font=("Arial", 12))

        self.frame_tabla = tk.Frame(self)
        self.estilo.configure('Treeview', background='#355872', foreground='white', fieldbackground='#355872', rowheight=25, font=('Calibri', 12))
        self.estilo.configure('Treeview.Heading', background="#E1EDF7", foreground='black', font=('Calibri', 12, 'bold'))

        columnas = ('Id', 'Grado', 'Seccion')

        self.tabla = ttk.Treeview(self.frame_tabla, columns= columnas, show='headings')

        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Grado', text='Grado', anchor=tk.CENTER)
        self.tabla.heading('Seccion', text='Seccion', anchor=tk.CENTER)

        self.tabla.column('Id', width=150, anchor=tk.CENTER)
        self.tabla.column('Grado', width=150,  anchor=tk.CENTER)
        self.tabla.column('Seccion', width=150,  anchor=tk.CENTER)

    

        aulas = ClienteDAO.seleccionarAula()

        if not aulas:
            self.tabla.insert(parent='', index=tk.END, values=("(vacio)", "(vacio)", "(vacio)"))
        else: 
            for cliente in aulas:
                self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.grado, cliente.seccion))


        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.tabla.bind('<<TreeviewSelect>>', self.seleccionar_aula)


        self.tabla.grid(row=0, column=0)

        self.frame_tabla.grid(row=1, column=1, padx=20, pady=20)

    def mostrar_botones(self):
        self.frame_botones = tk.Frame(self, bg="#9CD5FF")

        insertar_btn = ctk.CTkButton(self.frame_botones, text="Guardar", fg_color="#51D465", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.validar_aulas)
        insertar_btn.grid(row=0, column=0, padx=10)

        actualizar_btn = ctk.CTkButton(self.frame_botones, text="Limpiar", fg_color="#E6EBE8", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.limpiar_datos)
        actualizar_btn.grid(row=0, column=1, padx=10)

        eliminar_btn = ctk.CTkButton(self.frame_botones, text="Eliminar", fg_color="#AD3131", text_color="white", font=("Calibri", 18, "bold"), border_width=1, command=self.eliminar_aula)
        eliminar_btn.grid(row=0, column=2, padx=10)

        self.icon_ven = ctk.CTkImage(light_image=Image.open(Path(__file__).parent.parent / "assets" / "icon" / "extraer_ventana.png"), dark_image=Image.open(Path(__file__).parent.parent / "assets" / "icon" / "extraer_ventana.png"), size=(20, 20))
        ventanas_btn = ctk.CTkButton(self.frame_botones, text="", fg_color="#FFFFFF", text_color="black", font=("Calibri", 18, "bold"), border_width=1, image=self.icon_ven, compound="left", command=self.abrir_ventana)
        ventanas_btn.grid(row=1, column=1, pady=(100,0))

        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

    def abrir_ventana(self):
        app_aula = AppAula()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()
    
    def validar_aulas(self):

        if(self.grado_t.get() and self.seccion_t.get()):
            if self.validar_cantidad():
                self.guardar_aula()
            else:
                messagebox.showerror("Error", "El valor debe ser un número.")
                self.grado_t.delete(0, tk.END)
                self.grado_t.focus_set()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            self.grado_t.delete(0, tk.END)
            self.seccion_t.delete(0, tk.END) 
            self.grado_t.focus_set()    

    def validar_cantidad(self):
        try:
            int(self.grado_t.get())
            return True

        except ValueError:
            print("El grado debe ser un número.")
            return False

    def guardar_aula(self):
        grado = self.grado_t.get()
        seccion = self.seccion_t.get()

        if self.id_aula is None:

            materiales = Aula(None, grado, seccion)
            ClienteDAO.insertarAula(materiales)
            messagebox.showinfo("Éxito", "Aula guardada correctamente.")


        self.recargar_datos()

    def seleccionar_aula(self, event):
        item_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(item_seleccionado)
        material = elemento['values']

        self.id_aula = material[0]
        grado_t = material[1]
        seccion_t = material[2]


        self.limpiar_datos_formulario()

        self.grado_t.insert(0, grado_t)
        self.seccion_t.insert(0, seccion_t)

    def recargar_datos(self):
        self.mostrar_tabla()

        self.limpiar_datos()

    def eliminar_aula(self):
        if self.id_aula is None:
            messagebox.showerror("Error", "Debes seleccionar un cliente para eliminarlo")

        else:

            validar_aula = ClienteDAO.aulaValid(self.id_aula)
            if validar_aula > 0:
                messagebox.showerror("Error", "No se puede eliminar el aula porque tiene materiales asociados.")
                return
            else:
                material = Aula(self.id_aula, None, None)
                ClienteDAO.eliminarAula(material)
                messagebox.showinfo("Éxito", "Aula eliminada correctamente.")
                self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_datos_formulario()
        self.id_aula = None

    def limpiar_datos_formulario(self):
        self.grado_t.delete(0, tk.END)
        self.seccion_t.delete(0, tk.END)   
        self.grado_t.focus_set()

