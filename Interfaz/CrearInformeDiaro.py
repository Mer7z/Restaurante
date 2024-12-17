import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from Interfaz.Tooltips import add_tooltip 

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class CrearInformeDiario():
    """
    Clase para crear y mostrar un informe diario de una aplicación de gestión de comandas.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        informes (list): Lista de informes generados.
        comandas (list): Lista de comandas del día.
        registrador (Registrador): Objeto que gestiona las operaciones con los informes y comandas.
        subventana (tk.Toplevel): Ventana secundaria para mostrar el informe diario.
        informe (Informe): Objeto informe diario generado.
    """
    def __init__(self, ventana, registrador, informes, comandas):
        """
        Constructor de la clase. Inicializa la ventana secundaria y configura los widgets.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto que gestiona las operaciones con los informes y comandas.
            informes (list): Lista de informes generados.
            comandas (list): Lista de comandas del día.
        """
        self.ventana = ventana
        self.informes = informes
        self.comandas = comandas
        self.registrador = registrador      
        fecha = date.today().strftime("%d-%m-%Y")
        self.informe = self.registrador.generar_informes_diarios(self.informes, fecha, self.comandas)

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Informe Diario")


        self.subventana.geometry("300x300")     
        ttk.Label(self.subventana, text="Informe Diario").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        ttk.Label(frame, text="ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Label(frame, width=25, text=self.informe.id_informe)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Fecha:").grid(row=1, column=0, sticky=tk.W, pady=5)
        fecha_entry = ttk.Label(frame, width=25, text=self.informe.fecha_informe)
        fecha_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Cant. Comandas:").grid(row=2, column=0, sticky=tk.W, pady=5)
        cant_entry = ttk.Label(frame, width=25, text=self.informe.cant_comandas)
        cant_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Total Ganacias Día:").grid(row=3, column=0, sticky=tk.W, pady=5)
        total_entry = ttk.Label(frame, width=25, text=self.informe.total_ganancias)
        total_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Promedio Ganacias Día:").grid(row=4, column=0, sticky=tk.W, pady=5)
        promedio_entry = ttk.Label(frame, width=25, text=self.informe.promedio_ganancias)
        promedio_entry.grid(row=4, column=1, pady=5)

        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=6, column=1, pady=10)
        
        add_tooltip(salir_button, "Haz clic aquí para salir")
        
    def guardar(self):
        pass

    def buscar(self):
        try:
            id = int(self.id.get())
        except:
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
