import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.Tooltips import add_tooltip 


class CambiarEstado():
    """
    Clase para manejar la interfaz gráfica que permite cambiar el estado de una comanda.
    
    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        chef (Chef): Objeto de tipo Chef que maneja las comandas.
        comandas (list): Lista de comandas.
        subventana (tk.Toplevel): Subventana para la interfaz de cambio de estado.
        id (tk.StringVar): Variable para almacenar el ID de la comanda.
        cedula (tk.StringVar): Variable para almacenar la cédula del cliente.
        mesa (tk.StringVar): Variable para almacenar el número de la mesa.
        platos (tk.StringVar): Variable para almacenar la lista de platos de la comanda.
        precio (tk.StringVar): Variable para almacenar el precio total de la comanda.
        estado (tk.StringVar): Variable para almacenar el estado de la comanda.
    """
    
    def __init__(self, ventana, chef, listaComandas):
        """
        Constructor de la clase.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            chef (Chef): Objeto de tipo Chef que maneja las comandas.
            listaComandas (list): Lista de comandas.
        """
        self.ventana = ventana
        self.comandas = listaComandas
        self.chef = chef      

        # Crear una subventana para cambiar el estado de la comanda
        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title("Cambiar Estado Comanda")

        # Variables para los campos de la interfaz
        self.id = tk.StringVar(self.subventana)
        self.cedula = tk.StringVar(self.subventana)
        self.mesa = tk.StringVar(self.subventana)
        self.platos = tk.StringVar(self.subventana)
        self.precio = tk.StringVar(self.subventana)
        self.estado = tk.StringVar(self.subventana)

        # Configuración de la subventana
        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Cambiar Estado Comanda").pack(pady=10)
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
        estado_entry = ttk.Entry(frame, width=25, textvariable=self.estado)
        estado_entry.grid(row=5, column=1, pady=5)

        # Botones para buscar, cambiar estado y salir
        self.iconoBuscar= tk.PhotoImage(master=self.ventana, file=r"icons\zoom.png")
        buscar_button = ttk.Button(frame, text="Buscar", image=self.iconoBuscar, compound= "right", command=self.buscar)
        buscar_button.grid(row=6, column=0, pady=10)
        add_tooltip(buscar_button, "Haz clic aquí para buscar la comanda")
        
        self.iconoCambiar= tk.PhotoImage(master=self.ventana, file=r"icons\control_repeat.png")
        cambiar_button = ttk.Button(frame, text="Cambiar Estado",image=self.iconoCambiar,compound="right",command=self.guardar)
        cambiar_button.grid(row=6, column=1, pady=10)
        add_tooltip(cambiar_button, "Haz clic aquí para cambiar el estado de la comanda")
        
        self.iconoSalir = tk.PhotoImage(master=self.ventana, file=r"icons\cancel.png")
        salir_button = ttk.Button(frame, text="Salir", image=self.iconoSalir, compound= "right", command=self.subventana.destroy)
        salir_button.grid(row=6, column=2, pady=10)
        add_tooltip(salir_button, "Haz clic aquí para salir de la ventana")

    def guardar(self):
        """
        Método para cambiar el estado de la comanda buscada.
        """
        try:
            id = int(self.id.get())
        except:
            messagebox.showerror(title="Error", message="Ingrese un número válido")
            return
        comanda = self.buscar_comandas(id)
        if not comanda:
            messagebox.showwarning(title="Advertencia", message="No se encontró la comanda con el ID proporcionado")
            return
        self.chef.cambiar_estado_comanda(comanda, self.estado.get().lower())

        messagebox.showinfo(message="Se ha cambiado el estado de la comanda correctamente")

    def buscar(self):
        """
        Método para buscar una comanda por su ID y mostrar sus detalles.
        """
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
            messagebox.showwarning(title="Advertencia", message="No se encontró la comanda con el ID proporcionado")
            return

        # Mostrar los detalles de la comanda en los campos correspondientes
        self.id.set(comanda.id)
        self.cedula.set(comanda.cliente)
        self.mesa.set(comanda.mesa)
        self.platos.set(f"{ [plato[0].id_plato for plato in comanda.platos] }")
        comanda.calcular_precio_total()
        self.precio.set(comanda.precio_total)
        self.estado.set(comanda.estado)

    def buscar_comandas(self, id):
        """
        Método para buscar una comanda en la lista de comandas por su ID.
        
        Argumentos:
            id (int): ID de la comanda a buscar.
        
        Retorna:
            Comanda: Objeto de tipo Comanda si se encuentra, None en caso contrario.
        """
        for comanda in self.comandas:
            if comanda.id == id:
                return comanda