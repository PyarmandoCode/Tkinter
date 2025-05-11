import tkinter as tk
from interfaz import App
            
#Ejecutar la app
if __name__=="__main__":
    root= tk.Tk()
    #centrar ventana
    ancho_ventana=500
    alto_ventana=400
    #Obtener las dimensiones de la ventana
    ancho_pantalla=root.winfo_screenwidth()
    alto_pantalla=root.winfo_screenheight()

    #Calcular coordenadas x e y
    x=(ancho_pantalla // 2) - (ancho_ventana // 2)
    y=(alto_pantalla //2) - (alto_ventana // 2)
    #Establecer tamaño y posicion de la ventana
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    app=App(root)
    root.mainloop()