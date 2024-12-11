from Interfaz.GestionarChef import GestionarChef
from Interfaz.GestionarMesero import GestionarMesero
from Interfaz.GestionarMesa import GestionarMesa
from Interfaz.CalcularPrecioComanda import CalcularPrecioComanda
from Interfaz.CrearInformeDiaro import CrearInformeDiario
import tkinter as tk
from Registrador import Registrador
from Chef import Chef
from Mesa import Mesa
from Serializador import Serializador
from SerializadorComanda import SerializadorComanda
from Plato import Plato
from Interfaz.MenuChef.MenuChef import MenuChef
from Interfaz.Loggin import Loggin

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

app = tk.Tk()

app.geometry("500x400")
serializadorChef = Serializador("chefs.txt", Chef, ["str", "str", "str", "str", "str"])
serializadorMesa = Serializador("mesas.txt", Mesa, ["int", "int", "str"])
serializadorComanda = SerializadorComanda()
serializadorPlato = Serializador("platos.txt", Plato, ["int", "str", "float", "str", "int"])
listaPlatos = serializadorPlato.leerArchivo()
listaComandas = serializadorComanda.leerArchivo(listaPlatos)
listaChefs = serializadorChef.leerArchivo()
listaMesas = serializadorMesa.leerArchivo()
listaInformes = []
reg = Registrador("", "", "", "", "", listaMesas, [], listaChefs)
chef  = Chef("", "", "", "", "")

# GestionarChef(app, reg, "eliminar")
# GestionarMesero(app, reg, "crear")
# GestionarMesa(app, reg, "eliminar")
# MenuChef(chef, listaComandas)
Loggin(app, listaComandas, listaInformes, listaPlatos)

app.mainloop()