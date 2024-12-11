__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Persona:
    """Clase que representa a una persona con atributos básicos."""

    def __init__(self, cedula, nombre, apellido, telefono, email):
        """Inicializa una nueva instancia de Persona.

        Args:
            cedula (str): Cédula de identidad de la persona.
            nombre (str): Nombre de la persona.
            apellido (str): Apellido de la persona.
            telefono (str): Número de teléfono de la persona.
            email (str): Dirección de correo electrónico de la persona.
        """
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
