from datetime import datetime
import customtkinter as ctk
#from customtkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from escuela.cliente_dao import ClienteDAO
from escuela.materiales import Materiales
from aula_gui_custom import AppAula
import ctypes 

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception as e:
    print(f"No se pudo ajustar el DPI: {e}")

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class App(ctk.CTk, tk.Tk):

    COLOR_VENTANA = "lightblue"

    def __init__(self):
        super().__init__()
        self.id_material = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()
        self.mostrar_btn_aula()


    def configurar_ventana(self):

        self.title("Proyecto Escuela")
        self.geometry("1300x600")
        self.resizable(0, 0)
        self.config(bg="#9CD5FF")

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure(self, background="#9CD5FF",
                              foreground="black", font=("Arial", 12))


    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

    def mostrar_titulo(self):
        etiqueta = ctk.CTkLabel(self, text="Sistema escolar", bg_color="#9CD5FF", font=("Calibri", 48, "bold"), text_color="black")

        etiqueta.grid(row=0, column=0, columnspan=2, pady=20)

    def mostrar_formulario(self):
        
        self.frame_forma = tk.Frame(self, bg="#9CD5FF")

        descripcion = ctk.CTkLabel(self.frame_forma, text="Descripcion:", font=("Calibri", 18, "bold"), text_color="black")
        descripcion.grid(row=0, column=0, sticky=ctk.W, pady=20, padx=5)
        self.descripcion_t =ctk.CTkEntry(self.frame_forma)
        self.descripcion_t.grid(row=0, column=1)

        cantidad = ctk.CTkLabel(self.frame_forma, text="Cantidad:", font=("Calibri", 18, "bold"), text_color="black")
        cantidad.grid(row=1, column=0, sticky=ctk.W, pady=20, padx=5)
        self.cantidad_t =ctk.CTkEntry(self.frame_forma)
        self.cantidad_t.grid(row=1, column=1)

        registrado_por = ctk.CTkLabel(self.frame_forma, text="Registrado por:", font=("Calibri", 18, "bold"), text_color="black")
        registrado_por.grid(row=2, column=0, sticky=ctk.W, pady=20, padx=5)
        self.registrado_por_t =ctk.CTkEntry(self.frame_forma)
        self.registrado_por_t.grid(row=2, column=1)

        aula = ctk.CTkLabel(self.frame_forma, text="Aula:", font=("Calibri", 18, "bold"), text_color="black")
        aula.grid(row=3, column=0, sticky=ctk.W, pady=20, padx=5)

        aulas = ClienteDAO.seleccionarAula()

        texto_alineado = []
        for aula in aulas:
            texto_alineado.append(aula.grado + "-" + aula.seccion)

        self.aula_t = ctk.CTkComboBox(self.frame_forma, values=texto_alineado)
        self.aula_t['state'] = 'readonly'
        self.aula_t.grid(row=3, column=1)


        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):

        self.frame_tabla = tk.Frame(self)
        self.estilo.configure('Treeview', background='#355872', foreground='white', fieldbackground='#355872', rowheight=40, font=('Calibri', 12))
        self.estilo.configure('Treeview.Heading', background="#E1EDF7", foreground='black', font=('Calibri', 12, 'bold'))

        columnas = ('Id', 'Descripcion', 'Cantidad', 'Registrado_por', 'Fecha_creacion', 'Fecha_Actualizacion', 'Grado', 'Seccion')

        self.tabla = ttk.Treeview(self.frame_tabla, columns= columnas, show='headings')

        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Descripcion', text='Descripcion', anchor=tk.W)
        self.tabla.heading('Cantidad', text='Cantidad', anchor=tk.W)
        self.tabla.heading('Registrado_por', text='Registrado por', anchor=tk.W)
        self.tabla.heading('Fecha_creacion', text='Fecha creacion', anchor=tk.W)
        self.tabla.heading('Fecha_Actualizacion', text='Fecha Actualizacion', anchor=tk.W)
        self.tabla.heading('Grado', text='Grado', anchor=tk.W)
        self.tabla.heading('Seccion', text='Seccion', anchor=tk.W)

        self.tabla.column('Id', width=50, anchor=tk.CENTER)
        self.tabla.column('Descripcion', width=130,  anchor=tk.W)
        self.tabla.column('Cantidad', width=100,  anchor=tk.CENTER)
        self.tabla.column('Registrado_por', width=160,  anchor=tk.W)
        self.tabla.column('Fecha_creacion', width=160,  anchor=tk.W)
        self.tabla.column('Fecha_Actualizacion', width=190,  anchor=tk.W)
        self.tabla.column('Grado', width=80,  anchor=tk.CENTER)
        self.tabla.column('Seccion', width=90,  anchor=tk.CENTER)

    

        clientes = ClienteDAO.seleccionar()

        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.descripcion, cliente.cantidad, cliente.registrado_por, cliente.fecha_creacion, cliente.fecha_actualizacion, cliente.grado, cliente.seccion))


        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.tabla.bind('<<TreeviewSelect>>', self.seleccionar_material)


        self.tabla.grid(row=0, column=0)

        self.frame_tabla.grid(row=1, column=1, padx=20, pady=20)

    def mostrar_botones(self):
        self.frame_botones = tk.Frame(self, bg="#9CD5FF")

        self.estilo.configure("Aceptar.TButton", background="#49CD4D", foreground="black")
        self.estilo.configure("Peligro.TButton", background="red", foreground="white")


        insertar_btn = ctk.CTkButton(self.frame_botones, text="Guardar", fg_color="#51D465", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.validar_materiales)
        insertar_btn.grid(row=0, column=0, padx=10)

        actualizar_btn = ctk.CTkButton(self.frame_botones, text="Limpiar", fg_color="#E6EBE8", text_color="black", font=("Calibri", 18, "bold"), border_width=1, command=self.limpiar_datos)
        actualizar_btn.grid(row=0, column=1, padx=10)

        eliminar_btn = ctk.CTkButton(self.frame_botones, text="Eliminar", fg_color="#AD3131", text_color="white", font=("Calibri", 18, "bold"), border_width=1, command=self.eliminar_material)
        eliminar_btn.grid(row=0, column=2, padx=10)

        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
    
    def mostrar_btn_aula(self):
        self.frame_aula = ctk.CTkFrame(self, width=300, height=200, border_width=3)
        #self.frame_aula.pack(pady=10, padx=10, fill="both", expand=True)

        self.frame_aula.grid_columnconfigure(0, weight=1)
        self.frame_aula.grid_rowconfigure(0, weight=1)

        # 3. Crear el botón y colocarlo en la posición (0,0)
        boton_central = ctk.CTkButton(self.frame_aula, text="Registar Aulas", width=250, height=50, fg_color="#355872", text_color="white", font=("Calibri", 18, "bold"), border_width=1, command=self.abrir_v_aula)
        boton_central.grid(row=0, column=0)

        self.frame_aula.grid(row=3, column=0, columnspan=2, pady=30)

    def validar_materiales(self):

        if(self.descripcion_t.get() and self.cantidad_t.get() and self.registrado_por_t.get() and self.aula_t.get()):
            if self.validar_cantidad():
                self.guardar_material()
            else:
                messagebox.showerror("Error", "El valor debe ser un número.")
                self.cantidad_t.delete(0, tk.END)
                self.cantidad_t.focus_set()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            self.cantidad_t.delete(0, tk.END)
            self.descripcion_t.delete(0, tk.END)
            self.registrado_por_t.delete(0, tk.END)    
            self.descripcion_t.focus_set()    

    def abrir_v_aula(self):
        # self.withdraw()  # Oculta la ventana actual
        app_aula = AppAula()  # Crea una instancia de la nueva ventana
        app_aula.mainloop()  # Inicia el bucle de eventos de la nueva ventana
        # self.deiconify()  # Vuelve a mostrar la ventana actual cuando se cierra la nueva ventana


    def validar_cantidad(self):
        try:
            int(self.cantidad_t.get())
            return True

        except ValueError:
            print("La cantidad debe ser un número.")
            return False

    def guardar_material(self):
        desc = self.descripcion_t.get()
        cant = int(self.cantidad_t.get())
        reg_por = self.registrado_por_t.get()

        aula_seleccionada = self.aula_t.get()
        id_aula = ClienteDAO.aulaSelect(aula_seleccionada)

        ahora = datetime.now()
        fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
        fecha_creacion = fecha_actualizacion = fecha_formateada

        if self.id_material is None:


            materiales = Materiales(None, desc, cant, id_aula, reg_por, fecha_creacion, fecha_actualizacion)
            ClienteDAO.insertarMat(materiales)
            messagebox.showinfo("Éxito", "Material guardado correctamente.")

        else:

            materiales = Materiales(self.id_material, desc, cant, id_aula, reg_por, fecha_creacion, fecha_actualizacion)
            ClienteDAO.actualizar(materiales)
            messagebox.showinfo("Éxito", "Material actualizado correctamente.")


        self.recargar_datos()

    def seleccionar_material(self, event):
        item_seleccionado = self.tabla.selection()[0]
        elemento = self.tabla.item(item_seleccionado)
        material = elemento['values']

        self.id_material = material[0]
        descripcion_t = material[1]
        cantidad_t = material[2]
        registrador_por_t = material[3]
        aula_t = str(material[6]) + "-" + material[7]

        self.limpiar_datos_formulario()

        self.descripcion_t.insert(0, descripcion_t)
        self.cantidad_t.insert(0, cantidad_t)
        self.registrado_por_t.insert(0, registrador_por_t)
        self.aula_t.set(aula_t)

    def recargar_datos(self):
        self.mostrar_tabla()

        self.limpiar_datos()

    def eliminar_material(self):
        if self.id_material is None:
            messagebox.showerror("Error", "Debes seleccionar un cliente para eliminarlo")

        else:
            material = Materiales(self.id_material, None, None, None, None, None, None)
            ClienteDAO.eliminarMat(material)
            messagebox.showinfo("Éxito", "Material eliminado correctamente.")
            self.recargar_datos()

    def limpiar_datos(self):
        self.limpiar_datos_formulario()
        self.id_material = None

    def limpiar_datos_formulario(self):
        self.descripcion_t.delete(0, tk.END)
        self.cantidad_t.delete(0, tk.END)
        self.registrado_por_t.delete(0, tk.END)       
        self.descripcion_t.focus_set()



if __name__ == "__main__":
    app = App()
    app.mainloop()
