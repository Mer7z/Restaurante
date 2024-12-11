__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Mesa:
    """Esta clase representa a los objetos de tipo Mesa.

    Atributos:
        id_mesa (int): Identificador de la mesa.
        cantidad_comensales (int): Número de comensales que puede acomodar la mesa.
        estado (str): Estado actual de la mesa, puede ser "libre" o "ocupada".
    """
    
    def __init__(self, id_mesa, cantidad_comensales, estado="libre"):
        """Método constructor que permite instanciar objetos de tipo Mesa.
        
        Argumentos:
            param1 id_mesa (int): [id_mesa]
            param2 cantidad_comensales (int): [cantidad_comensales]
            param3 estado (str): [estado], por defecto "libre"
        Retornos:
            None
        Excepciones:
            None
        """
        self.id_mesa = id_mesa
        self.cantidad_comensales = cantidad_comensales
        self.estado = estado

    def ocupar_mesa(self):
        """Método que permite ocupar la mesa si está libre.
        
        Argumentos:
            None
        Retornos:
            bool: True si la mesa se ocupa correctamente, False en caso contrario.
        Excepciones:
            None
        """
        if self.estado == "libre":
            self.estado = "ocupada"
            return True
        else:
            print("La mesa ya está ocupada")
            return False

    def liberar_mesa(self):
        """Método que permite liberar la mesa si está ocupada.
        
        Argumentos:
            None
        Retornos:
            bool: True si la mesa se libera correctamente, False en caso contrario.
        Excepciones:
            None
        """
        if self.estado == "ocupada":
            self.estado = "libre"
            return True
        else:
            print("La mesa ya está libre")
            return False
