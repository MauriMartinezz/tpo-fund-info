import random

# Constantes
MINIMO_VENTAS_DIARIAS = 20
MAXIMO_VENTAS_DIARIAS = 200
MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
         'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
PRODUCTOS = ['SILLAS', 'MESAS', 'SILLONES', 'RACKS TV', 'CAMAS']

# Códigos de productos
COD_CAMAS = 5
COD_RACKS_TV = 4
COD_SILLONES = 3
COD_MESAS = 2
COD_SILLAS = 1

# Precios de ventas de productos
PDV_SILLAS = [55000, 62000, 68000, 70000]
PDV_MESAS = [145000, 160000, 180000, 200000]
PDV_SILLONES = [200000, 300000, 400000, 450000]
PDV_RACKS_TV = [158000, 165000, 170000, 200000]
PDV_CAMAS = [50000, 70000, 85000, 110000]


# Variables
facturacion_dia = [0]*30
ventas_dia = [0]*30

facturacion_por_producto = [0, 0, 0, 0, 0]
facturacion_por_modelo = [[0, 0, 0, 0], [0, 0, 0, 0],
                          [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

clientes_unicos_por_producto = [[], [], [], [], []]
clientes_totales = []
articulos_comprados = []


clientes = []
ventas_cliente = []
facturacion_por_cliente = []

mes = 0
dia = 0
anio = 0

while (mes > len(MESES) or mes <= 0):
    mes = int(input("Ingrese el mes que desea consultar... "))

while (anio < 2000 or anio > 2024):
    anio = int(input("Ingrese el anio que desea consultar... "))


# Funciones

def get_usuario_index(id_usuario):
    for i in range(len(clientes)):
        if clientes[i] == id_usuario:
            return i


def generar_datos(dia):
    ventas_contador = 0
    ventas_generadas = random.randint(
        MINIMO_VENTAS_DIARIAS, MAXIMO_VENTAS_DIARIAS)
    while (ventas_contador < ventas_generadas):
        ventas_contador += 1
    # Creo ID de cliente, numero al azar entre 1000 y 10000
        id_cliente = random.randint(1000, 9999)
    # Si no existe este ID, lo agrego al array
    # de IDs de clientes_unicos_unicos_unicos
        if id_cliente not in clientes:
            clientes.append(id_cliente)
            ventas_cliente.append(1)
        else:
            ventas_cliente[get_usuario_index(id_cliente)] += 1

    # Cada iteración significa una nueva venta para el mes
    # En una posicion al azar del mes, agrego la venta
        ventas_dia[dia - 1] = ventas_contador

    # Selecciono un producto al azar entre
    # SILLAS, MESAS, SILLONES, RACKS_TV & CAMAS
        producto_seleccionado = PRODUCTOS[random.randint(
            1, len(PRODUCTOS)) - 1]

    # Dependiendo qué producto sea, selecciono un modelo de dicho
    # producto al azar
    # Luego sumo a facturacion_dia el precio de ese modelo
        match producto_seleccionado:
            case 'SILLAS':
                indice_modelo = random.randint(1, 4) - 1
                precio_producto = PDV_SILLAS[indice_modelo]
                facturacion_dia[dia - 1] += precio_producto

                # Sumar ventas a producto y modelo
                # SILLAS esta en la posicion 0, lo que varia es el modelo
                facturacion_por_producto[0] += precio_producto
                facturacion_por_modelo[0][indice_modelo] += precio_producto

                # Si no existe este ID en la lista de
                # clientes_unicos_unicos_unicos de producto se agrega al array
                if id_cliente not in clientes_unicos_por_producto[0]:
                    clientes_unicos_por_producto[0].append(id_cliente)

            case 'MESAS':
                indice_modelo = random.randint(1, 4) - 1
                precio_producto = PDV_MESAS[indice_modelo]
                facturacion_dia[dia - 1] = precio_producto

                # Sumar ventas a producto y modelo
                # MESAS esta en la posicion 2, lo que varia es el modelo
                facturacion_por_producto[1] += precio_producto
                facturacion_por_modelo[1][indice_modelo] += precio_producto

                # Si no existe este ID en la lista de
                # clientes_unicos_unicos_unicos de producto se agrega al array
                if id_cliente not in clientes_unicos_por_producto[1]:
                    clientes_unicos_por_producto[1].append(id_cliente)
            case 'SILLONES':
                indice_modelo = random.randint(1, 4) - 1
                precio_producto = PDV_SILLONES[indice_modelo]
                facturacion_dia[dia - 1] += precio_producto

                # Sumar ventas a producto y modelo
                # SILLONES esta en la posicion 2, lo que varia es el modelo
                facturacion_por_producto[2] += precio_producto
                facturacion_por_modelo[2][indice_modelo] += precio_producto

                # Si no existe este ID en la lista de
                # clientes_unicos_unicos_unicos de producto se agrega al array
                if id_cliente not in clientes_unicos_por_producto[2]:
                    clientes_unicos_por_producto[2].append(id_cliente)
            case 'RACKS TV':
                indice_modelo = random.randint(1, 4) - 1
                precio_producto = PDV_RACKS_TV[indice_modelo]
                facturacion_dia[dia - 1] += precio_producto

                # Sumar ventas a producto y modelo
                # RACKS_TV esta en la posicion 2, lo que varia es el modelo
                facturacion_por_producto[3] += precio_producto
                facturacion_por_modelo[3][indice_modelo] += precio_producto

                # Si no existe este ID en la lista de
                # clientes_unicos_unicos_unicos de producto se agrega al array
                if id_cliente not in clientes_unicos_por_producto[3]:
                    clientes_unicos_por_producto[3].append(id_cliente)
            case 'CAMAS':
                indice_modelo = random.randint(1, 4) - 1
                precio_producto = PDV_CAMAS[indice_modelo]
                facturacion_dia[dia - 1] += precio_producto

                # Sumar ventas a producto y modelo
                # RACKS_TV esta en la posicion 2, lo que varia es el modelo
                facturacion_por_producto[4] += precio_producto
                facturacion_por_modelo[4][indice_modelo] += precio_producto

                # Si no existe este ID en la lista de
                # clientes_unicos_unicos_unicos de producto se agrega al array
                if id_cliente not in clientes_unicos_por_producto[4]:
                    clientes_unicos_por_producto[4].append(id_cliente)
# Funcion que imprime el menu por pantalla
# Se agregan las opciones necesarias segun el programa de cada uno.


def generar_datos_mensual():
    for i in range(30):
        generar_datos(i)


def get_facturacion_mensual():
    total = 0
    for i in range(len(facturacion_dia)):
        total += facturacion_dia[i]

    return total


def get_ventas_mensuales():
    ventas = 0
    for i in range(len(ventas_dia)):
        ventas += ventas_dia[i]

    return ventas


def get_fecha_formateada(dia_seleccionado):
    fecha_formateada = dia_seleccionado + \
        " de " + MESES[mes - 1] + " del " + anio

    return fecha_formateada


def imprimir_menu():
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


def get_total_por_mes(mes):
    print()
    print("Mes ", MESES[mes - 1])
    print()

    print("Total facturado en ",
          MESES[mes - 1], ' $', get_facturacion_mensual())
    print("Ventas realizadas: ", get_ventas_mensuales())
    print("Clientes unicos: ", len(clientes))
    print("Costo de adquisicion productos vendidos: ")
    print()

# Opción II


def total_por_producto_y_modelo(producto):
    print()
    print("Producto elegido: ", PRODUCTOS[producto])
    print()

    print("Total facturado: ", facturacion_por_producto[producto])
    print()
    for i in range(len(facturacion_por_modelo[producto])):
        print("Ventas modelo ", i + 1, facturacion_por_modelo[producto][i])
    print()
    print("Clientes únicos: ", len(
        clientes_unicos_por_producto[producto]))
    print("Costo adquisicion productos vendidos: ")

# Opción III


def get_ventas_mensuales_por_cliente():
    print()
    print("Mes ", mes, " del ", anio)
    print()
    for i in range(len(clientes)):
        print("ID Cliente: ", clientes[i])
        print("Artículos comprados: ", ventas_cliente[i])
        print("Total facturado cliente: ")


# Opción IV


def detalle_por_dia():
    for i in range(len(ventas_dia)):
        print()
        print(i + 1, "/", mes, "/", anio)
        print("-----------------------------------")
        print("Ventas realizadas: ", ventas_dia[i])
        print("Total facturado del dia: ", facturacion_dia[i])
        print("-----------------------------------")
        print()
    print()

# Opción V


def detalle_del_dia(dia):
    print()
    print("Día: ", dia)
    print()

    print("ID cliente: ")
    print("Tipo de producto: ")
    print("Modelo: ")
    print("Total facturado: ")


# ***********************
# Programa principal
# ***********************


print("\nBienvenido al programa\n")
generar_datos_mensual()
# Leer la primera vez la opcion del menu
imprimir_menu()
opcion = int(input("Ingrese la opcion elegida del menu principal: "))


# Comienzo del proceso de las opciones del menu elegidas.

while opcion != 6:

    flagMenu = validarOpcionMenu(opcion)
    while flagMenu is False:
        print("Opcion de menu invalida, ingrese una opción válida...")
        print()
        opcion = int(input("Ingrese la opcion elegida del menu principal: "))
        flagMenu = validarOpcionMenu(opcion)

    # Analizamos las opciones validas del menú
    if opcion == 1:
        # Instrucciones para la opcion 1
        print()
        print("Resumen mensual")
        get_total_por_mes(mes)
    elif opcion == 2:
        print("Resumen por tipo de producto y modelo")
        print("1. Sillas")
        print("2. Mesas")
        print("3. Sillones")
        print("4. Racks de TV")
        print("5. Camas")
        print()
        productoAConsultar = int(
            input("Ingrese el código del producto que desea consultar..."))

        total_por_producto_y_modelo(productoAConsultar - 1)
        # ingreso de datos para opcion 2
        # proceso de datos para opcion 2
        # impresion de datos para opcion 2
    elif opcion == 3:
        print("Detalles por cliente: ")
        get_ventas_mensuales_por_cliente()
        # proceso de datos para opcion 3
        # impresion de datos para opcion 3
    elif opcion == 4:
        print()
        print("********************************************************************")
        print()
        print("Detalles por día: ", MESES[mes - 1], " del ", anio)
        detalle_por_dia()
    elif opcion == 5:
        print("Detalle del día")
        detalle_del_dia()
    else:
        print("*************************")
        print("Ingrese un número válido")
        print("*************************")
    # Luego de procesar la opcion del menu elegida
    # Vuelvo a invocar al menu
    imprimir_menu()
    opcion = int(input("Ingrese la opcion elegida del menu principal: "))

else:
    print("GUSBAY")

# Fin del programa
