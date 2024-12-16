import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Cliente import Cliente
__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"


class GestionarCliente():
    def __init__(self, ventana, mesero, accion):
        self.ventana = ventana
        self.mesero = mesero
        self.accion = accion
        

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Gestionar Cliente")

        self.cedula = tk.StringVar(self.subventana)
        self.nombre = tk.StringVar(self.subventana)
        self.apellido = tk.StringVar(self.subventana)
        self.telefono = tk.StringVar(self.subventana)
        self.email = tk.StringVar(self.subventana)


        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Registrar Cliente" if accion == "crear" else "Eliminar Cliente").pack(pady=10)
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


        self.iconoGuardar = tk.PhotoImage(file=r"icons\add.png")
        guardar_button = ttk.Button(frame, text="Guardar", image=self.iconoGuardar, compound="right", command=self.guardar)
        guardar_button.grid(row=5, column=0, pady=10)

        self.iconoSalir = tk.PhotoImage(file=r"icons\cancel.png")
        salir_button = ttk.Button(frame, text="Salir",image=self.iconoSalir, compound="right", command=self.subventana.destroy)
        salir_button.grid(row=5, column=1, pady=10)

        if accion == "eliminar":
            buscar_button = ttk.Button(frame, text="Buscar", command=self.buscar)
            buscar_button.grid(row=5, column=0, pady=5)
            guardar_button.grid_configure(pady=5, column=1)
            salir_button.grid_configure(pady=5, column=2)
    

    def guardar(self):
        cedula = self.cedula.get()
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        telefono = self.telefono.get()
        email = self.email.get()

        if not cedula or self.accion == "crear" and (not nombre or not apellido or not telefono or not email):
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return
        
        if self.accion == "crear":
            clienteEncontrado = self.buscar_clientes(cedula)
            if clienteEncontrado:
                messagebox.showwarning(title="Advertencia", message="Ya existe un cliente con la misma cédula")
                return
            cliente = Cliente(cedula, nombre, apellido, telefono, email)
        elif self.accion == "eliminar":
            cliente = self.buscar_clientes(cedula)
            if not cliente:
                messagebox.showwarning(title="Advertencia", message="No se encontró el cliente con la cédula proporcionada")
                return
            if not messagebox.askyesno(message="¿Desea eliminar el cliente?"):
                return

        self.mesero.gestionar_cliente(cliente, self.accion)

        messagebox.showinfo(message="La acción se ha realizado con éxito")

    def buscar(self):
        cedula = self.cedula.get()
        if not cedula:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        cliente = self.buscar_clientes(cedula)
        if not cliente:
            messagebox.showwarning(title="Advertencia", message="No se encontró el cliente con la cédula proporcionada")
            return

        self.nombre.set(cliente.nombre)
        self.apellido.set(cliente.apellido)
        self.telefono.set(cliente.telefono)
        self.email.set(cliente.email)

    def buscar_clientes(self, cedula):
        clientes = self.mesero.clientes
        for cliente in clientes:
            if cliente.cedula == cedula:
                return cliente
