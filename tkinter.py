import tkinter as tk

def saludar():
    nombre = entrada.get()
    edad = entrada.get()
    etiqueta_resultado.config(text=f"Hola{nombre}, tienes{edad}años")
    
    ventana = tk.TK()
    ventana.title("Mi primera app gráfica")
    ventana.geometry("200x200")
    
    etiqueta = tk.Label(ventana,text="Ingresa tu nombre:", bg = "blue")
    etiqueta.pack()

    etiqueta = tk.Label(ventana,text="Ingresa tu edad:", bg = "purple" )
    etiqueta.pack()
    
    entrada = tk.Entry(ventana)
    entrada.pack()
    
    boton = tk.Button(ventana,text="Mostrar saludo",command=saludar,edad)
    boton.pack()
    
    etiqueta_resultado = tk.Label(ventana,text="")
    etiqueta_resultado.pack()
    
    ventana.mainloop()
