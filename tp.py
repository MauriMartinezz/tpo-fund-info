import random
#-----------------------------------------------------------------------------------------
#-----------------     Plantilla para diseño de un menú ----------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
    
# Constantes
MINIMO_VENTAS_DIARIAS = 20
MAXIMO_VENTAS_DIARIAS = 200
MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO','AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
PRODUCTOS = ['SILLAS', 'MESAS', 'SILLONES', 'RACKS TV', 'CAMAS']

# Códigos de productos
COD_CAMAS = 5
COD_RACKS_TV = 4
COD_SILLONES = 3
COD_MESAS = 2
COD_SILLAS = 1

# Precios de ventas de productos
PDV_SILLAS = [55000, 62000, 68000,70000]
PDV_MESAS = [145000, 160000,180000,200000]
PDV_SILLONES = [200000,300000, 400000, 450000]
PDV_RACKS_TV = [158000, 165000, 170000, 200000]
PDV_CAMAS = [50000, 70000, 85000, 110000]

# Variables
ventas_dia = 0
ventas_mensuales = [0,0,0,0,0,0,0,0,0,0,0,0]
facturacion_mensual = [0,0,0,0,0,0,0,0,0,0,0,0]
clientes = []
dia = 0
mes = 0
anio = 0
anios_con_ventas = []
while (dia > 30 or dia <= 0):
    dia = int(input("Ingrese el día de la fecha... "))

while (mes > len(MESES) or mes <= 0):
    mes = int(input("Ingrese el numero del mes... "))

while (anio < 1990):
    anio = int(input("Ingrese el año... "))

#Funciones
def agregar_anio_array(anio):
    if chequear_anio_array(anio) == False:
        anios_con_ventas.append(anio)

def chequear_anio_array(anio):
    existe_anio_en_array = False
    for i in anios_con_ventas:
        if anios_con_ventas[i] == anio:
            existe_anio_en_array = True
    return existe_anio_en_array


def generar_datos():
    ventas_contador = 0
    ventas_generadas = random.randint(MINIMO_VENTAS_DIARIAS, MAXIMO_VENTAS_DIARIAS)
    while(ventas_contador < ventas_generadas ):
        ventas_contador += 1
    # Creo ID de cliente, numero al azar entre 1000 y 10000
        id_cliente = random.randint(1000, 9999)
    # Si no existe este ID, lo agrego al array de IDs de clientes
        if id_cliente not in clientes:
            clientes.append(id_cliente)

    # Cada iteración significa una nueva venta para ele mes
        ventas_mensuales[mes - 1] += 1

    # Selecciono un producto al azar entre
    # SILLAS, MESAS, SILLONES, RACKS_TV & CAMAS
        producto_seleccionado = PRODUCTOS[random.randint(1,len(PRODUCTOS)) - 1]

    # Dependiendo qué producto sea, selecciono un modelo de dicho producto al azar
    # Luego sumo a total_facturado_mes el precio de ese modelo
        if producto_seleccionado == 'SILLAS':
            precio_producto = PDV_SILLAS[random.randint(1,4) - 1]
            facturacion_mensual[mes - 1] += precio_producto

        elif producto_seleccionado == 'MESAS':
            precio_producto = PDV_MESAS[random.randint(1,4) - 1]
            facturacion_mensual[mes -1] += precio_producto

        elif producto_seleccionado == 'SILLONES':
            precio_producto = PDV_SILLONES[random.randint(1,4) - 1]
            facturacion_mensual[mes - 1 ] += precio_producto

        elif producto_seleccionado == 'RACKS_TV':
            precio_producto = PDV_RACKS_TV[random.randint(1,4) - 1]
            facturacion_mensual[mes - 1] += precio_producto

        else:
            precio_producto = PDV_CAMAS[random.randint(1,4) - 1]
            facturacion_mensual[mes - 1] += precio_producto

        
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
    if opcion > 6 or opcion < 1:
        return False
    else:
        return True

# Opción I
#
def totalPorMes():
    generar_datos()
    print()
    print("Mes ", MESES[mes - 1], ' ',anio)
    print()

    print("Total facturado en ", MESES[mes -1] , ' $', facturacion_mensual[mes - 1])
    print("Ventas realizadas: ", ventas_mensuales[mes - 1])
    print("Clientes unicos: ", len(clientes))
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


print("\nBienvenido al programa\n")

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
        print("")
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





