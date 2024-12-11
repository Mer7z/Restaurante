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

class GestionarMesas():
    def __init__(self, ventana, mesero, accion):
        self.ventana = ventana
        self.mesero = mesero
        self.accion = accion
        

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Gestionar Mesa")

        self.id = tk.StringVar(self.subventana)
        self.comensales = tk.IntVar(self.subventana)
        self.estado = tk.StringVar(self.subventana, "libre")


        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Consultar Mesa" if accion == "consultar" else "Ocupar Mesa" if accion == "ocupar" else "Liberar mesa").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        ttk.Label(frame, text="ID*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Entry(frame, width=25, textvariable=self.id)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Cantidad de Comensales*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        comensales_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.comensales)
        comensales_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Estado*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        estado_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.estado)
        estado_entry.grid(row=2, column=1, pady=5)
        
        if accion != "consultar":
            guardar_button = ttk.Button(frame, text="Guardar", command=self.guardar)
            guardar_button.grid(row=5, column=1, pady=10)

        buscar_button = ttk.Button(frame, text="Buscar", command=self.buscar)
        buscar_button.grid(row=5, column=0, pady=5)

        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=5, column=2, pady=10)

    

    def guardar(self):
        try:
            id = int(self.id.get())
            comensales = int(self.comensales.get())
        except:
            messagebox.showerror(title="Error", message="Ingrese un número válido")
            return

        if not id or self.accion == "crear" and (not comensales):
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return
        mesa = self.buscar_mesas(id)
        if not mesa:
            messagebox.showwarning(title="Advertencia", message="No se encontró el mesa con el id proporcionado")
            return
        if self.accion == "ocupar":
            self.mesero.ocupar_mesa(mesa)
        elif self.accion == "liberar":
            self.mesero.liberar_mesa(mesa)
        

        messagebox.showinfo(message="La acción se ha realizado con éxito")

    def buscar(self):
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
        mesas = self.mesero.mesas
        for mesa in mesas:
            if mesa.id_mesa == id:
                return mesa
