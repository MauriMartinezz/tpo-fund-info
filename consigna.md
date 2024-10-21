

Todos los meses, tienen que generar el resumen de la facturación de todas las ventas del mes, para ello cuentan con la siguiente información de precio de venta por unidad de los productos:


PDV --> Precio de Venta

  Sillas:
   PDV Modelo 1: 55.000
   PDV Modelo 2: 62.000
   PDV Modelo 3: 68.000
   PDV Modelo 4: 70.000
 Mesas:
   PDV Modelo 1: 145.000
   PDV Modelo 2: 160.000
   PDV Modelo 3: 180.000
   PDV Modelo 4: 200.000
 Sillones:
   PDV Modelo 1: 200.000
   PDV Modelo 2: 300.000
   PDV Modelo 3: 400.000
   PDV Modelo 4: 450.000
 Racks TV:
   PDV Modelo 1: 158.000
   PDV Modelo 2: 165.000
   PDV Modelo 3: 170.000
   PDV Modelo 4: 200.000
 Camas:
   PDV Modelo 1: 50.000
   PDV Modelo 2: 70.000
   PDV Modelo 3: 85.000
   PDV Modelo 4: 110.000
 
 La empresa cuenta con el detalle de todas las ventas del mes realizado por sus clientes

 ** Se deberá solicitar al usuario **
   - Qué mes de qué año desea consultar la información
      - Este es el dato de entrada que permite luego generar la tabla de datos

 Tabla ejemplo de datos a generar
   Los datos pertenecen al mismo mes del mismo año

 Fecha
   1/8/24
       ID Cliente (4 digitos)
           3245
       Tipo producto
           SILLAS
       Modelo Vendido
           Modelo 2
   1/8/24
       ID Cliente 
           4700
       Tipo producto
           Mesas
       Modelo Vendido
           Modelo 1
   5/8/24
       ID Cliente
           1000
       Tipo producto
           Sillones
       Modelo Vendido
           Modelo 4
 

 ****** ACLARACIONES *******
 
   - Puede haber hasta 200 ventas por día 
       - Garantizar que existan al menos 20 ventas por día
   - Un mismo cliente puede comprar más de un artículo por día
   - El ID de cliente es un número de 4 dígitos, que va de 1000 a 9999
   - La fecha de la venta debe corresponder al mismo mes
       - Toda la tabla debe ser construida validando las fechas en forma correcta
   - Los datos serán generados por números al azar
   - El mes y el año serán leídos por teclado
       - A partir de esto se generan las fechas con sus datos
   - Costo de adquisición:
       
 

 ****** OBJETIVOS ********

 ## Totales mes (Opción 1)
 Mes: Agosto 2024 
 
  Total facturado: $xxxxx
  Total ventas realizados: xxxxx
  Total clientes únicos: xxxxx
  Total costo adquisición productos vendidos: $xxxxx

 ## Total por tipo de producto y Modelo (Opción 2) 
  Producto seleccionado: SILLONES
  
  Total facturado: $xxxxx
    Total ventas modelo 1: xxxxx
    Total ventas modelo 2: xxxxx
    Total ventas modelo 3: xxxxx
    Total ventas modelo 3: xxxxx
    Total ventas modelo 4: xxxxx
  Total clientes únicos: xxxxx
  Total costo adquisición productos vendidos: $xxxxx

 ## Detalle por clientes (Opción 3)
 Mes: Agosto 2024

   ID Cliente
       1000
   Total artículos comprados
       3
   Total facturado por cliente
       150.000

   ID Cliente
       1002
   Total artículos comprados
       4
   Total facturado por cliente
       350.000
 

 ## Detalle por día Opción 4

 Mes: Agosto 2024

   Día
       1/8/24
   Total ventas realizadas
       150
   Total facturado del día
       590.000
   Día 
       2/8/24
   Total ventas realizadas
       600
   Total facturado del día
       590.000


 ## Detalle del día: Opción 5

 Día: 18 de agosto 2024

   ID Cliente
       1000
   Tipo de producto
       SILLAS
   Modelo
       Modelo 4
   Total facturado
       150.000

   ID Cliente
       3390
   Tipo de producto
       Sillones
   Modelo
       Modelo 4
   Total facturado
       130.000

