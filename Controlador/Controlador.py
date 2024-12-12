from Modelo.Conexion import Conexion

class Controlador():
    def __init__(self):
        self.con = Conexion.crear_conexion()
        if not self.con:
            raise Exception("Error. No se pudo Conectar a la base de datos. Verifique su conexión.")
        
        self.cursor = self.con.cursor()
    
    def cerrar_con(self):
        Conexion.cerrar_conexion(self.con)
