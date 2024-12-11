from Mesero import Mesero
from Mesa import Mesa
from Plato import Plato
from Registrador import Registrador
from Chef import Chef
from Serializador import Serializador
from SerializadorComanda import SerializadorComanda
from Cliente import Cliente

class Main():
    def main():
        def buscar_comanda(id_comanda, listaComandas):
            for comanda in listaComandas:
                if comanda.id == id_comanda:
                    return comanda
            print("Comanda no encontrada.")
        
        def buscar_mesa(id_mesa, listaMesas):
            for mesa in listaMesas:
                if mesa.id_mesa == id_mesa:
                    return mesa
            print("Mesa no encontrada.")
        
        def buscar_mesero(cedula, listaMeseros):
            for mesero in listaMeseros:
                if mesero.cedula == cedula:
                    return mesero
            print("Mesero no encontrada.")
        
        def buscar_chef(cedula, listaChefs):
            for chef in listaChefs:
                if chef.cedula == cedula:
                    return chef
            print("Chef no encontrada.")

        serializadorMesa = Serializador("mesas.txt", Mesa, ["int", "int", "str"])
        serializadorComanda = SerializadorComanda()
        serializadorChef = Serializador("chefs.txt", Chef, ["str", "str", "str", "str", "str"])
        serializadorPlato = Serializador("platos.txt", Plato, ["int", "str", "float", "str"])
        serializadorMesero = Serializador("meseros.txt", Mesero, ["str", "str", "str", "str", "str"])
        serialiazadorRegistrador = Serializador("registradores.txt", Registrador, ["str", "str", "str", "str", "str"])
        serializadorCliente = Serializador("clientes.txt", Cliente, ["str", "str", "str", "str", "str"])
        
        listaMesas = serializadorMesa.leerArchivo()
        listaPlatos = [
            Plato(1, "bistec de pollo", 30000, "delicia"),
            Plato(2, "arroz paisa", 20000, "arroz paisa")
        ]
        listaComandas = serializadorComanda.leerArchivo(listaPlatos)

        listaChefs = serializadorChef.leerArchivo()

        listaMeseros = serializadorMesero.leerArchivo()
        listaClientes = serializadorCliente.leerArchivo()
        miRegistrador = Registrador(12345678, "Manuelito", "el botcito", 321456789, "manuelito@fornait.com", listaMesas, listaMeseros, listaChefs)

        #menú principal
        opcion = 999
        while opcion != 0:

            print("######### INGRESAR #########")
            print("1. Registrador")
            print("2. Mesero")
            print("3. Chef")
            print("0. Salir")

            opcion = int(input("Escriba la opción que desea -> "))
            
            if opcion == 1:
                #Registrador
                regOpt = 999
                while regOpt != 0:
                    print("####### MENÚ REGISTRADOR #######")
                    print("1. Calcular valor total de comanda")
                    print("2. Gestionar Mesas")
                    print("3. Gestionar Meseros")
                    print("4. Gestionar Chefs")
                    print("0. Volver")
                    regOpt = int(input("Escriba la opción que desea -> "))
                    
                    if regOpt == 1:
                        id_comanda = int(input("Ingrese el id de la comanda: "))
                        comanda = buscar_comanda(id_comanda, listaComandas)
                        if comanda:
                            precio = miRegistrador.calcular_precio_total(comanda)
                            print(f"El precio total de la comanda {comanda.id} es de: ${precio}")
                    elif regOpt == 2:
                        print("Gestionar Mesas")
                        print("1. Crear")
                        print("2. Eliminar")
                        accion = int(input("Escriba la opción que desea -> "))
                        if accion == 1:
                            accion = "crear"
                            comensales = int(input("Ingrese la cantidad de comensales de la nueva mesa: "))
                            mesa = Mesa(len(listaMesas)+1, comensales)
                        elif accion == 2:
                            accion = "eliminar"
                            idMesa = int(input("Ingrese el id de la mesa a eliminar: "))
                            mesa = buscar_mesa(idMesa, listaMesas)
                        else:
                            print("Opción no válida.")
                            continue
                        if mesa:
                            miRegistrador.gestionar_mesas(mesa, accion)
                            print(f"Se ha realizado la acción de {accion} correctamente.")
                    elif regOpt == 3:
                        print("Gestionar Meseros")
                        print("1. Crear")
                        print("2. Eliminar")
                        accion = int(input("Escriba la opción que desea -> "))
                        if accion == 1:
                            accion = "crear"
                            cedula = input("Ingrese la cedula del nuevo mesero: ")
                            nombre = input("Ingrese el nombre del nuevo mesero: ")
                            apellido = input("Ingrese el apellido del nuevo mesero: ")
                            telefono = input("Ingrese el número de teléfono del nuevo mesero: ")
                            email = input("Ingrese el email del nuevo mesero: ")
                            mesero = Mesero(cedula, nombre, apellido, telefono, email, listaMesas, listaComandas, listaPlatos)
                        elif accion == 2:
                            accion = "eliminar"
                            cedulaMesero = input("Ingrese la cedula del mesero a eliminar: ")
                            mesero = buscar_mesero(cedulaMesero, listaMeseros)
                        else:
                            print("Opción no válida.")
                            continue
                        if mesero:
                            miRegistrador.gestionar_meseros(mesero, accion)
                            print(f"Se ha realizado la acción de {accion} correctamente.")
                    elif regOpt == 4:
                        print("Gestionar Chefs")
                        print("1. Crear")
                        print("2. Eliminar")
                        accion = int(input("Escriba la opción que desea -> "))
                        if accion == 1:
                            accion = "crear"
                            cedula = input("Ingrese la cedula del nuevo chef: ")
                            nombre = input("Ingrese el nombre del nuevo chef: ")
                            apellido = input("Ingrese el apellido del nuevo chef: ")
                            telefono = input("Ingrese el número de teléfono del nuevo chef: ")
                            email = input("Ingrese el email del nuevo chef: ")
                            chef = Chef(cedula, nombre, apellido, telefono, email, listaPlatos)
                        elif accion == 2:
                            accion = "eliminar"
                            cedulaChef = input("Ingrese la cedula del chef a eliminar: ")
                            chef = buscar_chef(cedulaChef, listaChefs)
                        else:
                            print("Opción no valida.")
                            continue
                        if chef:
                            miRegistrador.gestionar_chef(chef, accion)
                            print(f"Se ha realizado la acción de {accion} correctamente.")
                    elif regOpt != 0:
                        print("Opción no válida.")
            elif opcion == 2:
                #Mesero
                cedula = input("Ingrese la cédula del mesero: ")
                miMesero = buscar_mesero(cedula, listaMeseros)
                miMesero.setMesas(listaMesas)
                miMesero.setComandas(listaComandas)
                miMesero.setPlatos(listaPlatos)

                if miMesero:
                    mesOpt = 999
                    while mesOpt != 0:
                        print("######### MENÚ MESERO ##########")
                        print("1. Consultar Mesa")
                        print("2. Tomar Comandas")
                        print("3. Procesar estado comanda")
                        print("4. Servir comanda")
                        print("5. Liberar Mesa")
                        print("0. Volver")
                        mesOpt = int(input("Escriba la opción que desea -> "))

                        if mesOpt == 1:
                            mesas = miMesero.consultar_disponibilidad_mesas()
                            print("Mesas Disponibles: ")
                            for mesa in mesas:
                                print(f"Mesa {mesa.id_mesa}\n Estado: {mesa.estado}")
                        elif mesOpt == 2:
                            comandasOpt = 999
                            while comandasOpt != 0:
                                print("1. Seleccionar y ocupar mesa")
                                print("2. Crear comanda")
                                print("3. Agregar plato a la comanda")
                                print("4. Eliminar plato a la comanda")
                                print("5. Guadar Comanda")
                                print("0. Volver")
                                comandasOpt = int(input("Seleccione una opción -> "))

                                if comandasOpt == 1:
                                    miMesero.ocupar_mesa()
                                elif comandasOpt == 2:
                                    miMesero.tomar_comanda(listaClientes)
                                elif comandasOpt == 3:
                                    miMesero.agregar_plato_comanda()
                                elif comandasOpt == 4:
                                    miMesero.eliminar_plato_comanda()
                                elif comandasOpt == 5:
                                    miMesero.guardar_comanda()
                                elif comandasOpt != 0:
                                    print("Opción no válida.")
                        elif mesOpt == 3:
                            miMesero.cambiar_estado_comanda()
                        elif mesOpt == 4:
                            miMesero.calcular_precio_total()
                        elif mesOpt == 5:
                            miMesero.liberar_mesa()
                        elif mesOpt != 0:
                            print("Opción no válida")
            elif opcion == 3:
                #Chef
                cedula = input("Ingrese la cédula del chef: ")
                miChef = buscar_chef(cedula, listaChefs)
                if miChef:
                    chefOpt = 999
                    while chefOpt != 0:
                        print("####### MENÚ CHEF ########")
                        print("1. Cambiar estado comanda")
                        print("2. Gestionar Platos")
                        chefOpt = int(input("Escriba la opción que desea -> "))

                        if chefOpt == 1:
                            idComanda = int(input("Ingrese el Id de la comanda: "))
                            comanda = buscar_comanda(idComanda, listaComandas)
                            if comanda:
                                print("Estado")
                                print("1. pendiente")
                                print("2. En preparación")
                                print("3. servido")
                                estado = int(input("Seleccióne el estado -> "))
                                if estado == 1:
                                    estado = "pendiente"
                                elif estado == 2:
                                    estado = "en preparacion"
                                elif estado == 3:
                                    estado = "servido"
                                else:
                                    print("Opción no válida.")
                                    continue
                                miChef.cambiar_estado_comanda(comanda, estado)
                                texto = ""
                                for comanda in listaComandas:
                                    texto = f"{comanda.id}\n{comanda.mesa}\n{comanda.cliente}\n{comanda.precio_total}\n{comanda.estado}\n"
                                    i=0
                                    for plato in comanda.platos:
                                        texto+=f"{plato[0]},{plato[1]}"
                                        if i < len(comanda.platos) - 1:
                                            texto+="|"
                                        i+=1
                                    texto+="\n"
                                serializadorComanda.escribirTodo(texto)
                        elif chefOpt == 2:
                            print("Gestionar Platos")
                            print("1. Crear")
                            print("2. Eliminar")
                            accion = int(input("Seleccione una acción -> "))
                            if accion == 1:
                                accion = "crear"
                            elif accion == 2:
                                accion = "elminar"
                            else:
                                print("Opción no válida")
                                continue
                            miChef.gestionar_platos(accion, listaPlatos)
            elif opcion == 0:
                print("Hasta pronto")
            else:
                print("Opción no válida")

    main()