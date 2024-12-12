from Persona import Persona
from Plato import Plato
from Serializador import Serializador
from Controlador.PlatoControlador import PlatoControlador

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"


class Chef(Persona):
    """Esta clase representa a los objetos de tipo Chef y hereda de la super clase Persona.

    Atributos:
        __serializadorPlatos (Serializador): Objeto encargado de la serialización de platos.
    """
    
    def __init__(self, cedula, nombre, apellido, telefono, email):
        """Método constructor que permite instanciar objetos de tipo Chef.
        
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
        # self.__serializadorPlatos = Serializador("platos.txt", Plato, ["int", "str", "float", "str"])

    def cambiar_estado_comanda(self, comanda, estado):
        """Método que permite cambiar el estado de una comanda.

        Argumentos:
            param1 comanda (Comanda): [comanda]
            param2 estado (str): [estado]
        Retornos:
            None
        Excepciones:
            None
        """
        if comanda.cambiar_estado(estado):
            print("Se ha cambiado el estado de la comanda correctamente.")
        else:
            print("No se ha logrado cambiar el estado de la comanda correctamente.")

    def gestionar_platos(self, plato, accion, listaPlatos):
        """Método que permite gestionar los platos, ya sea creando o eliminando.

        Argumentos:
            param1 accion (str): [accion]
            param2 listaPlatos (list): [listaPlatos]
        Retornos:
            None
        Excepciones:
            None
        """
        if accion == "crear":
            listaPlatos.append(plato)
            print("El plato se ha creado correctamente.")

        elif accion == "eliminar":
            listaPlatos.remove(plato)

        self.serializar_platos(listaPlatos)
    
    def serializar_platos(self, listaPlatos):
        """Método que permite serializar los datos de los platos en un archivo.

        Argumentos:
            param1 listaPlatos (list): [listaPlatos]
        Retornos:
            None
        Excepciones:
            None
        """
        platoCon = PlatoControlador()
        for plato in listaPlatos:
            if platoCon.obtener_plato(plato.id_plato):
                platoCon.actualizar_plato(plato)
            else:
                platoCon.guardar_plato(plato)
        platoCon.cerrar_con()
