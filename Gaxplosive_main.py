import Gaxplosive_funciones as fn
#crear lista de colecciones
lista_pedidos = []
while True:
    opcion = fn.menu()
    if(opcion == 1):
        fn.registrar_pedido(lista_pedidos)
    elif(opcion == 2):
        fn.mostrar_pedidos(lista_pedidos)
    elif(opcion == 3):
        fn.imprimir_hoja(lista_pedidos)
    elif(opcion == 4):
        break
print("Hasta la proxima!")