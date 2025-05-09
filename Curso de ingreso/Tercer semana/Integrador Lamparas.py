"""
1) En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán
pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan
$800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez)
se aplicará el siguiente descuento:
● Si compra 6 o más lámparas bajo consumo tiene un descuento del 50%.
● Si compra 5 lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si
es de otra marca el descuento es del 30%.
● Si compra 4 lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un
descuento del 25 % y si es de otra marca el descuento es del 20%.
● Si compra 3 lámparas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es
“FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
Por otro lado, si el importe final con descuento suma más de $4000 se obtiene un descuento adicional
de 5%.
Mostrar por pantalla:
Marca, cantidad de lámparas, total a pagar sin descuento, el importe del descuento obtenido si
corresponde, y el total a pagar con descuento.

"""

#Todas las lamparas estan 800

#Solo una marca por vez

#Implementar un sistema que permita a los usuarios saber cuánto deberán
#pagar por la compra de lámparas de bajo consumo

#Marca, cantidad de lámparas, total a pagar sin descuento, el importe del descuento obtenido si
#corresponde, y el total a pagar con descuento.

#Marcas:ArgentinaLuz, FelipeLamparas, otras


#Las variables de ingreso de datos
lampara = input("Introduzca la marca de la lampara: ")

cantidad = input("Introduzca la cantidad de lamparas: ")

#Cuenta principal

cuentacantidad = int(cantidad) * 800

#Cuentas porcentajes

cuenta55 = int(cuentacantidad) * 0.55

cuenta50 = int(cuentacantidad) * 0.5

cuenta40 = int(cuentacantidad) * 0.4

cuenta30 = int(cuentacantidad) * 0.3

cuenta25 = int(cuentacantidad) * 0.25

cuenta20 = int(cuentacantidad) * 0.2

cuenta15 = int(cuentacantidad) * 0.15

cuenta10 = int(cuentacantidad) * 0.1

cuenta5 = int(cuentacantidad) * 0.05

#Codigo de mensaje general

mensaje = "Marca: " + lampara + " Cantidad de lamparas: " + cantidad + " El precio en total: " + str(cuentacantidad)

#Especificaciones de marcas

marcArg = lampara == "ArgentinaLuz"

marcFel = lampara == "FelipeLamparas"

#Print

if int(cantidad) >= 6 and 4000 <= int(cuenta50):
    print( mensaje + " El descuento es de: 50% " + "Precio final: " + str(cuenta50) )
elif int(cantidad) == 5 and marcArg :
    print( mensaje + " El descuento es de: 40% " + "Precio final: " + str(cuenta40) )
elif int(cantidad) == 5 and not marcArg :
    print( mensaje + " El descuento es de: 30% " + "Precio final: " + str(cuenta30) )
elif int(cantidad) == 4 and marcArg or marcFel:
    print( mensaje + " El descuento es de: 25% " + "Precio final: " + str(cuenta25) )
elif int(cantidad) == 4 and not marcArg or marcFel :
    print( mensaje + " El descuento es de: 20% " + "Precio final: " + str(cuenta20) )
elif int(cantidad) == 3 and marcArg :
    print( mensaje + " El descuento es de: 15% " + "Precio final: " + str(cuenta15) )
elif int(cantidad) == 3 and marcFel :
    print( mensaje + " El descuento es de: 10% " + "Precio final: " + str(cuenta10) )
elif int(cantidad) == 3 and not marcArg or marcFel :
    print( mensaje + " El descuento es de: 5% " + "Precio final: " + str(cuenta5) )
elif int(cuenta50) >= 4000:
    print( mensaje + " El descuento es de: 55% " + "Precio final: " + str(cuenta55) )



