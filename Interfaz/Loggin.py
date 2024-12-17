import tkinter as tk
from tkinter import ttk
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
        self.loggin.title("Login!")
        self.loggin.geometry("300x250")
        self.loggin.resizable(0,0)
        self.iconBullet = tk.PhotoImage(file=r"icons\bullet_yellow.png")
        self.loggin.iconphoto(True, self.iconBullet)

        self.iconUser = tk.PhotoImage(file=r"icons\user.png")
        self.label_user = tk.Label(loggin, text="Usuario:", image=self.iconUser,compound= "right")
        self.label_user.pack(pady=5)
        self.entry_user = tk.Entry(loggin)
        self.entry_user.pack(pady=5)

        self.iconBuilded = tk.PhotoImage(file= r"icons\building_edit.png")
        self.label_pass = tk.Label(loggin, text="Contraseña:", image=self.iconBuilded, compound= "right")
        self.label_pass.pack(pady=5)
        self.entry_pass = tk.Entry(loggin, show="*")
        self.entry_pass.pack(pady=5)

        self.iconGroup = tk.PhotoImage(file=r"icons\group_go.png")
        self.lbRol = tk.Label(loggin, text="Rol:", image=self.iconGroup, compound= "right")
        self.lbRol.pack(pady=5)

        opciones = ["registrador", "mesero", "chef"]
        self.cbRol = ttk.Combobox(loggin, values=opciones)
        self.cbRol.set("registrador")
        self.cbRol.pack(pady=5)
        
        self.lbError = tk.Label(loggin, text="", fg="red")
        self.lbError.pack(pady=3)

        self.iconGo = tk.PhotoImage(file=r"icons\application_go.png")
        self.button_login = tk.Button(loggin, text="Login", image= self.iconGo, compound="left", command=self.check_login)
        self.button_login.pack(pady=10)

    def check_login(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        rol = self.cbRol.get()

        if user == "Juanes" and password == "123456":
            self.open_registrador_menu(Registrador)
        elif user == "Esneider" and password == "987654":
            self.open_chef_menu(Chef)
        elif user == "Manuel" and password == "456789":
            self.open_mesero_menu(Mesero)
        else:
            lista = []
            if rol == "registrador":
                if self.listaRegistradores:
                    lista = self.listaRegistradores
            elif rol == "mesero":
                if self.listaMeseros:
                    lista = self.listaMeseros
            elif rol == "chef":
                if self.listaChefs:
                    lista = self.listaChefs
            
            for u in lista:
                if u.nombre == user:
                    if u.cedula == password:
                        if rol == "registrador":
                            self.open_registrador_menu(u)
                        elif rol == "mesero":
                            self.open_mesero_menu(u)
                        elif rol == "chef":
                            self.open_chef_menu(u)
                        return
                    else:
                        self.lbError.config(text="El nombre de usuario o contraseña no son correctos.")
                        break
            self.lbError.config(text="El usuario no exite.")
                            


    
    def animate_message(self, message):
        self.message_window = tk.Toplevel(self.loggin)
        self.message_window.title("Hola!")
        self.message_window.geometry("250x100")
        self.message_window.resizable(0, 0)

        self.label_animation = tk.Label(self.message_window, text="", font=("Arial", 10))
        self.label_animation.pack(expand=True)
        self.show_animation(message, 0)

    def show_animation(self, message, index):
        if index < len(message):
            self.label_animation.config(text=message[:index + 1])  
            self.loggin.after(100, self.show_animation, message, index + 1)
        else:
            self.loggin.after(3000, self.message_window.destroy)

    def open_registrador_menu(self, usuario):
        self.animate_message("Bienvenido, Registrador")


        app = Menu(self.loggin, usuario, self.listaInformes, self.listaComandas)

    def open_chef_menu(self, usuario):
        self.animate_message("Bienvenido, Chef")
        MenuChef(self.loggin,usuario, self.listaComandas, self.listaPlatos)

    def open_mesero_menu(self, usuario):
        self.animate_message("Bienvenido, Mesero")
        MenuMesero(self.loggin, usuario, self.listaComandas)