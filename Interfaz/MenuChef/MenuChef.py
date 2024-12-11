import tkinter as tk
from tkinter import messagebox
from Interfaz.MenuChef.GestionarPlatos import GestionarPlato
from Interfaz.MenuChef.CambiarEstado import CambiarEstado

class MenuChef():
    """
    Clase para gestionar el menú principal de la aplicación para un chef. Permite agregar o eliminar platos,
    cambiar el estado de comandas y salir de la aplicación.

    Atributos:
        ventana (tk.Tk): Ventana principal de la aplicación.
        Chef (Chef): Objeto que representa al chef.
        comandas (list): Lista de comandas.
    """
    def Salir(self):
        """Método para salir de la aplicación, muestra una confirmación antes de cerrar la ventana."""
        respuesta = messagebox.askquestion("Confirmacion", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def agregarPlato(self):
        agregar = GestionarPlato(self.ventana, self.Chef, "crear", self.platos)

    def eliminarPlato(self):
        eliminar = GestionarPlato(self.ventana, self.Chef, "eliminar", self.platos)

    def cambiarEstado(self):
        cambiar = CambiarEstado(self.ventana, self.Chef, self.comandas) 

    def __init__(self, Chef, comandas, platos):
        self.ventana = tk.Tk()
        self.ventana.geometry("535x400")
        self.ventana.title("Menú Principal")
        self.ventana.resizable(0, 0)
        self.ventana.focus_set()
        self.ventana.configure(bg="white")
        self.Chef = Chef
        self.comandas = comandas
        self.platos = platos

        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)
        menuPlatos = tk.Menu(self.menu)

        self.lblElaborado = tk.Label(self.ventana, text="Elaborado por:\n John Esneider Marin\n Juan Esteban Agudelo\n Manuel Esteban Ramirez")
        self.lblElaborado.grid(row=8, column=5, padx=(250, 0))

        self.lblBienvenido = tk.Label(self.ventana, text=f"Bienvenido!!!")
        self.lblBienvenido.grid(row=5, column=4, columnspan=2, padx=150, pady=150)

        self.menu.add_cascade(label="Gestionar Platos", menu=menuPlatos)
        menuPlatos.add_command(label="Agregar Plato", command=lambda: self.agregarPlato())
        menuPlatos.add_separator()
        menuPlatos.add_command(label="Eliminar Plato", command=lambda: self.eliminarPlato())

        menuComandas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Comandas", menu=menuComandas)
        menuComandas.add_command(label="Cambiar Estado", command=lambda: self.cambiarEstado())

        menuSalir = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=menuSalir)
        menuSalir.add_command(label="Salir", command=lambda: self.Salir())

        self.ventana.mainloop()
        

