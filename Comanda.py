from Plato import Plato

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Comanda:
    """Esta clase representa a los objetos de tipo Comanda.

    Atributos:
        id (int): Identificador de la comanda.
        mesa (int): Número de la mesa asociada a la comanda.
        platos (list): Lista de platos incluidos en la comanda.
        cliente (Cliente): Cliente asociado a la comanda.
        precio_total (float): Precio total de la comanda.
        estado (str): Estado actual de la comanda.
    """
    
    def __init__(self, id_comanda, mesa, cliente, precio_total=0.0, estado="pendiente", platos=[]):
        """Método constructor que permite instanciar objetos de tipo Comanda.
        
        Argumentos:
            param1 id_comanda (int): [id_comanda]
            param2 mesa (int): [mesa]
            param3 cliente (Cliente): [cliente]
            param4 precio_total (float): [precio_total], por defecto 0.0
            param5 estado (str): [estado], por defecto "pendiente"
            param6 platos (list): [platos], por defecto lista vacía
        Retornos:
            None
        Excepciones:
            None
        """
        self.id = id_comanda
        self.mesa = mesa
        self.platos: list[Plato] = platos
        self.cliente = cliente
        self.precio_total = precio_total
        self.estado = estado

    def agregar_plato(self, plato):
        """Método que permite agregar un plato a la comanda.
        
        Argumentos:
            param1 plato (tuple): [plato] una tupla que contiene el plato y la cantidad.
        Retornos:
            None
        Excepciones:
            None
        """
        self.platos.append(plato)
        self.calcular_precio_total()

    def eliminar_plato(self, id_plato):
        """Método que permite eliminar un plato de la comanda.
        
        Argumentos:
            param1 id_plato (int): [id_plato] el identificador del plato.
        Retornos:
            None
        Excepciones:
            None
        """
        self.platos = [plato for plato in self.platos if plato[0] != id_plato]
        self.calcular_precio_total()

    def calcular_precio_total(self):
        """Método que permite calcular el precio total de la comanda.
        
        Argumentos:
            None
        Retornos:
            None
        Excepciones:
            None
        """
        self.precio_total = sum(plato[0].precio * plato[1] for plato in self.platos)

    def cambiar_estado(self, nuevo_estado):
        """Método que permite cambiar el estado de la comanda.
        
        Argumentos:
            param1 nuevo_estado (str): [nuevo_estado] el nuevo estado de la comanda.
        Retornos:
            bool: True si el estado se cambió correctamente, False en caso contrario.
        Excepciones:
            None
        """
        if nuevo_estado in ["pendiente", "en preparacion", "servido"]:
            self.estado = nuevo_estado
            return True
        else:
            print("Estado no valido")
            return False
