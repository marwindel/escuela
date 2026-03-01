import tkinter as tk
from tkinter import ttk
from escuela.cliente_dao import ClienteDAO


class App(tk.Tk):

    COLOR_VENTANA = "lightblue"

    def __init__(self):
        super().__init__()

        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.mostrar_tabla()
        self.mostrar_botones()


    def configurar_ventana(self):

        self.title("Proyecto Escuela")
        self.geometry("1200x600")
        self.resizable(0, 0)
        self.config(bg="#9CD5FF")

        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")
        self.estilo.configure(self, background="#9CD5FF",
                              foreground="black", font=("Arial", 12))


    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
        etiqueta = tk.Label(self, text="Sistema escolar", bg="#9CD5FF", font=("Calibri", 32), fg="black")

        etiqueta.grid(row=0, column=0, columnspan=2, pady=20)

    def mostrar_formulario(self):
        
        self.frame_forma = ttk.Frame()

        descripcion = ttk.Label(self.frame_forma, text="Descripcion:")
        descripcion.grid(row=0, column=0, sticky=tk.W, pady=20, padx=5)
        self.descripcion_t =ttk.Entry(self.frame_forma)
        self.descripcion_t.grid(row=0, column=1)

        cantidad = ttk.Label(self.frame_forma, text="Cantidad:")
        cantidad.grid(row=1, column=0, sticky=tk.W, pady=20, padx=5)
        self.cantidad_t =ttk.Entry(self.frame_forma)
        self.cantidad_t.grid(row=1, column=1)

        registrado_por = ttk.Label(self.frame_forma, text="Registrado por:")
        registrado_por.grid(row=2, column=0, sticky=tk.W, pady=20, padx=5)
        self.registrado_por_t =ttk.Entry(self.frame_forma)
        self.registrado_por_t.grid(row=2, column=1)

        aula = ttk.Label(self.frame_forma, text="Aula:")
        aula.grid(row=3, column=0, sticky=tk.W, pady=20, padx=5)

        aulas = ClienteDAO.seleccionarAula()
        

        self.aula_t = ttk.Combobox(self.frame_forma, values=aulas)
        self.aula_t['state'] = 'readonly'
        self.aula_t.grid(row=3, column=1)


        self.frame_forma.grid(row=1, column=0)

    def mostrar_tabla(self):

        self.frame_tabla = ttk.Frame(self)
        self.estilo.configure('Treeview', background='#355872', foreground='white', fieldbackground='#355872', rowheight=20, font=('Calibri', 12))
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
        self.tabla.column('Descripcion', width=100, anchor=tk.W)
        self.tabla.column('Cantidad', width=70, anchor=tk.W)
        self.tabla.column('Registrado_por', width=100, anchor=tk.W)
        self.tabla.column('Fecha_creacion', width=130, anchor=tk.W)
        self.tabla.column('Fecha_Actualizacion', width=130, anchor=tk.W)
        self.tabla.column('Grado', width=50, anchor=tk.W)
        self.tabla.column('Seccion', width=60, anchor=tk.W)

    

        clientes = ClienteDAO.seleccionar()

        for cliente in clientes:
            self.tabla.insert(parent='', index=tk.END, values=(cliente.id, cliente.descripcion, cliente.cantidad, cliente.registrado_por, cliente.fecha_creacion, cliente.fecha_actualizacion, cliente.grado, cliente.seccion))


        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)

        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        self.tabla.grid(row=0, column=0)

        self.frame_tabla.grid(row=1, column=1, padx=20)

    def mostrar_botones(self):
        self.frame_botones = ttk.Frame(self)

        self.estilo.configure("Aceptar.TButton", background="#49CD4D", foreground="black")
        self.estilo.configure("Peligro.TButton", background="red", foreground="white")


        insertar_btn = ttk.Button(self.frame_botones, text="Guardar", style="Aceptar.TButton")
        insertar_btn.grid(row=0, column=0, padx=10)

        actualizar_btn = ttk.Button(self.frame_botones, text="Actualizar", style="Aceptar.TButton")
        actualizar_btn.grid(row=0, column=1, padx=10)

        eliminar_btn = ttk.Button(self.frame_botones, text="Eliminar", style="Peligro.TButton"  )
        eliminar_btn.grid(row=0, column=2, padx=10)

        self.frame_botones.grid(row=2, column=0, columnspan=2, pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
