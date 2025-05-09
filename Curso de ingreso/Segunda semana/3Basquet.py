"""
Crear un programa que a partir del ingreso de la altura de un
basquetbolista determinar si es pivot o no. Para serlo el mismo deberá
medir más de 1.80 metros
"""

altura = input ("Ingrese su altura en cm porfavor: ")

if 180 <= int(altura):
    print ("Es pivot")
else: 
    print("No es pivot")