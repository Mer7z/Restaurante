from Serializador import Serializador  # Importamos la clase base Serializador
from Comanda import Comanda  # Importamos la clase Comanda
__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class SerializadorComanda(Serializador):
    """
    Clase para serializar (escribir y leer) objetos de tipo Comanda en archivos de texto.

    Hereda de Serializador para aprovechar los métodos de escritura y lectura genéricos.

    Atributos:
        __ruta (str): Ruta del archivo donde se guardan las comandas serializadas ("comandas.txt").
        __formato (list):   Lista que define el formato esperado de los datos en el archivo.
                            Incluye tipos como "int", "str", "float" y "plato".
        __archivo (file object): Objeto de archivo utilizado para operaciones de lectura y escritura.

    Métodos:
        __init__():
            Constructor de la clase. Inicializa la ruta del archivo, el formato esperado y el archivo mismo.

        escribirArchivo(texto):
            Método heredado de Serializador. Escribe el texto proporcionado al final del archivo.

        escribirTodo(texto):
            Método heredado de Serializador. Sobrescribe completamente el contenido del archivo con el texto proporcionado.

        leerArchivo(listaPlatos):
            Lee el archivo según el formato especificado y devuelve una lista de instancias de la clase Comanda.
            Además, utiliza la lista de platos proporcionada para asociar los platos a la comanda correcta.

        __buscarPlatos(listaPlatos, id_plato):
            Método privado para buscar un plato por su ID en una lista de platos.

    """
    def __init__(self):
        """
        Inicializa una instancia de SerializadorComanda.

        Establece la ruta del archivo, el formato esperado y crea el archivo si no existe.

        Args:
            None

        Returns:
            None
        """
        self.__ruta = "comandas.txt"
        self.__formato = ["int", "int", "str", "float", "str", "plato"]
        self.__archivo = open(self.__ruta, "a").close()  # Abre y cierra el archivo para crearlo si no existe

    def escribirArchivo(self, texto):
        """
        Escribe el texto proporcionado al final del archivo.

        Args:
            texto (str): Texto que se escribirá en el archivo.

        Returns:
            None
        """
        return super().escribirArchivo(texto)

    def escribirTodo(self, texto):
        """
        Sobrescribe completamente el contenido del archivo con el texto proporcionado.

        Args:
            texto (str): Texto completo que se escribirá en el archivo.

        Returns:
            None
        """
        return super().escribirTodo(texto)

    def leerArchivo(self, listaPlatos):
        """
        Lee el archivo según el formato especificado y devuelve una lista de instancias de la clase Comanda.

        Args:
            listaPlatos (list): Lista de objetos de tipo Plato para asociar con las comandas.

        Returns:
            list: Lista de instancias de la clase Comanda creadas a partir de los datos del archivo.
        """
        atributos = []
        lista = []
        i = 0
        self.__archivo = open(self.__ruta, "r")
        for linea in self.__archivo:
            tipos = self.__formato
            if tipos[i] == "str":
                dato = linea.strip()
            elif tipos[i] == "int":
                dato = int(linea.strip())
            elif tipos[i] == "float":
                dato = float(linea.strip())
            elif tipos[i] == "plato":
                infoPl = linea.strip().split("|")
                platos = []
                for pl in infoPl:
                    listaPl = pl.split(",")
                    id = int(listaPl[0])
                    cantidad = int(listaPl[1])
                    plato = self.__buscarPlatos(listaPlatos, id)
                    platos.append([plato, cantidad])
                dato = platos
            atributos.append(dato)
            i += 1

            if i == len(self.__formato):
                i = 0
                comanda = Comanda(*atributos)
                lista.append(comanda)
                atributos = []

        self.__archivo.close()
        return lista

    def __buscarPlatos(self, listaPlatos, id_plato):
        """
        Método privado para buscar un plato por su ID en una lista de platos.

        Args:
            listaPlatos (list): Lista de objetos de tipo Plato.
            id_plato (int): ID del plato que se desea buscar.

        Returns:
            Plato or None: Objeto Plato si se encuentra, None si no se encuentra.
        """
        for plato in listaPlatos:
            if plato.id_plato == id_plato:
                return plato
        return None
