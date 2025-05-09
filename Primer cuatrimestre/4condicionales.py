""" El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.
Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.
A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

Tarifa base:

Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
El costo por metro cúbico (m³) de agua es de $200/m³.

Bonificaciones y Recargos según tipo de cliente:
Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
Casos especiales:
Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
En todos los casos, se aplica el IVA del 21% sobre el total.

Requerimientos del programa:
1-Solicitar al usuario:
Cantidad de metros consumidos
Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
2-Calcular:
Subtotal de consumo.
Bonificaciones, si corresponde
Recargos, si corresponde
Subtotal, con recargos y bonificaciones.
IVA aplicado (21%), si corresponde.
Total final a pagar.
3-Mostrar en pantalla el desglose de los cálculos
"""

#Entrada

mCubicos = int(input ("Ingrese los metros cubicos consumidos en el mes: "))
tipoCliente = input ("Ingrese si usted es residencial, comercial o industrial: ").lower()

#Variables base

cargoFijo = 7000

costoCubicos = mCubicos * 200

subConsumo = cargoFijo + costoCubicos

num = 0

mensaje = ""

#Mensajes 1

mensubsin = "El subtotal es: " + str(costoCubicos)

mensubcon = "El subtotal con el cargo fijo de 7000 es: " + str(subConsumo)

mencli = "El tipo de cliente es: " + str(tipoCliente)

mencub = "Los metros cubicos gastados son: " + str(mCubicos)



#Proceso

match tipoCliente:
    case "residencial":
        if mCubicos < 30:
            num = costoCubicos * 0.10
            mensaje = ("Tiene un descuento del 10%")
        elif mCubicos > 80:
             num = costoCubicos + (costoCubicos * 0.15)
             mensaje = ("Tiene un recargo del 15%")
    case "comercial":
        if mCubicos > 300:
             num = costoCubicos * 0.12
             mensaje = ("Tiene un descuento del 12%")
        elif mCubicos < 150:
             num = costoCubicos * 0.08
             mensaje = ("Tiene un descuento del 8%")
        elif mCubicos > 50:
             num = costoCubicos + (costoCubicos * 0.05)
             mensaje = ("Tiene un recargo del 5%")
    case "industrial":
        if mCubicos < 500:
             num = costoCubicos * 0.20
             mensaje = ("Tiene un descuento del 20%")
        elif mCubicos < 1000:
             num = costoCubicos * 0.30
             mensaje = ("Tiene un descuento del 30%")
        elif mCubicos > 50:
             num = costoCubicos + (costoCubicos * 0.10)
             mensaje = ("Tiene un recargo del 10%")

if subConsumo > 35000 and tipoCliente == "residencial":
             num = subConsumo * 0.05
             mensaje = ("Tiene un descuento del 5%")

iva = num + (num * 0.21)


#Mensaes 2

mensubon = "El subtotal con bonificaciones y recargos es: " + str(num)

meniva = "El total con el iva es: " + str(iva)

mentot = "El total a pagar es: " + str(iva)

#Salida

print ( mencli )

print ( mencub )

print ( mensubsin )

print ( mensubcon )

print ( mensaje )

print ( mensubon )

print ( meniva )

print ( "El total a pagar es: ", iva + subConsumo )



