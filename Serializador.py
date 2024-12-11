__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Serializador:
    """
    Clase para manejar la lectura y escritura de archivos de texto en un formato específico para una clase dada.

    Atributos:
        __ruta (str): Ruta del archivo donde se leerán o escribirán los datos.
        __archivo (file object): Objeto de archivo utilizado para operaciones de lectura y escritura.
        __clase (type): Clase que se espera instanciar a partir de los datos leídos del archivo.
        __formato (list): Lista que define el formato esperado de los datos en el archivo.

    Métodos:
        __init__(self, ruta, clase, formato):
            Constructor de la clase Serializador. Inicializa los atributos de la clase.

        escribirArchivo(self, texto):
            Escribe el texto proporcionado al final del archivo.

        escribirTodo(self, texto):
            Sobrescribe completamente el contenido del archivo con el texto proporcionado.

        leerArchivo(self):
            Lee el archivo según el formato especificado y devuelve una lista de instancias de la clase __clase.
    """

    def __init__(self, ruta, clase, formato):
        """
        Inicializa una instancia de Serializador.

        Args:
            ruta (str): Ruta del archivo donde se leerán o escribirán los datos.
            clase (type): Clase que se instanciará con los datos leídos del archivo.
            formato (list): Lista que define el formato esperado de los datos en el archivo
                            (p. ej., ["int", "str", "float", "str"]).

        Returns:
            None
        """
        self.__ruta = ruta or "archivo.txt"
        self.__archivo = open(self.__ruta, "a").close()  # Abre y cierra el archivo para crearlo si no existe
        self.__clase = clase
        self.__formato = formato

    def escribirArchivo(self, texto):
        """
        Escribe el texto proporcionado al final del archivo.

        Args:
            texto (str): Texto que se escribirá en el archivo.

        Returns:
            None
        """
        self.__archivo = open(self.__ruta, "a")
        self.__archivo.write(texto)
        self.__archivo.close()

    def escribirTodo(self, texto):
        """
        Sobrescribe completamente el contenido del archivo con el texto proporcionado.

        Args:
            texto (str): Texto completo que se escribirá en el archivo.

        Returns:
            None
        """
        self.__archivo = open(self.__ruta, "w")
        self.__archivo.write(texto)
        self.__archivo.close()

    def leerArchivo(self):
        """
        Lee el archivo según el formato especificado y devuelve una lista de instancias de la clase __clase.

        Returns:
            list: Lista de instancias de la clase __clase creadas a partir de los datos del archivo.
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
            atributos.append(dato)
            i += 1

            if i == len(self.__formato):
                i = 0
                obj_clase = self.__clase(*atributos)
                lista.append(obj_clase)
                atributos = []

        self.__archivo.close()
        return lista
