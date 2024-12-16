import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Interfaz.MenuMesero.GestionarCliente import GestionarCliente
from Interfaz.MenuMesero.GestionarMesas import GestionarMesas
from Interfaz.MenuMesero.GestionarComanda import GestionarComanda

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"


class MenuMesero:
    def __init__(self, ventana, mesero, listaComandas):
        self.root = ventana
        self.listaComandas = listaComandas
        self.ventana = tk.Toplevel(self.root)
        self.ventana.geometry("535x400")
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)
        self.ventana.focus_set()
        self.ventana.configure(bg="white")
        self.mesero = mesero
        
        self.menu = tk.Menu(self.ventana) 
        self.ventana.config(menu=self.menu)

        self.lblElaborado = tk.Label(self.ventana, text="Elaborado por:\n John Esneider Marin\n Juan Esteban Agudelo\n Manuel Esteban Ramirez")
        self.lblElaborado.grid(row=8, column=5, padx=(250,0))

        self.lblBienvenido = tk.Label(self.ventana, text=f"Bienvenido!!!")
        self.lblBienvenido.grid(row=5, column=4, columnspan=2, padx=150, pady=150)

        menuClientes = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Cliente", menu=menuClientes)
        menuClientes.add_command(label="Registrar Cliente", command=lambda: self.gestionar_cliente("crear"))
        menuClientes.add_separator()
        menuClientes.add_command(label="Eliminar Cliente", command=lambda: self.gestionar_cliente("eliminar"))

        menuMesas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Mesas", menu=menuMesas)
        menuMesas.add_command(label="Consultar Mesas", command=lambda: self.gestionar_mesas("consultar"))
        menuMesas.add_separator()
        menuMesas.add_command(label="Ocupar Mesa", command=lambda: self.gestionar_mesas("ocupar"))
        menuMesas.add_separator()
        menuMesas.add_command(label="Liberar Mesa", command=lambda: self.gestionar_mesas("liberar"))

        menuComandas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Comandas", menu=menuComandas)
        menuComandas.add_command(label="Tomar Comanda", command=lambda: self.gestionar_comanda("tomar"))
        menuComandas.add_separator()
        menuComandas.add_command(label="Agregar Plato a Comanda", command=lambda: self.gestionar_comanda("crear"))
        menuComandas.add_separator()
        menuComandas.add_command(label="Eliminar Plato de Comanda", command=lambda: self.gestionar_comanda("eliminar"))
        menuComandas.add_separator()
        menuComandas.add_command(label="Enviar Comanda", command=lambda: self.gestionar_comanda("enviar"))

        menuSalir = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=menuSalir)
        menuSalir.add_command(label="Salir", command=lambda: self.salir())

        self.ventana.mainloop()

    def gestionar_cliente(self, accion):
        GestionarCliente(self.ventana, self.mesero, accion)
        pass

    def gestionar_mesas(self, accion):
        GestionarMesas(self.ventana, self.mesero, accion)
        pass

    def gestionar_comanda(self, accion):
        GestionarComanda(self.ventana, self.mesero, accion, self.listaComandas)
        pass

    def salir(self):
        respuesta = messagebox.askquestion("Confirmacion", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()

