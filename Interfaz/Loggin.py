import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Interfaz.Menu import Menu
from Interfaz.MenuChef.MenuChef import MenuChef
from Interfaz.MenuMesero.MenuMesero import MenuMesero
from Registrador import Registrador
from Chef import Chef
from Mesero import Mesero

__author__ = "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona"
__copyright__ = "Copyright 2024, JMJ"
__credits__ = ["JMJ", "John Esneider Marin Bolivar, Manuel Esteban ramirez, Juan Esteban Agudelo Carmona", "Univalle"]
__license__ = "GPL"
__version__ = "0.1.0"
__maintainer__ = "Equipo JMJ"
__email__ = "john.bolivar@correounivalle.edu.co, manuel.umana@correounivalle.edu.co, juan.agudelo.carmona@corre"
__status__ = "Beta"

class Loggin:
    def __init__(self, loggin, listaComandas, listaInformes, listaPlatos, listaMeseros, listaRegistradores, listaChefs):
        self.loggin = loggin
        self.listaComandas = listaComandas
        self.listaInformes = listaInformes
        self.listaPlatos = listaPlatos
        self.listaMeseros = listaMeseros
        self.listaRegistradores = listaRegistradores
        self.listaChefs = listaChefs
        self.loggin.title("Login")
        self.loggin.geometry("300x250")
        self.loggin.resizable(0,0)

        self.label_user = tk.Label(loggin, text="Usuario:")
        self.label_user.pack(pady=5)
        self.entry_user = tk.Entry(loggin)
        self.entry_user.pack(pady=5)

        self.label_pass = tk.Label(loggin, text="Contraseña:")
        self.label_pass.pack(pady=5)
        self.entry_pass = tk.Entry(loggin, show="*")
        self.entry_pass.pack(pady=5)

        self.lbRol = tk.Label(loggin, text="Rol:*")
        self.lbRol.pack(pady=5)

        opciones = ["registrador", "mesero", "chef"]
        self.cbRol = ttk.Combobox(loggin, values=opciones)
        self.cbRol.set("registrador")
        self.cbRol.pack(pady=5)
        
        self.lbError = tk.Label(loggin, text="", fg="red")
        self.lbError.pack(pady=3)

        self.button_login = tk.Button(loggin, text="Login", command=self.check_login)
        self.button_login.pack(pady=10)

    def check_login(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        rol = self.cbRol.get()

        if user == "Juanes" and password == "123456":
            self.open_registrador_menu()
        elif user == "Esneider" and password == "987654":
            self.open_chef_menu()
        elif user == "Manuel" and password == "456789":
            self.open_mesero_menu()
        else:
            lista = []
            if rol == "registrador":
                lista = self.listaRegistradores
            elif rol == "mesero":
                lista = self.listaMeseros
            elif rol == "chef":
                lista = self.listaChefs
            
            for u in lista:
                if u.nombre == user:
                    if u.cedula == password:
                        if rol == "registrador":
                            self.open_registrador_menu()
                        elif rol == "mesero":
                            self.open_mesero_menu()
                        elif rol == "chef":
                            self.open_chef_menu()
                        return
                    else:
                        self.lbError.config(text="El nombre de usuario o contraseña no son correctos.")
                        break
            self.lbError.config(text="El usuario no exite.")
                            



    def open_registrador_menu(self):
        messagebox.showinfo("Registrador", "Bienvenido, Registrador")
        miRegistrador = Registrador("11151", "juan", "agudelo", "31146446","juan@gmail.com")


        app = Menu(miRegistrador, self.listaInformes, self.listaComandas)

    def open_chef_menu(self):
        messagebox.showinfo("Chef", "Bienvenido, Chef")
        michef = Chef("12345", "Esneider", "Marin", "1234345", "esneider@gmail.com")
        MenuChef(michef, self.listaComandas, self.listaPlatos)

    def open_mesero_menu(self):
        messagebox.showinfo("Mesero", "Bienvenido, Mesero")
        mimesero = Mesero("2355667", "Manuel", "Ramirez", "435677", "manuel@gmail.com")
        MenuMesero(mimesero, self.listaComandas)