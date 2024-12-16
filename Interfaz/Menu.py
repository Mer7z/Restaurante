import tkinter as tk
from tkinter import messagebox
from Interfaz.GestionarChef import GestionarChef
from Interfaz.GestionarMesero import GestionarMesero
from Interfaz.GestionarMesa import GestionarMesa
from Interfaz.CalcularPrecioComanda import CalcularPrecioComanda
from Interfaz.CrearInformeDiaro import CrearInformeDiario

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"


class Menu():
    """Clase para gestionar el menú principal de la aplicación."""

    def Salir(self):
        """Método para salir de la aplicación, muestra una confirmación antes de cerrar la ventana."""
        respuesta = messagebox.askquestion("Confirmacion", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def crearChef(self):
        """Método para abrir la ventana de creación de un chef."""
        crear = GestionarChef(self.ventana, self.Registrador, "crear")

    def eliminarChef(self):
        """Método para abrir la ventana de eliminación de un Chef."""
        eliminar = GestionarChef(self.ventana, self.Registrador,"eliminar")

    def crearMesero (self):
        """Método para abrir la ventana de creación de un Mesero."""
        crear = GestionarMesero(self.ventana, self.Registrador, "crear")

    def eliminarMesero(self):
        """Método para abrir la ventana de eliminación de un Mesero."""
        eliminar = GestionarMesero(self.ventana, self.Registrador,"eliminar")

    def AgregarMesa (self):
        """Método para abrir la ventana de Agregar una mesa."""
        mesa = GestionarMesa (self.ventana, self.Registrador, "crear")

    def eliminarMesa(self):
        """Método para abrir la ventana de eliminar una mesa."""
        mesa = GestionarMesa(self.ventana, self.Registrador, "eliminar")
    
    def CalcularPrecioComanda (self):
        """Metodo para Calcular el Precio total de las comandas"""""
        mesa = CalcularPrecioComanda(self.ventana, self.Registrador, self.listaComandas)

    def CrearInformeDiario (self):
        """Metodo para crear un informe diario"""""
        mesa = CrearInformeDiario(self.ventana, self.Registrador, self.listaInformes, self.listaComandas)



    def __init__(self, ventana, Registrador, listaInformes, listaComandas):
        self.root = ventana
        self.ventana = tk.Toplevel(self.root)
        self.ventana.geometry("535x400")
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)
        self.ventana.focus_set()
        self.ventana.configure(bg="white")
        self.Registrador = Registrador
        self.listaInformes = listaInformes
        self.listaComandas = listaComandas
        
        self.menu = tk.Menu(self.ventana) 
        self.ventana.config(menu=self.menu)
        menuRegistrador = tk.Menu(self.menu)

        self.lblElaborado = tk.Label(self.ventana, text="Elaborado por:\n John Esneider Marin\n Juan Esteban Agudelo\n Manuel Esteban Ramirez")
        self.lblElaborado.grid(row=8, column=5, padx=(250,0))

        self.lblBienvenido = tk.Label(self.ventana, text=f"Bienvenido!!!")
        self.lblBienvenido.grid(row=5, column=4, columnspan=2, padx=150, pady=150)

        self.menu.add_cascade(label="Gestionar chef", menu=menuRegistrador)
        menuRegistrador.add_command(label="Regsitrar chef", command=lambda:self.crearChef())
        menuRegistrador.add_separator()
        menuRegistrador.add_command(label="Eliminar chef", command=lambda:self.eliminarChef())

        menuMeseros = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar meseros", menu=menuMeseros)
        menuMeseros.add_command(label="Registrar mesero", command=lambda:self.crearMesero())
        menuMeseros.add_separator()
        menuMeseros.add_command(label="Eliminar mesero", command=lambda:self.eliminarMesero())

        menuMesa = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar mesas", menu=menuMesa)
        menuMesa.add_command(label="Agregar mesa", command=lambda:self.AgregarMesa())
        menuMesa.add_separator()
        menuMesa.add_command(label="Eliminar mesa", command=lambda:self.eliminarMesa())
        
        menuPrecio = tk.Menu(self.menu)
        self.menu.add_cascade(label="Calcular Precio Total", menu=menuPrecio)
        menuPrecio.add_command(label="Calcular precio total", command=lambda:self.CalcularPrecioComanda())
        menuPrecio.add_separator()
        menuPrecio.add_command(label="Crear Informe Diario", command=lambda:self.CrearInformeDiario())

        menuSalir = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=menuSalir)
        menuSalir.add_command(label="Salir", command=lambda:self.Salir())

        self.ventana.mainloop()



