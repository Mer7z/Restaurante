from Comanda import Comanda
from Cliente import Cliente
from SerializadorComanda import SerializadorComanda
from Serializador import Serializador
from Mesa import Mesa
from Controlador.ComandaControlador import ComandaControlador
from Controlador.MesaControlador import MesaControlador

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Mesero:
    """Esta clase representa a los objetos de tipo Mesero.

    Atributos:
        cedula (str): Cédula del mesero.
        nombre (str): Nombre del mesero.
        apellido (str): Apellido del mesero.
        telefono (str): Teléfono del mesero.
        email (str): Correo electrónico del mesero.
        mesas (list): Lista de mesas asignadas al mesero.
        comandas (list): Lista de comandas tomadas por el mesero.
        platos (list): Lista de platos disponibles para las comandas.
        clientes (list): Lista de clientes registrados.
        __serializadorComanda (SerializadorComanda): Objeto para serializar comandas.
        __serializadorClientes (Serializador): Objeto para serializar clientes.
        __serializadorMesa (Serializador): Objeto para serializar mesas.
    """
    
    def __init__(self, cedula, nombre, apellido, telefono, email, mesas=[], comandas=[], platos=[], clientes=[]):
        """Método constructor que permite instanciar objetos de tipo Mesero.
        
        Argumentos:
            param1 cedula (str): [cedula]
            param2 nombre (str): [nombre]
            param3 apellido (str): [apellido]
            param4 telefono (str): [telefono]
            param5 email (str): [email]
            param6 mesas (list): [mesas], por defecto lista vacía
            param7 comandas (list): [comandas], por defecto lista vacía
            param8 platos (list): [platos], por defecto lista vacía
            param9 clientes (list): [clientes], por defecto lista vacía
        Retornos:
            None
        Excepciones:
            None
        """
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.mesas = mesas
        self.comandas = comandas
        self.platos = platos
        self.clientes = clientes
        self.__serializadorComanda = SerializadorComanda()
        self.__serializadorClientes = Serializador("clientes.txt", Cliente, ["str", "str", "str", "str", "str"])
        self.__serializadorMesa = Serializador("mesas.txt", Mesa, ["int", "int", "str"])

    def setMesas(self, mesas):
        """Método que permite establecer la lista de mesas asignadas al mesero.
        
        Argumentos:
            param1 mesas (list): [mesas] lista de mesas asignadas
        Retornos:
            None
        Excepciones:
            None
        """
        self.mesas = mesas
    
    def setComandas(self, comandas):
        """Método que permite establecer la lista de comandas tomadas por el mesero.
        
        Argumentos:
            param1 comandas (list): [comandas] lista de comandas tomadas
        Retornos:
            None
        Excepciones:
            None
        """
        self.comandas = comandas
    
    def setPlatos(self, platos):
        """Método que permite establecer la lista de platos disponibles para las comandas.
        
        Argumentos:
            param1 platos (list): [platos] lista de platos disponibles
        Retornos:
            None
        Excepciones:
            None
        """
        self.platos = platos
    
    def setClientes(self, clientes):
        """Método que permite establecer la lista de clientes registrados.
        
        Argumentos:
            param1 clientes (list): [clientes] lista de clientes registrados
        Retornos:
            None
        Excepciones:
            None
        """
        self.clientes = clientes

    def serializar_mesa(self):
        """Método que serializa la información de las mesas asignadas.
        
        Argumentos:
            None
        Retornos:
            None
        Excepciones:
            None
        """
        mesaCon = MesaControlador()
        for mesa in self.mesas:
            if mesaCon.obtener_mesa(mesa.id_mesa):
                mesaCon.actualizar_mesa(mesa)
            else:
                mesaCon.guardar_mesa(mesa)
        mesaCon.cerrar_con()

    def agregar_mesa(self, mesa):
        """Método que permite agregar una mesa a la lista de mesas asignadas.
        
        Argumentos:
            param1 mesa (Mesa): [mesa] objeto de tipo Mesa a agregar
        Retornos:
            None
        Excepciones:
            None
        """
        self.mesas.append(mesa)
        self.serializar_mesa()

    def consultar_disponibilidad_mesas(self):
        """Método que consulta la disponibilidad de las mesas asignadas.
        
        Argumentos:
            None
        Retornos:
            list: Lista de mesas disponibles
        Excepciones:
            None
        """
        return [mesa for mesa in self.mesas]

    def ocupar_mesa(self, mesa):
        """Método que permite ocupar una mesa si está libre.
        
        Argumentos:
            param1 mesa (Mesa): [mesa] objeto de tipo Mesa a ocupar
        Retornos:
            None
        Excepciones:
            None
        """
        if not mesa:
            return
        if mesa.ocupar_mesa():
            print(f"Se ha ocupado correctamente la mesa {mesa.id_mesa}")
        self.serializar_mesa()

    def liberar_mesa(self, mesa):
        """Método que permite liberar una mesa si está ocupada.
        
        Argumentos:
            param1 mesa (Mesa): [mesa] objeto de tipo Mesa a liberar
        Retornos:
            None
        Excepciones:
            None
        """
        if not mesa:
            return
        if mesa.liberar_mesa():
            print(f"Se ha liberado correctamente la mesa {mesa.id_mesa}")
        self.serializar_mesa()

    def tomar_comanda(self, cedula, id_comanda, id_mesa):
        """Método que permite al mesero tomar una comanda para una mesa ocupada.
        
        Argumentos:
            param1 cedula (str): [cedula] cédula del cliente asociado a la comanda
            param2 id_comanda (int): [id_comanda] identificador de la comanda
            param3 id_mesa (int): [id_mesa] identificador de la mesa donde se toma la comanda
        Retornos:
            str or None: Retorna "no cliente" si no se encuentra el cliente, None si se toma la comanda correctamente.
        Excepciones:
            None
        """
        mesa = self.buscar_mesa(id_mesa)
        if not mesa:
            return "no mesa"
        if mesa.estado == "ocupada":
            cliente = self.buscar_cliente(cedula)
            if not cliente:
                return "no cliente"
            comanda = Comanda(id_comanda, mesa.id_mesa, cliente.cedula)
            self.comandas.append(comanda)
            print(f"Se ha creado la comanda con el id: {comanda.id}")
        else:
            print("La mesa no está ocupada")
            return False
    
    def gestionar_cliente(self, cliente, accion):
        """Método que permite gestionar clientes (crear o eliminar).
        
        Argumentos:
            param1 cliente (Cliente): [cliente] objeto de tipo Cliente a gestionar
            param2 accion (str): [accion] acción a realizar ('crear' o 'eliminar')
        Retornos:
            None
        Excepciones:
            None
        """
        if accion == 'crear':
            self.clientes.append(cliente)
        elif accion == 'eliminar':
            self.clientes.remove(cliente)
        self.serializar_clientes()

    def serializar_clientes(self):
        """Método que serializa la información de los clientes registrados.
        
        Argumentos:
            None
        Retornos:
            None
        Excepciones:
            None
        """
        texto = ""
        for cliente in self.clientes:
            cedula = cliente.cedula
            nombre = cliente.nombre
            apellido = cliente.apellido
            telefono = cliente.telefono
            email = cliente.email
            texto += f"{cedula}\n{nombre}\n{apellido}\n{telefono}\n{email}\n"
        self.__serializadorClientes.escribirTodo(texto)

    def agregar_plato_comanda(self, id_comanda, id_plato):
        """Método que permite agregar un plato a una comanda específica.
        
        Argumentos:
            param1 id_comanda (int): [id_comanda] identificador de la comanda
            param2 id_plato (int): [id_plato] identificador del plato a agregar
        Retornos:
            None
        Excepciones:
            None
        """
        comanda = self.buscar_comanda(id_comanda)
        plato = self.buscar_plato(id_plato)
        if not comanda or not plato:
            return False
        comanda.agregar_plato([plato, 1])
        print(f"Se agregó el plato {plato.id_plato} a la comanda {comanda.id}")

    def eliminar_plato_comanda(self, id_comanda, id_plato):
        """Método que permite eliminar un plato de una comanda específica.
        
        Argumentos:
            param1 id_comanda (int): [id_comanda] identificador de la comanda
            param2 id_plato (int): [id_plato] identificador del plato a eliminar
        Retornos:
            None
        Excepciones:
            None
        """
        comanda = self.buscar_comanda(id_comanda)
        plato = self.buscar_plato(id_plato)
        if not comanda or not plato:
            return False
        comanda.eliminar_plato(plato)
        print(f"Se eliminó el plato {plato.id_plato} de la comanda {comanda.id}")
    
    def cambiar_estado_comanda(self, comanda, estado):
        """Método que permite cambiar el estado de una comanda.
        
        Argumentos:
            param1 comanda (Comanda): [comanda] objeto de tipo Comanda
            param2 estado (str): [estado] nuevo estado de la comanda ("pendiente", "en preparacion", "servido")
        Retornos:
            bool: True si se cambia el estado correctamente, False en caso contrario
        Excepciones:
            None
        """
        return comanda.cambiar_estado(estado)
    
    def calcular_precio_total(self):
        """Método que calcula el precio total de una comanda específica.
        
        Argumentos:
            None
        Retornos:
            None
        Excepciones:
            None
        """
        id_comanda = int(input("Ingrese el id de la comanda: "))
        comanda = self.buscar_comanda(id_comanda)
        if not comanda:
            return
        precio = comanda.precio_total
        print(f"El precio total de la comanda {comanda.id} es de: ${precio}")
    
    def guardar_comanda(self):
        """Método que guarda la información de una comanda en un archivo.
        
        Argumentos:
            None
        Retornos:
            None
        Excepciones:
            None
        """
        id_comanda = int(input("Ingrese el id de la comanda a guardar: "))
        comanda = self.buscar_comanda(id_comanda)
        if not comanda:
            return
        comandaCon = ComandaControlador()
        comandaCon.guardar_comanda(comanda)
    
    def buscar_mesa(self, id_mesa):
        """Método que busca una mesa por su identificador.
        
        Argumentos:
            param1 id_mesa (int): [id_mesa] identificador de la mesa a buscar
        Retornos:
            Mesa or None: Retorna el objeto Mesa si lo encuentra, None si no lo encuentra.
        Excepciones:
            None
        """
        for mesa in self.mesas:
            if mesa.id_mesa == id_mesa:
                return mesa
        print("Mesa no encontrada.")
    
    def buscar_comanda(self, id_comanda):
        """Método que busca una comanda por su identificador.
        
        Argumentos:
            param1 id_comanda (int): [id_comanda] identificador de la comanda a buscar
        Retornos:
            Comanda or None: Retorna el objeto Comanda si lo encuentra, None si no lo encuentra.
        Excepciones:
            None
        """
        for comanda in self.comandas:
            if comanda.id == id_comanda:
                return comanda
        print("Comanda no encontrada.")
    
    def buscar_plato(self, id_plato):
        """Método que busca un plato por su identificador.
        
        Argumentos:
            param1 id_plato (int): [id_plato] identificador del plato a buscar
        Retornos:
            Plato or None: Retorna el objeto Plato si lo encuentra, None si no lo encuentra.
        Excepciones:
            None
        """
        for plato in self.platos:
            if plato.id_plato == id_plato:
                return plato
        print("Plato no encontrado.")
    
    def buscar_cliente(self, cedula):
        """Método que busca un cliente por su cédula.
        
        Argumentos:
            param1 cedula (str): [cedula] cédula del cliente a buscar
        Retornos:
            Cliente or None: Retorna el objeto Cliente si lo encuentra, None si no lo encuentra.
        Excepciones:
            None
        """
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        print("Cliente no encontrado.")
