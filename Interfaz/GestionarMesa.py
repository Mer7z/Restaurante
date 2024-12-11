import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Mesa import Mesa

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"


class GestionarMesa():
    """
    Clase para gestionar la creación y eliminación de mesas en una aplicación de gestión de restaurantes.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        registrador (Registrador): Objeto que gestiona las operaciones con las mesas.
        accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        subventana (tk.Toplevel): Ventana secundaria para gestionar mesas.
        id (tk.StringVar): Variable para almacenar el ID de la mesa.
        comensales (tk.IntVar): Variable para almacenar la cantidad de comensales de la mesa.
        estado (tk.StringVar): Variable para almacenar el estado de la mesa.
    """
    def __init__(self, ventana, registrador, accion):
        """
        Constructor de la clase. Inicializa la ventana secundaria y configura los widgets.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto que gestiona las operaciones con las mesas.
            accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        """
        self.ventana = ventana
        self.registrador = registrador
        self.accion = accion
        

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Gestionar Mesa")

        self.id = tk.StringVar(self.subventana)
        self.comensales = tk.IntVar(self.subventana)
        self.estado = tk.StringVar(self.subventana, "libre")


        self.subventana.geometry("400x200")
        ttk.Label(self.subventana, text="Registrar Mesa" if accion == "crear" else "Eliminar Mesa").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        ttk.Label(frame, text="ID*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Entry(frame, width=25, textvariable=self.id)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Cantidad de Comensales*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        comensales_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.comensales)
        comensales_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Estado*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        estado_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.estado)
        estado_entry.grid(row=2, column=1, pady=5)
        

        guardar_button = ttk.Button(frame, text="Guardar", command=self.guardar)
        guardar_button.grid(row=5, column=0, pady=10)

        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=5, column=1, pady=10)

        if accion == "eliminar":
            buscar_button = ttk.Button(frame, text="Buscar", command=self.buscar)
            buscar_button.grid(row=5, column=0, pady=5)
            guardar_button.grid_configure(pady=5, column=1)
            salir_button.grid_configure(pady=5, column=2)
    

    def guardar(self):
        """
        Método para guardar la mesa en el registrador. Puede crear o eliminar una mesa según la acción.
        """
        try:
            id = int(self.id.get())
            comensales = int(self.comensales.get())
        except:
            messagebox.showerror(title="Error", message="Ingrese un número válido")
            return

        if not id or self.accion == "crear" and (not comensales):
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return
        
        if self.accion == "crear":
            mesaEncontrado = self.buscar_mesas(id)
            if mesaEncontrado:
                messagebox.showwarning(title="Advertencia", message="Ya existe un mesa con la misma cédula")
                return
            mesa = Mesa(id, comensales)
        elif self.accion == "eliminar":
            mesa = self.buscar_mesas(id)
            if not mesa:
                messagebox.showwarning(title="Advertencia", message="No se encontró el mesa con la cédula proporcionada")
                return
            if not messagebox.askyesno(message="¿Desea eliminar el mesa?"):
                return

        self.registrador.gestionar_mesas(mesa, self.accion)

        messagebox.showinfo(message="La acción se ha realizado con éxito")

    def buscar(self):
        """
        Método para buscar una mesa en el registrador por ID.
        """
        try:
            id = int(self.id.get())
        except:
            messagebox.showerror(title="Error", message="Ingrese un número válido")
            return
        
        if not id:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        mesa = self.buscar_mesas(id)
        if not mesa:
            messagebox.showwarning(title="Advertencia", message="No se encontró el mesa con el id proporcionado")
            return

        self.comensales.set(mesa.cantidad_comensales)
        self.estado.set(mesa.estado)

    def buscar_mesas(self, id):
        """
        Método auxiliar para buscar una mesa en la lista de mesas del registrador por ID.

        Argumentos:
            id (int): ID de la mesa a buscar.

        Retorna:
            Mesa: Objeto mesa encontrado, None si no se encuentra.
        """
        mesas = self.registrador.mesas
        for mesa in mesas:
            if mesa.id_mesa == id:
                return mesa
