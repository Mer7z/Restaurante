from Persona import Persona

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Cliente(Persona):
    """Esta clase representa a los objetos de tipo Cliente y hereda de la super clase Persona.
    
    Atributos:
        No tiene atributos adicionales, hereda todos los atributos de la clase Persona.
    """
    
    def __init__(self, cedula, nombre, apellido, telefono, email):
        """Método constructor que permite instanciar objetos de tipo Cliente.
        
        Argumentos:
            param1 cedula (str): [cedula]
            param2 nombre (str): [nombre]
            param3 apellido (str): [apellido]
            param4 telefono (str): [telefono]
            param5 email (str): [email]
        Retornos:
            None
        Excepciones:
            None
        """
        super().__init__(cedula, nombre, apellido, telefono, email)
