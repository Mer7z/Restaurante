from Controlador.Controlador import Controlador
from Cliente import Cliente

class ClienteControlador(Controlador):
    def obtener_clientes(self):
        self.cursor.execute("SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='cliente'")
        datos = self.cursor.fetchall()
        clientes = []
        if not datos:
            return None
        for dato in datos:
            clientes.append(Cliente(dato[0], dato[1], dato[2], dato[3], dato[4]))
        return clientes

    def obtener_cliente(self, cedula):
        self.cursor.execute(f"SELECT cedula, nombre, apellido, telefono, email FROM persona WHERE rol='cliente' and cedula='{cedula}'")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        cliente = Cliente(datos[0], datos[1], datos[2], datos[3], datos[4])
        return cliente
    
    def guardar_clientes(self, cliente: Cliente):
        self.cursor.execute("INSERT INTO persona (cedula, nombre, apellido, telefono, email, rol) VALUES (%s, %s, %s, %s, %s, %s)", (cliente.cedula, cliente.nombre, cliente.apellido, cliente.telefono, cliente.email, 'cliente',))
        self.con.commit()
    
    def actualizar_cliente(self, cliente: Cliente):
        self.cursor.execute("DELETE FROM persona WHERE rol='cliente' cedula=%s", (cliente.cedula))
        self.con.commit()
        self.guardar_clientes(cliente)
    