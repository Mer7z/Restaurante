from Persona import Persona
from Informe import Informe
from Serializador import Serializador
from Mesa import Mesa
from Mesero import Mesero
from Chef import Chef

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Registrador(Persona):
    """Clase que representa a un Registrador en un sistema de gestión de restaurante.
    Hereda de la clase Persona e incluye métodos para gestionar mesas, meseros, chefs y generar informes diarios.

    Atributos:
        cedula (str): Número de cédula del registrador.
        nombre (str): Nombre del registrador.
        apellido (str): Apellido del registrador.
        telefono (str): Número de teléfono del registrador.
        email (str): Dirección de correo electrónico del registrador.
        mesas (list): Lista que contiene objetos de tipo Mesa.
        meseros (list): Lista que contiene objetos de tipo Mesero.
        chefs (list): Lista que contiene objetos de tipo Chef.
        __serializadorMesa (Serializador): Instancia de Serializador para manejar la serialización de mesas.
        __serializadorMesero (Serializador): Instancia de Serializador para manejar la serialización de meseros.
        __serializadorChef (Serializador): Instancia de Serializador para manejar la serialización de chefs.

    Métodos:
        __init__(self, cedula, nombre, apellido, telefono, email, mesas=[], meseros=[], chefs=[]):
            Constructor de la clase Registrador.
        
        setMesas(self, mesas):
            Establece la lista de mesas del restaurante.
        
        setMeseros(self, meseros):
            Establece la lista de meseros del restaurante.
        
        setChefs(self, chefs):
            Establece la lista de chefs del restaurante.
        
        calcular_precio_total(self, comanda):
            Calcula el precio total de una comanda sumando el precio de todos los platos.

        gestionar_mesas(self, mesa, accion):
            Gestiona las mesas del restaurante (crear, eliminar).

        serializar_mesas(self):
            Serializa las mesas en un archivo de texto.

        gestionar_meseros(self, mesero, accion):
            Gestiona los meseros del restaurante (crear, eliminar).

        serializar_meseros(self):
            Serializa los meseros en un archivo de texto.

        gestionar_chef(self, chef, accion):
            Gestiona los chefs del restaurante (crear, eliminar).

        serializar_chefs(self):
            Serializa los chefs en un archivo de texto.

        generar_informes_diarios(self, informes, fecha, comandas):
            Genera un informe diario sobre las comandas del restaurante.

    """
    def __init__(self, cedula, nombre, apellido, telefono, email, mesas=[], meseros=[], chefs=[]):
        super().__init__(cedula, nombre, apellido, telefono, email)
        self.mesas = mesas
        self.meseros = meseros
        self.chefs = chefs
        self.__serializadorMesa = Serializador("mesas.txt", Mesa, ["int", "int", "str"])
        self.__serializadorMesero = Serializador("meseros.txt", Mesero, ["str", "str", "str", "str", "str"])
        self.__serializadorChef = Serializador("chefs.txt", Chef, ["str", "str", "str", "str", "str"])

    def setMesas(self, mesas):
        """Establece la lista de mesas del restaurante.

        Args:
            mesas (list): Lista de objetos de tipo Mesa.
        """
        self.mesas = mesas

    def setMeseros(self, meseros):
        """Establece la lista de meseros del restaurante.

        Args:
            meseros (list): Lista de objetos de tipo Mesero.
        """
        self.meseros = meseros

    def setChefs(self, chefs):
        """Establece la lista de chefs del restaurante.

        Args:
            chefs (list): Lista de objetos de tipo Chef.
        """
        self.chefs = chefs

    def calcular_precio_total(self, comanda):
        """Calcula el precio total de una comanda sumando el precio de todos los platos.

        Args:
            comanda (Comanda): La comanda de la cual se desea calcular el precio total.

        Returns:
            float: El precio total de la comanda.
        """
        return sum(plato[0].precio * plato[1] for plato in comanda.platos)

    def gestionar_mesas(self, mesa, accion):
        """Gestiona las mesas del restaurante (crear, eliminar).

        Args:
            mesa (Mesa): La mesa a gestionar.
            accion (str): Acción a realizar ('crear' o 'eliminar').
        """
        if accion == 'crear':
            self.mesas.append(mesa)
        elif accion == 'eliminar':
            self.mesas.remove(mesa)
        self.serializar_mesas()

    def serializar_mesas(self):
        """Serializa las mesas en un archivo de texto."""
        texto = ""
        for mesa in self.mesas:
            id = mesa.id_mesa
            comensales = mesa.cantidad_comensales
            estado = mesa.estado
            texto += f"{id}\n{comensales}\n{estado}\n"
        self.__serializadorMesa.escribirTodo(texto)

    def gestionar_meseros(self, mesero, accion):
        """Gestiona los meseros del restaurante (crear, eliminar).

        Args:
            mesero (Mesero): El mesero a gestionar.
            accion (str): Acción a realizar ('crear' o 'eliminar').
        """
        if accion == 'crear':
            self.meseros.append(mesero)
        elif accion == 'eliminar':
            self.meseros.remove(mesero)
        self.serializar_meseros()

    def serializar_meseros(self):
        """Serializa los meseros en un archivo de texto."""
        texto = ""
        for mesero in self.meseros:
            cedula = mesero.cedula
            nombre = mesero.nombre
            apellido = mesero.apellido
            telefono = mesero.telefono
            email = mesero.email
            texto += f"{cedula}\n{nombre}\n{apellido}\n{telefono}\n{email}\n"
        self.__serializadorMesero.escribirTodo(texto)

    def gestionar_chef(self, chef, accion):
        """Gestiona los chefs del restaurante (crear, eliminar).

        Args:
            chef (Chef): El chef a gestionar.
            accion (str): Acción a realizar ('crear' o 'eliminar').
        """
        if accion == 'crear':
            self.chefs.append(chef)
        elif accion == 'eliminar':
            self.chefs.remove(chef)
        self.serializar_chefs()
        
    def serializar_chefs(self):
        """Serializa los chefs en un archivo de texto."""
        texto = ""
        for chef in self.chefs:
            cedula = chef.cedula
            nombre = chef.nombre
            apellido = chef.apellido
            telefono = chef.telefono
            email = chef.email
            texto += f"{cedula}\n{nombre}\n{apellido}\n{telefono}\n{email}\n"
        self.__serializadorChef.escribirTodo(texto)

    def generar_informes_diarios(self, informes, fecha, comandas):
        """Genera un informe diario sobre las comandas del restaurante.

        Args:
            informes (list): Lista de informes existentes.
            fecha (str): Fecha del informe en formato YYYY-MM-DD.
            comandas (list): Lista de comandas del día.

        Returns:
            Informe: Objeto Informe generado para el día.
        """
        cant_comandas = len(comandas)
        precios = []
        for comanda in comandas:
            comanda.calcular_precio_total()
            precios.append(comanda.precio_total)
        total_ganancias = sum(precios)
        promedio_ganancias = total_ganancias / cant_comandas if cant_comandas > 0 else 0
        informe_diario = Informe(len(informes) + 1, fecha, cant_comandas, total_ganancias, promedio_ganancias)
        informes.append(informe_diario)
        return informe_diario
