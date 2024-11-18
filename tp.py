import random

# Constantes
MINIMO_VENTAS_DIARIAS = 20
MAXIMO_VENTAS_DIARIAS = 200
MESES = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO',
         'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
PRODUCTOS = ['SILLAS', 'MESAS', 'SILLONES', 'RACKS TV', 'CAMAS']

PRECIOS_DE_VENTA = [
    [55000, 62000, 68000, 70000],
    [145000, 160000, 180000, 200000],
    [200000, 300000, 400000, 450000],
    [158000, 165000, 170000, 200000],
    [50000, 70000, 85000, 110000]
]

# Códigos de productos
COD_CAMAS = 5
COD_RACKS_TV = 4
COD_SILLONES = 3
COD_MESAS = 2
COD_SILLAS = 1


# Variables
facturacion_dia = [0]*30
ventas_dia = [0]*30

facturacion = [[0, 0, 0, 0], [0, 0, 0, 0], [
    0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

ventas_por_producto = [[0, 0, 0, 0], [0, 0, 0, 0],
                       [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

clientes_del_dia = [[] for _ in range(30)]
ventas_producto_dia = [[] for _ in range(30)]
ventas_modelo_detalle_dia = [[] for _ in range(30)]
facturacion_por_venta_dia = [[] for _ in range(30)]


clientes_totales = []
articulos_comprados = []

clientes = []
ventas_clientes = []
facturacion_por_cliente = []

mes = 0
dia = 0
anio = 0

while (mes > len(MESES) or mes <= 0):
    mes = int(input("Ingrese el mes que desea consultar... "))

while (anio < 2000 or anio > 2024):
    anio = int(input("Ingrese el anio que desea consultar... "))


# Funciones

def get_facturacion():
    total = 0
    for i in range(len(facturacion)):
        for j in range(len(facturacion[i])):
            total += facturacion[i][j]

    return total


def get_usuario_index(id_usuario):
    i = 0
    while (i < len(clientes)):
        if (clientes[i] == id_usuario):
            return i
        i += 1
    return -1


def generar_venta(producto, modelo, cliente, dia):
    precio = PRECIOS_DE_VENTA[producto][modelo]
    indice_cliente = get_usuario_index(cliente)

    if (indice_cliente == -1):
        clientes.append(cliente)
        ventas_clientes.append(1)
        facturacion_por_cliente.append(precio)
    else:
        ventas_clientes[indice_cliente] += 1
        facturacion_por_cliente[indice_cliente] += precio

    facturacion[producto][modelo] += precio
    ventas_por_producto[producto][modelo] += 1

    ventas_modelo_detalle_dia[dia].append(modelo)
    ventas_producto_dia[dia].append(producto)
    facturacion_por_venta_dia[dia].append(precio)
    clientes_del_dia[dia].append(cliente)

    return precio


def crear_datos(dia):
    ventas_contador = 0

    ventas_del_dia = random.randint(
        MINIMO_VENTAS_DIARIAS, MAXIMO_VENTAS_DIARIAS)

    ventas_dia[dia] = ventas_del_dia

    while (ventas_contador < ventas_del_dia):
        ventas_contador += 1

        id_cliente = random.randint(1000, 9999)

        producto_vendido = random.randint(0, len(PRODUCTOS) - 1)
        modelo_vendido = random.randint(0, 3)

        valor_venta = generar_venta(
            producto_vendido, modelo_vendido, id_cliente, dia)

        facturacion_dia[dia] += valor_venta


def generar_datos_mensual():
    for i in range(30):
        crear_datos(i)


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


def sumar_elementos_array(array):
    total = 0

    for i in range(len(array)):
        total += array[i]

    return total

def ordenar_ids_descendente(dia_elegido):
    desordenada = True
    while desordenada:
        desordenada = False

        for i in range(len(clientes_del_dia[dia_elegido ]) - 1):
            if clientes_del_dia[dia_elegido ][i] > clientes_del_dia[dia_elegido ] [i+1]:
                aux = clientes_del_dia[dia_elegido ][i]
                auxVentasProducto = ventas_producto_dia[dia_elegido ][i]
                auxVentasModelo = ventas_modelo_detalle_dia[dia_elegido ][i]
                auxFacturacion = facturacion_por_venta_dia[dia_elegido ][i]

                clientes_del_dia[dia_elegido ][i] = clientes_del_dia[dia_elegido ][i+1]
                clientes_del_dia[dia_elegido ][i+1] = aux

                ventas_producto_dia[dia_elegido ][i] = ventas_producto_dia[dia_elegido ][i + 1]
                ventas_modelo_detalle_dia[dia_elegido ][i] = ventas_modelo_detalle_dia[dia_elegido ][i + 1]
                facturacion_por_venta_dia[dia_elegido ][i] = facturacion_por_venta_dia[dia_elegido ][i + 1]

                ventas_producto_dia[dia_elegido ][i + 1] = auxVentasProducto
                ventas_modelo_detalle_dia[dia_elegido ][i + 1] = auxVentasModelo
                facturacion_por_venta_dia[dia_elegido ][i + 1] = auxFacturacion

                desordenada = True

# Opción I


def get_total_por_mes(mes):
    print()
    print("Mes ", MESES[mes - 1])
    print()

    print("Total facturado en ",
          MESES[mes - 1], ' $', get_facturacion_mensual())
    print("Ventas realizadas: ", get_ventas_mensuales())
    print("Clientes unicos: ", len(clientes))
    print("Costo de adquisicion productos vendidos: $",
          get_facturacion_mensual() / 2)
    print()

# Opción II


def total_por_producto_y_modelo(producto_indice):
    print()
    print("Producto elegido: ", PRODUCTOS[producto_indice])
    print()

    print("Total facturado: $", get_facturacion())
    print()
    for i in range(len(facturacion[producto_indice])):
        print("Ventas modelo ", i + 1,
              ventas_por_producto[producto_indice][i])
    print()
    print("Clientes únicos: ")
    print("Costo adquisicion productos vendidos: ",
          facturacion[producto_indice][i] / 2)

# Opción III


def get_ventas_mensuales_por_cliente():
    print()
    print("Mes ", mes, " del ", anio)
    print()
    for i in range(len(clientes)):
        print()
        print("--------------------------")
        print("Cliente ", clientes[i])
        print("Artículos comprados: ", ventas_clientes[i])
        print("Total facturado por el cliente: $", facturacion_por_cliente[i])
        print("--------------------------")
        print()

# Opción IV


def detalle_por_dia():
    for i in range(len(ventas_dia)):
        print()
        print("-----------------------------------")
        print(i + 1, "/", mes, "/", anio, ':')
        print("Ventas realizadas: ", ventas_dia[i])
        print("Total facturado del dia: $", facturacion_dia[i])
        print("-----------------------------------")
        print()
    print()

# Opción V


def detalle_del_dia():
    dia_elegido = 0
    while (dia_elegido > 30 or dia_elegido < 1):
        dia_elegido = int(input("Indique el dia que desea consultar: "))


    ordenar_ids_descendente(dia_elegido - 1)

    print()
    print("Día: ", dia_elegido, " de ", MESES[mes - 1], ' del ', anio)
    print()

    for i in range(len(clientes_del_dia[dia_elegido - 1])):
        print("---------------------------")
        print("ID cliente: ", clientes_del_dia[dia_elegido - 1][i])
        print("Tipo de producto: ",
              PRODUCTOS[ventas_producto_dia[dia_elegido - 1][i]])
        print("Modelo: ", ventas_modelo_detalle_dia[dia_elegido - 1][i] + 1)
        print("Total facturado: ",
              facturacion_por_venta_dia[dia_elegido - 1][i])
        print("---------------------------")
        print()
    print("Ventas del dia ", len(clientes_del_dia[dia_elegido - 1]))

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
        print("**************************************************************")
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
    print("Hasta la proxima! ")

# Fin del programa
