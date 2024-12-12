from Controlador.Controlador import Controlador
from Registrador import Registrador

class RegistradorControlador(Controlador):
    def obtener_registradores(self):
        self.cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='registrador'")
        datos = self.cursor.fetchall()
        registradores = []
        if not datos:
            return None
        for dato in datos:
            registradores.append(Registrador(dato[0], dato[1], dato[2], dato[3], dato[4]))
        return registradores

    def obtener_registador(self, cedula):
        self.cursor.execute(f"SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='registrador' and cedula='{cedula}'")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        registrador = Registrador(datos[0], datos[1], datos[2], datos[3], datos[4])
        return registrador
    
    def guardar_registrador(self, registrador: Registrador):
        self.cursor.execute("INSERT INTO persona (cedula, nombre, apellido, telefono, email, rol) VALUES (%s, %s, %s, %s, %s, %s)", (registrador.cedula, registrador.nombre, registrador.apellido, registrador.telefono, registrador.email, 'registrador',))
        self.con.commit()

    def actualizar_registrador(self, registrador: Registrador):
        self.cursor.execute("DELETE FROM persona WHERE rol='registrador' AND cedula=%s", (registrador.cedula))
        self.con.commit()
        self.guardar_registrador(registrador)