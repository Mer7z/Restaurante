import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.Tooltips import add_tooltip 

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class CalcularPrecioComanda:
    """
    Clase para calcular el precio total de una comanda en una aplicación de gestión de comandas.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        comandas (list): Lista de comandas.
        registrador (Registrador): Objeto que gestiona las operaciones con las comandas.
        subventana (tk.Toplevel): Ventana secundaria para calcular el precio de la comanda.
        id (tk.StringVar): Variable para el ID de la comanda.
        cedula (tk.StringVar): Variable para la cédula del cliente.
        mesa (tk.StringVar): Variable para el número de mesa.
        platos (tk.StringVar): Variable para los platos en la comanda.
        precio (tk.StringVar): Variable para el precio total de la comanda.
        estado (tk.StringVar): Variable para el estado de la comanda.
    """

    def __init__(self, ventana, registrador, listaComandas):
        """
        Constructor de la clase. Inicializa la ventana secundaria y configura los widgets.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto que gestiona las operaciones con las comandas.
            listaComandas (list): Lista de comandas.
        """
        self.ventana = ventana
        self.comandas = listaComandas
        self.registrador = registrador      

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Calcular Precio Comanda")

        # Variables para los datos de la comanda
        self.id = tk.StringVar(self.subventana)
        self.cedula = tk.StringVar(self.subventana)
        self.mesa = tk.StringVar(self.subventana)
        self.platos = tk.StringVar(self.subventana)
        self.precio = tk.StringVar(self.subventana)
        self.estado = tk.StringVar(self.subventana)

        # Configuración de la ventana secundaria
        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Calcular Precio Comanda").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        # Campos de entrada y etiquetas
        ttk.Label(frame, text="ID*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Entry(frame, width=25, textvariable=self.id)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Cédula Cliente*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        cedula_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.cedula)
        cedula_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="No. Mesa*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        mesa_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.mesa)
        mesa_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Platos*:").grid(row=3, column=0, sticky=tk.W, pady=5)
        platos_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.platos)
        platos_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Precio Total*:").grid(row=4, column=0, sticky=tk.W, pady=5)
        precio_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.precio)
        precio_entry.grid(row=4, column=1, pady=5)

        ttk.Label(frame, text="Estado*:").grid(row=5, column=0, sticky=tk.W, pady=5)
        estado_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.estado)
        estado_entry.grid(row=5, column=1, pady=5)

        # Botones para calcular el total y salir
        guardar_button = ttk.Button(frame, text="Calcular Total", command=self.buscar)
        guardar_button.grid(row=6, column=0, pady=10)

        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=6, column=1, pady=10)

        add_tooltip(guardar_button, "Haz clic aquí para guardar")
        add_tooltip(salir_button, "Haz clic aquí para salir")

    def guardar(self):
        """
        Método para guardar los cambios realizados en la comanda.
        Actualmente, no realiza ninguna acción.
        """
        pass

    def buscar(self):
        """
        Método para buscar una comanda por su ID y calcular su precio total.
        Muestra los datos de la comanda en los campos correspondientes.

        Maneja errores de entrada y muestra mensajes de advertencia si no se encuentra la comanda.
        """
        try:
            id = int(self.id.get())
        except ValueError:
            messagebox.showerror(title="Error", message="Ingrese un número válido")
            return
        
        if not id:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        comanda = self.buscar_comandas(id)
        if not comanda:
            messagebox.showwarning(title="Advertencia", message="No se encontró el comanda con el id proporcionado")
            return

        self.id.set(comanda.id)
        self.cedula.set(comanda.cliente)
        self.mesa.set(comanda.mesa)
        self.platos.set(f"{ [plato[0].id_plato for plato in comanda.platos] }")
        self.precio.set(self.registrador.calcular_precio_total(comanda))
        self.estado.set(comanda.estado)

    def buscar_comandas(self, id):
        """
        Método para buscar una comanda por su ID en la lista de comandas.

        Argumentos:
            id (int): ID de la comanda a buscar.

        Retorna:
            Comanda: La comanda encontrada, o None si no se encuentra.
        """
        for comanda in self.comandas:
            if comanda.id == id:
                return comanda

