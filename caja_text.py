import customtkinter as ctk
import tkinter as tk
import subprocess
from tkinter import ttk
from datetime import datetime


ventana = ctk.CTk()

ventana.title("Configurar fecha y hora")
ventana.geometry("400x500")
ventana.resizable(0, 0)
ventana.config(bg="lightblue")

def saludar():
    texto_fecha = fecha.get()
    hora_texto = hora.get()

    try:
        validar_fecha = datetime.strptime(texto_fecha, "%d/%m/%Y")
        validar_hora = datetime.strptime(hora_texto, "%H:%M:%S")

        print(f"Fecha válida: {validar_fecha.strftime('%d/%m/%Y')}")
        print(f"Hora válida: {validar_hora.strftime('%H:%M:%S')}")

        etiquetas2.configure(text="Fecha y hora valida, Configurando la impresora...")

        #preparar el comando de fecha para windows

        datos = texto_fecha.split("/")
        dia = datos[0].strip()
        mes = datos[1].strip()
        year = datos[2].strip()
        year2 = year[-2:]

        # 1. Definimos la ruta del programa (usa 'r' para evitar problemas con \)
        ruta_exe = r"C:\IntTFHKA\IntTFHKA.exe SendCmd(PG"+ str(dia) + str(mes) + str(year2) +")" 

        # 2. Definimos el argumento (lo que va dentro de SendCmd)
        argumento = f'SendCmd("PG{dia}{mes}{year2}")'

       # resultado = subprocess.run([ruta_exe, argumento], capture_output=True, text=True, check=True)
        resultado = subprocess.run(ruta_exe)


        with open(r"C:\IntTFHKA\Status_Error.txt", "r", encoding="utf-8") as archivo:
            # Leemos la primera línea y quitamos espacios en blanco
            contenido = archivo.readline().strip()
            
            # Dividimos por espacios/tabulaciones: "TRUE 0 0" -> ["TRUE", "0", "0"]
            partes = contenido.split()
            
            if not partes:
                return "vacio"

            estado = partes[0] # Tomamos la primera palabra (TRUE o FALSE)
            
            if estado == "TRUE":
                etiquetas3.configure(text=f"Fecha configurada", bg_color="green", text_color="white")
                
            else:
                etiquetas3.configure(text=f"Fecha no configurada", bg_color="red", text_color="white")
                


        

        # Imprimimos la salida
       # print(resultado.stdout)

        # preparar el comando de hora para windows

        datos_hora = hora_texto.split(":")
        hora1 = datos_hora[0].strip()
        minuto = datos_hora[1].strip()
        segundo = datos_hora[2].strip()

        comando_hora = f'SendCmd("PF{hora1}{minuto}{segundo}")'

        # Ejecutamos el comando 
        ruta_exe2 = r"C:\IntTFHKA\IntTFHKA.exe SendCmd(PF"+ str(hora1) + str(minuto) + str(segundo) +")" 

     
        resultado2 = subprocess.run(ruta_exe2)

        with open(r"C:\IntTFHKA\Status_Error.txt", "r", encoding="utf-8") as archivo:
            # Leemos la primera línea y quitamos espacios en blanco
            contenido = archivo.readline().strip()
            
            # Dividimos por espacios/tabulaciones: "TRUE 0 0" -> ["TRUE", "0", "0"]
            partes = contenido.split()
            
            if not partes:
                return "vacio"

            estado = partes[0] # Tomamos la primera palabra (TRUE o FALSE)
            
            if estado == "TRUE":
                etiquetas4.configure(text="Hora configurada", bg_color="green", text_color="white")
  
            else:
                etiquetas4.configure(text="Hora no configurada", bg_color="red", text_color="white")
                    
       
       
        


    except ValueError:
        print("¡Formato de fecha incorrecto o de hora!")



def format_date(event):
    # Obtener el texto actual
    text = fecha.get()
    
    # Si el usuario está borrando, no hacemos nada
    if event.keysym == "BackSpace":
        return

    # Auto-insertar las barras de fecha
    if len(text) == 2 or len(text) == 5:
        fecha.insert(ctk.END, "/")
    
    # Limitar a 10 caracteres (DD/MM/AAAA)
    if len(text) >= 10:
        fecha.delete(10, ctk.END)

def format_hora(event):
    # Obtener el texto actual
    text = hora.get()
    
    # Si el usuario está borrando, no hacemos nada
    if event.keysym == "BackSpace":
        return

    # Auto-insertar las barras de fecha
    if len(text) == 2 or len(text) == 5:
        hora.insert(ctk.END, ":")
    
    # Limitar a 10 caracteres (DD/MM/AAAA)
    if len(text) >= 10:
        hora.delete(10, ctk.END)

etiquetas = ctk.CTkLabel(ventana, text="Farmasi", bg_color="lightblue", font=("Calibri", 32))
etiquetas.pack(pady=20)

fecha_label = ctk.CTkLabel(ventana, text="Fecha:", bg_color="lightblue", font=("Calibri", 14, "bold"))
fecha_label.pack(pady=5)
fecha = ctk.CTkEntry(ventana, font=("Calibri", 14), bg_color="lightblue", placeholder_text="DD/MM/AAAA")
fecha.pack(pady=5)

fecha.bind("<KeyRelease>", format_date)

hora_label = ctk.CTkLabel(ventana, text="Hora:", bg_color="lightblue", font=("Calibri", 14, "bold"))
hora_label.pack(pady=5)
hora = ctk.CTkEntry(ventana, font=("Calibri", 14), bg_color="lightblue", placeholder_text="HH:MM:SS")
hora.pack(pady=5)

hora.bind("<KeyRelease>", format_hora)

btn1 = ctk.CTkButton(ventana, text="Enviar", command=saludar, bg_color="lightblue")
btn1.pack(pady=10)



etiquetas2 = ctk.CTkLabel(ventana, text="")
etiquetas2.pack(pady=5)
etiquetas3 = ctk.CTkLabel(ventana, text="")
etiquetas3.pack(pady=5)
etiquetas4 = ctk.CTkLabel(ventana, text="")
etiquetas4.pack(pady=5)

ventana.mainloop()