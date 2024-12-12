from Controlador.Controlador import Controlador
from Chef import Chef

class ChefControlador(Controlador):
    def obtener_chefs(self):
        self.cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='chef'")
        datos = self.cursor.fetchall()
        chefs = []
        if not datos:
            return None
        for dato in datos:
            chefs.append(Chef(dato[0], dato[1], dato[2], dato[3], dato[4]))
        return chefs

    def obtener_chef(self, cedula):
        self.cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='chef' and cedula=%s", (cedula,))
        datos = self.cursor.fetchone()
        if not datos:
            return None
        chef = Chef(datos[0], datos[1], datos[2], datos[3], datos[4])
        return chef
    
    def guardar_chef(self, chef: Chef):
        self.cursor.execute("INSERT INTO persona (cedula, nombre, apellido, telefono, email, rol) VALUES (%s, %s, %s, %s, %s, %s)", (chef.cedula, chef.nombre, chef.apellido, chef.telefono, chef.email, 'chef',))
        self.con.commit()
    
    def actualizar_chef(self, chef: Chef):
        self.cursor.execute("DELETE FROM persona WHERE rol='chef' cedula=%s", (chef.cedula,))
        self.con.commit()
        self.guardar_chef(chef)