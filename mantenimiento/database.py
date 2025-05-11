import sqlite3

#clase para manejar la bd
class UsuarioDB:
    def __init__(self,nombre_bd="base_datos.db"):
        self.conexion= sqlite3.connect(nombre_bd)
        self.cursor=self.conexion.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        self.cursor.execute("""
             CREATE TABLE IF NOT EXISTS usuarios(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre TEXT NOT NULL,
                            edad INTEGER NOT NULL)
                            """)
        self.conexion.commit() 

    def insertar(self,nombre,edad):
        self.cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES (?,?)",(nombre,edad))    
        self.conexion.commit()
    def obtener_todos(self):
        self.cursor.execute("SELECT * FROM usuarios")    
        return self.cursor.fetchall()
    
    def eliminar(self,id_usuario):
        self.cursor.execute("DELETE FROM usuarios WHERE id=?",(id_usuario,))
        self.conexion.commit()

    def actualizar(self,id_usuario,nombre,edad):
        self.cursor.execute("UPDATE usuarios SET nombre=?,edad=? WHERE id=?",(nombre,edad,id_usuario))    
        self.conexion.commit()
