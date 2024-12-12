from Controlador.Controlador import Controlador
from Mesa import Mesa

class MesaControlador(Controlador):
    def obtener_mesas(self):
        self.cursor.execute("SELECT * FROM mesa")
        datos = self.cursor.fetchall()
        mesas = []
        if not datos:
            return None
        for dato in datos:
            mesas.append(Mesa(dato[0], dato[1], dato[2]))
        return mesas

    def obtener_mesa(self, id):
        self.cursor.execute(f"SELECT * FROM mesa WHERE id={id}")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        mesa = Mesa(datos[0], datos[1], datos[2])
        return mesa
    
    def guardar_mesa(self, mesa: Mesa):
        self.cursor.execute("INSERT INTO mesa VALUES (%s, %s, %s)", (mesa.id_mesa, mesa.cantidad_comensales, mesa.estado,))
        self.con.commit()
    
    def actualizar_mesa(self, mesa: Mesa):
        self.cursor.execute("DELETE FROM mesa WHERE id=%s", (mesa.id_mesa))
        self.con.commit()
        self.guardar_mesa(mesa)