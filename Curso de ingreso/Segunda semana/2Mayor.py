"""
Crear un programa que pida al usuario un número y pueda calcular si es o
no mayor de edad. Si es mayor de 18 se mostrará el mensaje “MAYOR” caso
contrario “MENOR”.
"""

edadUsusario = input ("Ingrese su edad porfavor: ")

if 18 <= int(edadUsusario):
    print ("Mayor")
else: 
    print("Menor")