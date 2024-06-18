def menu():
    print("----Bienvenido!----")
    print("1) Registrar pedido")
    print("2) Listar todos los pedidos")
    print("3) Imprimir hoja de ruta")
    print("4) Salir")
    while True:
        try:
            respuesta = int(input("Ingrese su opcion: "))
            break
        except:
            print("Ha ocurrido un problema, intente de nuevo!")
    return respuesta

def registrar_pedido(lista_pedidos):
    pedido = {}
    print("----Orden de pedido----")
    pedido["Nombre"] = input("Ingrese su nombre: ") + " "
    pedido["Nombre"] += input("Ingrese su apellido: ")
    pedido["Comuna"] = input("Ingrese su comuna: ")
    pedido["Sector"] = input("Ingrese el sector: ")
    pedido["Direccion"] = input("Ingrese la direccion: ")
    pedido["Cilindros_5kg"] = 0
    pedido["Cilindros_15kg"] = 0
    pedido["Cilindros_45kg"] = 0
    while True:
        print()
        print("Ingrese uno de los tipos de cilindros a pedir")
        print("1)Cilindros de  5 kgs")
        print("2)Cilindros de 15 kgs")
        print("3)Cilindros de 45 kgs")
        print("4)Salir")
        print()
        while True:
            try:
                opcion = int(input("Ingrese su opcion: "))
                break
            except:
                print("Ha ocurrido un problema, intente de nuevo!")
        if(opcion == 1):
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a pedir: "))
                    break
                except:
                    print("Ha ocurrido un problema, intente de nuevo!")
            pedido["Cilindros_5kg"] += cantidad
        elif(opcion == 2):
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a pedir: "))
                    break
                except:
                    print("Ha ocurrido un problema, intente de nuevo!")
            pedido["Cilindros_15kg"] += cantidad
        elif(opcion == 3):
            while True:
                try:
                    cantidad = int(input("Ingrese la cantidad a pedir: "))
                    break
                except:
                    print("Ha ocurrido un problema, intente de nuevo!")
            pedido["Cilindros_45kg"] += cantidad
        elif(opcion == 4):
            break
    print("Pedido archivado!")
    lista_pedidos.append(pedido)

def mostrar_pedidos(lista_pedidos):
    print("Cliente       Dirección       Sector         Cil. 5kg        Cil. 15kg        Cil. 45kg")
    for pedido in lista_pedidos:
        print(f"{pedido["Nombre"]}     {pedido["Comuna"]}     {pedido["Sector"]}     {pedido["Cilindros_5kg"]}      {pedido["Cilindros_15kg"]}     {pedido["Cilindros_45kg"]}")

def imprimir_hoja(lista_pedidos):
    lista_sectores = []
    for pedido in lista_pedidos:
        if(pedido["Sector"] not in lista_sectores):
            lista_sectores.append(pedido["Sector"])
    for sectores in lista_sectores:
        print(f"{sectores}    ",end="")
    sector_ingresado = input("Ingrese uno de los sectores disponibles: ")
    if sector_ingresado in lista_sectores:
        with open(f"{sector_ingresado}.txt","w") as archivo:
            archivo.write("Cliente       Dirección       Sector         Cil. 5kg        Cil. 15kg        Cil. 45kg\n")
            for pedido in lista_pedidos:
                if(pedido["Sector"] == sector_ingresado):
                    archivo.write(f"{pedido["Nombre"]}     {pedido["Comuna"]}     {pedido["Sector"]}     {pedido["Cilindros_5kg"]}      {pedido["Cilindros_15kg"]}     {pedido["Cilindros_45kg"]}\n")
                    