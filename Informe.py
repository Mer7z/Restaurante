__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Informe:
    """Esta clase representa a los objetos de tipo Informe.

    Atributos:
        id_informe (int): Identificador del informe.
        fecha_informe (str): Fecha en la que se generó el informe.
        cant_comandas (int): Cantidad de comandas registradas en el informe.
        total_ganancias (float): Total de ganancias registradas en el informe.
        promedio_ganancias (float): Promedio de ganancias por comanda en el informe.
    """
    
    def __init__(self, id_informe, fecha_informe, cant_comandas, total_ganancias, promedio_ganancias):
        """Método constructor que permite instanciar objetos de tipo Informe.
        
        Argumentos:
            param1 id_informe (int): [id_informe]
            param2 fecha_informe (str): [fecha_informe]
            param3 cant_comandas (int): [cant_comandas]
            param4 total_ganancias (float): [total_ganancias]
            param5 promedio_ganancias (float): [promedio_ganancias]
        Retornos:
            None
        Excepciones:
            None
        """
        self.id_informe = id_informe
        self.fecha_informe = fecha_informe
        self.cant_comandas = cant_comandas
        self.total_ganancias = total_ganancias
        self.promedio_ganancias = promedio_ganancias
