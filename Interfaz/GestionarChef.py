import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Chef import Chef
from Interfaz.Tooltips import add_tooltip 

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class GestionarChef():
    """
    Clase para gestionar la creación y eliminación de chefs en una aplicación de gestión de restaurantes.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        registrador (Registrador): Objeto que gestiona las operaciones con los chefs.
        accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        subventana (tk.Toplevel): Ventana secundaria para gestionar chefs.
        cedula (tk.StringVar): Variable para almacenar la cédula del chef.
        nombre (tk.StringVar): Variable para almacenar el nombre del chef.
        apellido (tk.StringVar): Variable para almacenar el apellido del chef.
        telefono (tk.StringVar): Variable para almacenar el teléfono del chef.
        email (tk.StringVar): Variable para almacenar el email del chef.
    """
    def __init__(self, ventana, registrador, accion):
        """
        Constructor de la clase. Inicializa la ventana secundaria y configura los widgets.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto que gestiona las operaciones con los chefs.
            accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        """
        self.ventana = ventana
        self.registrador = registrador
        self.accion = accion
        

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Gestionar Chef")

        self.cedula = tk.StringVar(self.subventana)
        self.nombre = tk.StringVar(self.subventana)
        self.apellido = tk.StringVar(self.subventana)
        self.telefono = tk.StringVar(self.subventana)
        self.email = tk.StringVar(self.subventana)


        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Registrar Chef" if accion == "crear" else "Eliminar Chef").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        ttk.Label(frame, text="Cédula*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        cedula_entry = ttk.Entry(frame, width=25, textvariable=self.cedula)
        cedula_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Nombre*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        nombre_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.nombre)
        nombre_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Apellido*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        apellido_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.apellido)
        apellido_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Teléfono*:").grid(row=3, column=0, sticky=tk.W, pady=5)
        telefono_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.telefono)
        telefono_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Email*:").grid(row=4, column=0, sticky=tk.W, pady=5)
        email_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.email)
        email_entry.grid(row=4, column=1, pady=5)

        guardar_button = ttk.Button(frame, text="Guardar", command=self.guardar)
        guardar_button.grid(row=5, column=0, pady=10)

        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=5, column=1, pady=10)

        add_tooltip(guardar_button, "Haz clic aquí para guardar")
        add_tooltip(buscar_button, "Haz clic aquí para buscar")
        add_tooltip(salir_button, "Haz clic aquí para salir")

        if accion == "eliminar":
            buscar_button = ttk.Button(frame, text="Buscar", command=self.buscar)
            buscar_button.grid(row=5, column=0, pady=5)
            guardar_button.grid_configure(pady=5, column=1)
            salir_button.grid_configure(pady=5, column=2)
    

    def guardar(self):
        """
        Método para guardar el chef en el registrador. Puede crear o eliminar un chef según la acción.
        """
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        telefono = self.telefono.get()
        email = self.email.get()

        if not cedula or self.accion == "crear" and (not nombre or not apellido or not telefono or not email):
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return
        
        if self.accion == "crear":
            chefEncontrado = self.buscar_chefs(cedula)
            if chefEncontrado:
                messagebox.showwarning(title="Advertencia", message="Ya existe un chef con la misma cédula")
                return
            chef = Chef(cedula, nombre, apellido, telefono, email)
        elif self.accion == "eliminar":
            chef = self.buscar_chefs(cedula)
            if not chef:
                messagebox.showwarning(title="Advertencia", message="No se encontró el chef con la cédula proporcionada")
                return
            if not messagebox.askyesno(message="¿Desea eliminar el chef?"):
                return

        self.registrador.gestionar_chef(chef, self.accion)

        messagebox.showinfo(message="La acción se ha realizado con éxito")

    def buscar(self):
        """
        Método para buscar un chef en el registrador por cédula.
        """
        cedula = self.cedula.get()
        if not cedula:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        chef = self.buscar_chefs(cedula)
        if not chef:
            messagebox.showwarning(title="Advertencia", message="No se encontró el chef con la cédula proporcionada")
            return

        self.nombre.set(chef.nombre)
        self.apellido.set(chef.apellido)
        self.telefono.set(chef.telefono)
        self.email.set(chef.email)

    def buscar_chefs(self, cedula):
        """
        Método para buscar un chef en la lista de chefs del registrador.

        Argumentos:
            cedula (str): Cédula del chef a buscar.

        Retorna:
            Chef: Objeto chef encontrado, None si no se encuentra.
        """
        chefs = self.registrador.chefs
        for chef in chefs:
            if chef.cedula == cedula:
                return chef

