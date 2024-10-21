-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------     Plantilla para diseño de un menú ----------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

# Variables

ventas_dia = 0

ventas_mensuales = [0,0,0,0,0,0,0,0,0,0,0,0]
facturacion_mensual = [0,0,0,0,0,0,0,0,0,0,0,0]

# Constantes
MINIMO_VENTAS_DIARIAS = 20
MAXIMO_VENTAS_DIARIAS = 200
MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO','AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
PRODUCTOS = ['SILLAS', 'MESAS', 'SILLONES', 'RACKS TV', 'CAMAS']
PDV_SILLAS = [55000, 62000, 68000,70000]
PDV_MESAS = [145000, 160000,180000,200000]
PDV_SILLONES = [200000,300000, 400000, 450000]
PDV_RACKS_TV = [158000, 165000, 170000, 200000]
PDV_CAMAS = [50000, 70000, 85000, 110000]

#Funciones
 
#Funcion que imprime el menu por pantalla
#Se agregan las opciones necesarias segun el programa de cada uno.
def imprimirMenu():
    print()
    print("********************************************")
    print("Debe elegir una opcion, solo numeros enteros")
    print("1 - Ver total del mes")   
    print("2 - Ver resumen por tipo de producto y modelo")
    print("3 - Ver detalles por cliente")
    print("4 - Ver detalles por día")
    print("5 - Ver detalles del día")
    print("6 - Salir")
    print("********************************************")
    print()
    
    return


# Funcion que valida que las opciones elegidas del menu sean las correctas.
# Solo valida numeros. Si se ingresa letras se corta el programa.
# Agregar las opciones necesarias segun el programa de cada uno.

def validarOpcionMenu(opcion):
    if opcion > 6 or opcion < 1
        return False
    else:
        return True

# Opción I
#
def totalPorMes():
    print()
    print("Mes Agosto 2024")
    print()

    print("Total facturado: ")
    print("Total ventas realizadas: ")
    print("Clientes unicos: ")
    print("Costo de adquisicion productos vendidos: ")
    print()

# Opción II
#
def totalPorProductoYModelo(producto):
    print()
    print("Producto elegido: ", producto)
    print()

    print("Total facturado: ")
    print("Ventas modelo I: ")
    print("Ventas modelo II: ")
    print("Ventas modelo III: ")
    print("Ventas modelo IV: ")
    print("Clientes únicos: ")
    print("Costo adquisicion productos vendidos: ")

# Opción III
#
def ventasMensualesPorCliente(mes):
    print()
    print("Mes ")
    print()
    print("ID Cliente: ")
    print("Artículos comprados: ")
    print("Total facturado cliente: ")


# Opción IV
#
def detallePorDia(mes):
    print()
    print("Mes ")
    print()

    print("Dia ")
    print("Ventas realizadas: ")
    print("Total facturado del dia: ")


# Opción V 
#
def detalleDelDia(dia):
    print()
    print("Día: ", dia)
    print()

    print("ID cliente: ")
    print("Tipo de producto: ")
    print("Modelo: ")
    print("Total facturado: ")


# ***********************   
#Programa principal
#************************   


print("Bienvenido al programa\n")

#Leer la primera vez la opcion del menu
imprimirMenu()
opcion=int(input("Ingrese la opcion elegida del menu principal: "))

#Comienzo del proceso de las opciones del menu elegidas.

while opcion != 6:

    flagMenu = validarOpcionMenu(opcion)
    while flagMenu == False:
        print("Opcion de menu invalida, ingrese una opción válida...")
        print()
        opcion=int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu=validarOpcionMenu(opcion)

    #Analizamos las opciones validas del menú
    if opcion == 1:
        #Instrucciones para la opcion 1
        print("Resumen mensual")
        totalPorMes()
    elif opcion == 2:
        print("Resumen por tipo de producto y modelo")
        totalPorProductoYModelo()
        #ingreso de datos para opcion 2
        #proceso de datos para opcion 2
        #impresion de datos para opcion 2
    elif opcion == 3:
        print("Detalles por cliente: ")
        ventasMensualesPorCliente()
        #proceso de datos para opcion 3
        #impresion de datos para opcion 3
    elif opcion == 4:
        print("Detalles por día")
        detallePorDia()
    elif opcion == 5:
        print("Detalle del día")
        detalleDelDia()
    else:
        print("*************************")
        print("Ingrese un número válido")
        print("*************************")
    #Luego de procesar la opcion del menu elegida
    #Vuelvo a invocar al menu
    imprimirMenu()   
    opcion=int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("FIN DEL PROGRAMA")
    
    

#Fin del programa
