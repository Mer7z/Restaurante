from Controlador.Controlador import Controlador
from Comanda import Comanda
from Controlador.PlatoControlador import PlatoControlador

class ComandaControlador(Controlador):
    def obtener_comandas(self):
        self.cursor.execute("SELECT * FROM comanda")
        datos = self.cursor.fetchall()
        comandas = []
        if not datos:
            return None
        for dato in datos:
            self.cursor.execute(f"SELECT plato_id, cantidad FROM plato_comanda WHERE comanda_id={dato[0]}")
            datosP = self.cursor.fetchall()
            platos = []
            if len(datosP) > 0:
                platoCon = PlatoControlador()
                for datoP in datosP:
                    plato = platoCon.obtener_plato(datoP[0])
                    plato.set_cantidad(datoP[1])
                    platos.append(plato)
                platoCon.cerrar_con()
            comandas.append(Comanda(id_comanda=dato[0], mesa=dato[1], cliente=dato[2], estado=dato[3], platos=platos))
        return comandas

    def obtener_comanda(self, id):
        self.cursor.execute(f"SELECT * FROM comanda WHERE id='{id}'")
        datos = self.cursor.fetchone()
        if not datos:
            return None
        self.cursor.execute(f"SELECT plato_id, cantidad FROM plato_comanda WHERE comanda_id={datos[0]}")
        datosP = self.cursor.fetchall()
        platos = []
        if len(datosP) > 0:
            platoCon = PlatoControlador()    
            for datoP in datosP:
                plato = platoCon.obtener_plato(datoP[0])
                plato.set_cantidad(datoP[1])
                platos.append(plato)
            platoCon.cerrar_con()
        comanda = Comanda(id_comanda=datos[0], mesa=datos[1], cliente=datos[2], estado=datos[3], platos=platos)
        return comanda
    
    def guardar_comanda(self, comanda: Comanda):
        self.cursor.execute("INSERT INTO comanda VALUES (%s, %s, %s, %s)", (comanda.id, comanda.mesa, comanda.cliente, comanda.estado,))
        self.con.commit()
        for plato in comanda.platos:
            self.cursor.execute("INSERT INTO plato_comanda VALUES (%s, %s, %s)", (comanda.id, plato.id_plato, plato.cantidad,))
            self.con.commit()
    
    def actualizar_comanda(self, comanda: Comanda):
        self.cursor.execute("DELETE FROM plato_comanda WHERE comanda_id=%s", (comanda.id,))
        self.cursor.execute("DELETE FROM comanda WHERE id=%s", (comanda.id,))
        self.con.commit()
        self.guardar_comanda(comanda)