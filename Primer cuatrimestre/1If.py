''' A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar
 la posición del jugador en la cancha, considerando los siguientes parámetros:
Menos de 160 cm: Base
Entre 160 cm y 179 cm: Escolta
Entre 180 cm y 199 cm: Alero
200 cm o más: Ala-Pívot o Pívot
'''

alturas = int(input ("Ingrese su altura en centimetros: "))

if alturas < 160:
    print (f"Usted como mide {alturas} es un jugador Base")
elif alturas >= 160 and alturas <= 179 :
    print(f"Usted como mide {alturas} es un jugador Escolta")
elif alturas >= 180 and alturas <= 199 :
    print(f"Usted como mide {alturas} es un jugador Alero")
else:
    print (f"Usted como mide {alturas} es un jugador Ala-Pívot o Pivot") 
