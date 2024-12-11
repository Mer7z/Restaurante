__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Plato:
    """Clase que representa un plato con atributos básicos."""

    def __init__(self, id_plato, nombre, precio, descripcion, cantidad = 1):
        """Inicializa una nueva instancia de Plato.

        Args:
            id_plato (int): Identificador único del plato.
            nombre (str): Nombre del plato.
            precio (float): Precio del plato.
            descripcion (str): Descripción del plato.
        """
        self.id_plato = id_plato
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad  # Cantidad por defecto es 1
        self.descripcion = descripcion
    
    def set_cantidad(self, cantidad):
        """Establece la cantidad de este plato en la comanda.

        Args:
            cantidad (int): Cantidad de este plato en la comanda.
        Returns:
            None
        """
        self.cantidad = cantidad
