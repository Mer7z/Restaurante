import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Plato import Plato
from Interfaz.Tooltips import add_tooltip 

class GestionarPlato:
    """
    Clase para gestionar la creación o eliminación de platos mediante una interfaz gráfica.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        registrador (Registrador): Objeto encargado de registrar los platos.
        accion (str): Acción a realizar ("crear" o "eliminar").
        subventana (tk.Toplevel): Subventana para la interfaz de gestión de platos.
        id (tk.StringVar): Variable para almacenar el ID del plato.
        nombre (tk.StringVar): Variable para almacenar el nombre del plato.
        precio (tk.DoubleVar): Variable para almacenar el precio del plato.
        cantidad_disponible (tk.IntVar): Variable para almacenar la cantidad disponible del plato.
        descripcion (tk.StringVar): Variable para almacenar la descripción del plato.
    """

    def __init__(self, ventana, registrador, accion, listaPlatos):
        """
        Constructor de la clase.

        Argumentos:
            ventana (tk.Tk): Ventana principal de la aplicación.
            registrador (Registrador): Objeto encargado de registrar los platos.
            accion (str): Acción a realizar ("crear" o "eliminar").
        """
        self.ventana = ventana
        self.registrador = registrador
        self.accion = accion
        self.listaPlatos = listaPlatos

        # Crear una subventana para gestionar los platos
        self.subventana = tk.Toplevel(self.ventana)
        self.subventana.title(f"{accion.capitalize()} Plato")

        # Variables para los campos de la interfaz
        self.id = tk.IntVar(self.subventana)
        self.nombre = tk.StringVar(self.subventana)
        self.precio = tk.DoubleVar(self.subventana)
        self.cantidad_disponible = tk.IntVar(self.subventana)
        self.descripcion = tk.StringVar(self.subventana)

        # Configuración de la subventana
        self.subventana.geometry("300x300")
        ttk.Label(self.subventana, text="Agregar Plato" if accion == "crear" else "Eliminar Plato").pack(pady=10)
        frame = ttk.Frame(self.subventana, padding="10")
        frame.pack()

        # Campos de entrada y etiquetas
        ttk.Label(frame, text="ID*:").grid(row=0, column=0, sticky=tk.W, pady=5)
        id_entry = ttk.Entry(frame, width=25, textvariable=self.id)
        id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Nombre*:").grid(row=1, column=0, sticky=tk.W, pady=5)
        nombre_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.nombre)
        nombre_entry.grid(row=1, column=1, pady=5)

        ttk.Label(frame, text="Precio*:").grid(row=2, column=0, sticky=tk.W, pady=5)
        precio_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.precio)
        precio_entry.grid(row=2, column=1, pady=5)

        ttk.Label(frame, text="Cantidad Disponible*:").grid(row=3, column=0, sticky=tk.W, pady=5)
        cantidad_disponible_entry = ttk.Entry(frame, width=25, state="normal" if accion == "crear" else "disabled", textvariable=self.cantidad_disponible)
        cantidad_disponible_entry.grid(row=3, column=1, pady=5)

        ttk.Label(frame, text="Descripción*:").grid(row=4, column=0, sticky=tk.W, pady=5)
        descripcion_entry = tk.Text(frame, width=23, height=4, state="normal" if accion == "crear" else "disabled", wrap=tk.WORD)
        descripcion_entry.grid(row=4, column=1, pady=5)
        descripcion_entry.bind("<KeyRelease>", lambda e: self.descripcion.set(descripcion_entry.get("1.0", tk.END).strip()))


        # Botones para guardar y salir
        self.iconoGuardar = tk.PhotoImage(file=r"icons\add.png")
        guardar_button = ttk.Button(frame, text="Guardar", image=self.iconoGuardar, compound="right", command=self.guardar)
        guardar_button.grid(row=5, column=0, pady=10)
        add_tooltip(guardar_button,"Haz clic aquí para guardar.")
        
        self.iconoSalir = tk.PhotoImage(file=r"icons\cancel.png")
        salir_button = ttk.Button(frame, text="Salir", command=self.subventana.destroy)
        salir_button.grid(row=5, column=1, pady=10)
        add_tooltip(salir_button,"Haz clic aquí para salir.")

        if accion == "eliminar":
            # Botón adicional para buscar en caso de eliminar
            buscar_button = ttk.Button(frame, text="Buscar", command=self.buscar)
            buscar_button.grid(row=5, column=0, pady=5)
            guardar_button.grid_configure(pady=5, column=1)
            salir_button.grid_configure(pady=5, column=2)

    def guardar(self):
        """
        Método para guardar los cambios realizados (crear o eliminar un plato).
        """
        try:
            id_ = int(self.id.get())
            nombre = self.nombre.get()
            precio = self.precio.get()
            cantidad_disponible = self.cantidad_disponible.get()
            descripcion = self.descripcion.get()
        except:
            messagebox.showwarning(message="Ingrese un valor válido")

        # Verificar que todos los campos requeridos estén completos
        if not id_ or self.accion == "crear" and (not nombre or not precio or not cantidad_disponible or not descripcion):
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return
        
        if self.accion == "crear":
            # Crear un nuevo plato y registrarlo
            plato = Plato(id_, nombre, precio, descripcion, cantidad_disponible)
            self.registrador.gestionar_platos(plato, self.accion, self.listaPlatos)
            messagebox.showinfo(message="El plato se ha agregado con éxito")
        elif self.accion == "eliminar":
            # Buscar el plato a eliminar
            plato = self.buscar_platos(id_)
            if not plato:
                messagebox.showwarning(title="Advertencia", message="No se encontró el plato con el ID proporcionado")
                return
            if not messagebox.askyesno(message="¿Desea eliminar el plato?"):
                return
            self.registrador.gestionar_platos(plato, self.accion, self.listaPlatos)
            messagebox.showinfo(message="El plato se ha eliminado con éxito")

    def buscar(self):
        """
        Método para buscar un plato por su ID y mostrar sus detalles en los campos correspondientes.
        """
        id_ = int(self.id.get())
        if not id_:
            messagebox.showwarning("Advertencia", "Ingrese los campos faltantes")
            return

        plato = self.buscar_platos(id_)
        if not plato:
            messagebox.showwarning(title="Advertencia", message="No se encontró el plato con el ID proporcionado")
            return

        # Mostrar los detalles del plato en los campos correspondientes
        self.nombre.set(plato.nombre)
        self.precio.set(plato.precio)
        self.cantidad_disponible.set(plato.cantidad)
        self.descripcion.set(plato.descripcion)

    def buscar_platos(self, id_):
        """
        Método para buscar un plato en la lista de platos por su ID.
        
        Argumentos:
            id_ (str): ID del plato a buscar.
        
        Retorna:
            Plato: Objeto de tipo Plato si se encuentra, None en caso contrario.
        """
        platos = self.listaPlatos
        for plato in platos:
            if plato.id_plato == id_:
                return plato
        return None


