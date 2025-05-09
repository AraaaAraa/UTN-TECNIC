"""
Crear un programa que al ingresar un número puede calcular si es mayor,
niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
adolescente (edad entre 13 y 17 años) de edad.
"""

edadUsusario = input ("Ingrese su edad porfavor: ")

if 13 <= int(edadUsusario) and 17 >= int(edadUsusario):
    print ("Eres un adolecente")
elif 10 > int(edadUsusario):
    print("Eres un niño/a")
elif 10 <= int(edadUsusario) and 13 > int(edadUsusario):
    print("Eres un pre-adolecente")
elif 18<= int(edadUsusario):
    print("Eres mayor de edad")

