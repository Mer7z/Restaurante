import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Mesero import Mesero
from Interfaz.Tooltips import add_tooltip 

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class GestionarMesero():
    """
    Clase para gestionar la creación y eliminación de meseros en una aplicación de gestión de restaurantes.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        registrador (Registrador): Objeto que gestiona las operaciones con los meseros.
        accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        subventana (tk.Toplevel): Ventana secundaria para gestionar meseros.
        cedula (tk.StringVar): Variable para almacenar la cédula del mesero.
        nombre (tk.StringVar): Variable para almacenar el nombre del mesero.
        apellido (tk.StringVar): Variable para almacenar el apellido del mesero.
        telefono (tk.StringVar): Variable para almacenar el teléfono del mesero.
        email (tk.StringVar): Variable para almacenar el email del mesero.
    """
    def __init__(self, ventana, registrador, accion):
        """
        Constructor de la clase. Inicializa la ventana secundaria y configura los widgets.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto que gestiona las operaciones con los meseros.
            accion (str): Acción a realizar, puede ser "crear" o "eliminar".
        """
        self.ventana = ventana
        self.registrador = registrador
        self.accion = accion
        

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Gestionar Mesero")

        self.cedula = tk.StringVar(self.subventana)
        self.nombre = tk.StringVar(self.subventana)
        self.apellido = tk.StringVar(self.subventana)
        self.telefono = tk.StringVar(self.subventana)
        self.email = tk.StringVar(self.subventana)


        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Registrar Mesero" if accion == "crear" else "Eliminar Mesero").pack(pady=10)
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
        Método para guardar el mesero en el registrador. Puede crear o eliminar un mesero según la acción.
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
            meseroEncontrado = self.buscar_meseros(cedula)
            if meseroEncontrado:
                messagebox.showwarning(title="Advertencia", message="Ya existe un mesero con la misma cédula")
                return
            mesero = Mesero(cedula, nombre, apellido, telefono, email)
        elif self.accion == "eliminar":
            mesero = self.buscar_meseros(cedula)
            if not mesero:
                messagebox.showwarning(title="Advertencia", message="No se encontró el mesero con la cédula proporcionada")
                return
            if not messagebox.askyesno(message="¿Desea eliminar el mesero?"):
                return

        self.registrador.gestionar_meseros(mesero, self.accion)

        messagebox.showinfo(message="La acción se ha realizado con éxito")

    def buscar(self):
        """
        Método para buscar un mesero en el registrador por cédula y mostrar sus datos en los campos del formulario.
        """
        cedula = self.cedula.get()
        if not cedula:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        mesero = self.buscar_meseros(cedula)
        if not mesero:
            messagebox.showwarning(title="Advertencia", message="No se encontró el mesero con la cédula proporcionada")
            return

        self.nombre.set(mesero.nombre)
        self.apellido.set(mesero.apellido)
        self.telefono.set(mesero.telefono)
        self.email.set(mesero.email)

    def buscar_meseros(self, cedula):
        """
        Método auxiliar para buscar un mesero en la lista de meseros del registrador por cédula.

        Argumentos:
            cedula (str): Cédula del mesero a buscar.

        Retorna:
            Mesero: Objeto mesero encontrado, None si no se encuentra.
        """
        meseros = self.registrador.meseros
        for mesero in meseros:
            if mesero.cedula == cedula:
                return mesero
