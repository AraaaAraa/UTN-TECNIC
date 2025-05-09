"""
Crear un programa que se ingrese la edad del usuario en número y pueda
calcular si es adolescente (edad entre 13 y 17 años).
"""

edadUsusario = input ("Ingrese su edad porfavor: ")

if 13 <= int(edadUsusario) and 17 >= int(edadUsusario):
    print ("Eres un adolecente")
else: 
    print("No eres un adolecente")
