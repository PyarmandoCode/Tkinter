import tkinter as tk
from tkinter import messagebox
from database import UsuarioDB

#clase para la interfaz grafica
class App:
    def __init__(self,root):
        self.root=root
        self.root.title("Mantenimento de Usuarios")
        self.db=UsuarioDB()
        self.id_seleccionado=None
        self.crear_widgtes()

        
    def crear_widgtes(self):    
        frame=tk.Frame(self.root,bg="#ffffff",padx=10,pady=10,relief="groove",bd=2)
        frame.pack(padx=20,pady=20,fill="both",expand=True)

        #Entradas
        tk.Label(frame,text="Nombre:",bg="#ffffff").grid(row=0,column=0,sticky="e",pady=5)
        self.nombre_entry=tk.Entry(frame,width=30)
        self.nombre_entry.grid(row=0,column=1,pady=5)

        tk.Label(frame,text="Edad:",bg="#ffffff").grid(row=1,column=0,sticky="e",pady=5)
        self.edad_entry=tk.Entry(frame,width=30)
        self.edad_entry.grid(row=1,column=1,pady=5)

        btn_frame=tk.Frame(frame,bg="#ffffff")
        btn_frame.grid(row=2,column=0,columnspan=2,pady=10)

        tk.Button(btn_frame,text="Agregar", bg="#4CAF50", fg="white",command=self.agregar_usuarios).grid(row=0,column=0,padx=5)
        tk.Button(btn_frame,text="Actualizar", bg="#4CAF50", fg="white",command=self.actualizar_usuario).grid(row=0,column=1,padx=5)
        tk.Button(btn_frame,text="Eliminar", bg="#4CAF50", fg="white",command=self.eliminar_usuario).grid(row=0,column=2,padx=5)
        tk.Button(btn_frame,text="Limpiar",bg="#4CAF50", fg="white",command=self.limpiar_campos).grid(row=0,column=3,padx=5)
        tk.Button(btn_frame,text="Salir",bg="#4CAF50", fg="white",command=self.confirmar_salida).grid(row=0,column=4,padx=5)

        #Lista
        self.lista=tk.Listbox(frame,width=50)
        self.lista.grid(row=3,column=0,columnspan=3,pady=10)
        self.lista.bind("<<ListboxSelect>>",self.seleccionar_usuario)

        self.refrescar_lista()

    def agregar_usuarios(self):
        nombre= self.nombre_entry.get()
        edad=self.edad_entry.get()
        if nombre and edad.isdigit():
            self.db.insertar(nombre,int(edad))
            self.refrescar_lista()
        else:
            messagebox.showwarning("Advertencia","Datos Invalidos")  
    def refrescar_lista(self):
        self.lista.delete(0,tk.END)
        for usuario in self.db.obtener_todos():
            self.lista.insert(tk.END,f"{usuario[0]} | {usuario[1]} | {usuario[2]}")     

    def seleccionar_usuario(self,event):
        if self.lista.curselection:
            index=self.lista.curselection()[0]             
            datos=self.lista.get(index)
            partes=datos.split(" | ")
            self.id_seleccionado=int(partes[0])
            self.nombre_entry.delete(0,tk.END)
            self.nombre_entry.insert(0,partes[1])
            self.edad_entry.delete(0,tk.END)
            self.edad_entry.insert(0,partes[2])

    def eliminar_usuario(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertercias","Seleccione un usuario para eliminar")        
            return
        confirm=messagebox.askyesno("Confirmar","¿Estas seguro de eliminar este usuario?")
        if confirm:
            self.db.eliminar(self.id_seleccionado)
            self.refrescar_lista()
            self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_entry.delete(0,tk.END)        
        self.edad_entry.delete(0,tk.END)        
        self.id_seleccionado=None

    def actualizar_usuario(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertercias","Seleccione un usuario para Actualizar")        
            return
        nombre=self.nombre_entry.get().strip()
        edad=self.edad_entry.get().strip()
        if nombre and edad.isdigit():
            self.db.actualizar(self.id_seleccionado,nombre,edad)
            self.refrescar_lista()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia","Nombre o edad son invalidos")  

    def confirmar_salida(self):
        respuesta = messagebox.askyesno("Confirmar Salida","¿Estas Seguro de Salir"
                                        )          
        if respuesta:
            self.root.destroy()
