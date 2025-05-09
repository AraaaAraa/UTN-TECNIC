"""
Cree un programa en el cual pida al usuario el nombre y la edad y muestre
por consola la edad que tentra dentro de 10 años
"""

nombre = input("Ingrese su nombre completo: ")

edad = input("Ingrese su edad: ")

futuro = int(edad) + 10

nombreCompleto = ("Su nombre es ") + nombre

nombreEdad = nombreCompleto + " y su edad es " + edad + " la cual en 10 años va a ser " + str(futuro)

print("Hola! " + nombreEdad)