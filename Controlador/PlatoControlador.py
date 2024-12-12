from Controlador.Controlador import Controlador
from Plato import Plato

class PlatoControlador(Controlador):
    def obtener_platos(self):
        self.cursor.execute("SELECT * FROM plato")
        datos = self.cursor.fetchall()
        platos = []
        if not datos:
            return None
        for dato in datos:
            platos.append(Plato(dato[0], dato[1], dato[2], dato[3]))
        return platos

    def obtener_plato(self, id):
        self.cursor.execute(f"SELECT * FROM plato WHERE id={id}")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        plato = Plato(datos[0], datos[1], datos[2], datos[3])
        return plato
    
    def guardar_plato(self, plato: Plato):
        self.cursor.execute("INSERT INTO plato VALUES (%s, %s, %s, %s)", (plato.id_plato, plato.nombre, plato.precio, plato.descripcion,))
        self.con.commit()
    
    def actualizar_plato(self, plato: Plato):
        self.cursor.execute("DELETE FROM plato WHERE id=%s", (plato.id_plato))
        self.con.commit()
        self.guardar_plato(plato)