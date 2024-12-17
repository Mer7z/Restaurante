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

class GestionarComanda():
    def __init__(self, ventana, mesero, accion, comandas):
        self.ventana = ventana
        self.mesero = mesero
        self.accion = accion
        self.comandas = comandas   

        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Comanda")

        self.id = tk.IntVar(self.subventana)
        self.cedula = tk.StringVar(self.subventana)
        self.mesa = tk.StringVar(self.subventana)
        self.platos = tk.StringVar(self.subventana)
        self.precio = tk.StringVar(self.subventana)
        self.estado = tk.StringVar(self.subventana)


        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Tomar Comanda" if self.accion == "tomar" else "Agregar Plato Comanda" if self.accion == "crear" else "Eliminar Plato Comanda" if self.accion == "eliminar" else "Enviar Comanda").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        ttk.Label(frame, text="ID*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Entry(frame, width=25, textvariable=self.id)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Cédula Cliente*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        cedula_entry = ttk.Entry(frame, width=25, state="normal" if self.accion == "tomar" else "disabled", textvariable=self.cedula)
        cedula_entry.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="No. Mesa*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        mesa_entry = ttk.Entry(frame, width=25, state="normal" if self.accion == "tomar" else "disabled", textvariable=self.mesa)
        mesa_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Platos*:").grid(row=3, column=0, sticky=tk.W, pady=5)
        platos_entry = ttk.Entry(frame, width=25, state="normal" if self.accion == "crear" else "disabled", textvariable=self.platos)
        platos_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Precio Total*:").grid(row=4, column=0, sticky=tk.W, pady=5)
        precio_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.precio)
        precio_entry.grid(row=4, column=1, pady=5)

        ttk.Label(frame, text="Estado*:").grid(row=5, column=0, sticky=tk.W, pady=5)
        estado_entry = ttk.Entry(frame, width=25, state="disabled", textvariable=self.estado)
        estado_entry.grid(row=5, column=1, pady=5)

        self.iconoBuscar= tk.PhotoImage(master=self.ventana, file=r"icons\zoom.png")
        buscar_button = ttk.Button(frame, text="Buscar",image=self.iconoBuscar, compound= "right", command=self.buscar)
        buscar_button.grid(row=6, column=0, pady=10)
        add_tooltip(buscar_button, "haz clic aquí para buscar")

        self.iconoCambiar= tk.PhotoImage(master=self.ventana, file=r"icons\control_repeat.png")
        guardar_button = ttk.Button(frame, text="Guardar",image=self.iconoCambiar,compound="right", command=self.guardar)
        guardar_button.grid(row=6, column=1, pady=10)
        add_tooltip(guardar_button, "haz clic aquí para guardar")

        self.iconoSalir = tk.PhotoImage(master=self.ventana, file=r"icons\cancel.png")
        salir_button = ttk.Button(frame, text="Salir", image=self.iconoSalir, compound= "right", command=self.subventana.destroy)
        salir_button.grid(row=6, column=2, pady=10)
        add_tooltip(salir_button, "haz clic aquí para salir")

    def guardar(self):
        
        
        if self.accion == "tomar":
            try:
                id = int(self.id.get())
                cedula = self.cedula.get()
                mesa = int(self.mesa.get())
            except:
                messagebox.showerror(title="Error", message="Ingrese un valor válido")
                return
            if self.buscar_comandas(id):
                messagebox.showwarning(title="Advertencia", message="La comanda ya existe")
            comanda = self.mesero.tomar_comanda(cedula, id, mesa)
            if comanda == False:
                messagebox.showwarning(title="Advertencia", message="La mesa seleccionada aún no se ha ocupado")
                return
            elif comanda == "no cliente":
                messagebox.showwarning(message="No existe el cliente con esta cédula")
                return
            elif comanda == "no mesa":
                messagebox.showwarning(message="No se encontró la mesa")
                return
            
            messagebox.showinfo(message="Se ha creado la comanda con éxito")
        elif self.accion == "crear":
            try:
                id = int(self.id.get())
                cedula = self.cedula.get()
                mesa = int(self.mesa.get())
                platos = self.platos.get()
            except:
                messagebox.showerror(title="Error", message="Ingrese un valor válido")
                return
            comOb = self.buscar_comandas(id)
            if not comOb:
                messagebox.showwarning(title="Advertencia", message="No se encontró el comanda con el id proporcionado")
                return
            try:
                id_platos = [int(plato) for plato in platos.split("-")]
            except:
                messagebox.showwarning(message="Ingrese el id de los platos correctamente ej: 1-2-3")
            for plato in id_platos:
                comanda = self.mesero.agregar_plato_comanda(id, plato)
                if comanda == False:
                    messagebox.showwarning(message="No se encontró el plato seleccionado")
                    return
                
            messagebox.showinfo(message="Se agregó los platos a la comanda correctamente")
        elif self.accion == "eliminar":
            comOb = self.buscar_comandas(id)
            if not comOb:
                messagebox.showwarning(title="Advertencia", message="No se encontró el comanda con el id proporcionado")
                return
            try:
                id_platos = [int(plato) for plato in platos.split("-")]
            except:
                messagebox.showwarning(message="Ingrese el id de los platos correctamente ej: 1-2-3")
            for plato in id_platos:
                comanda = self.mesero.eliminar_plato_comanda(id, plato)
                if comanda == False:
                    messagebox.showwarning(message="No se encontró el plato seleccionado")
                    return
                
            messagebox.showinfo(message="Se eliminó los platos a la comanda correctamente")
        elif self.accion == "enviar":
            comOb = self.buscar_comandas(id)
            if not comOb:
                messagebox.showwarning(title="Advertencia", message="No se encontró el comanda con el id proporcionado")
                return
            
            self.mesero.cambiar_estado_comanda(comOb, "en preparación")
            messagebox.showinfo(message="Se envió la comanda correctamente")
           

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
        self.precio.set(self.mesero.calcular_precio_total(comanda))
        self.estado.set(comanda.estado)


    def buscar_comandas(self, id):
        comandas = self.comandas
        for comanda in comandas:
            if comanda.id == id:
                return comanda
