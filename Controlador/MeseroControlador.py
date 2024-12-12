from Controlador.Controlador import Controlador
from Mesero import Mesero

class MeseroControlador(Controlador):
    def obtener_meseros(self):
        self.cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='mesero'")
        datos = self.cursor.fetchall()
        chefs = []
        if not datos:
            return None
        for dato in datos:
            chefs.append(Mesero(dato[0], dato[1], dato[2], dato[3], dato[4]))
        return chefs

    def obtener_mesero(self, cedula):
        self.cursor.execute(f"SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='mesero' and cedula='{cedula}'")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        mesero = Mesero(datos[0], datos[1], datos[2], datos[3], datos[4])
        return mesero
    
    def guardar_mesero(self, mesero: Mesero):
        self.cursor.execute("INSERT INTO persona (cedula, nombre, apellido, telefono, email, rol) VALUES (%s, %s, %s, %s, %s, %s)", (mesero.cedula, mesero.nombre, mesero.apellido, mesero.telefono, mesero.email, 'mesero',))
        self.con.commit()
    
    def actualizar_mesero(self, mesero: Mesero):
        self.cursor.execute("DELETE FROM persona WHERE rol='mesero' and cedula=%s", (mesero.cedula,))
        self.con.commit()
        self.guardar_mesero(mesero)