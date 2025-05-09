"""
Cree un programa que calcule el promedio de un alumno, ingresando su
nombre apellido, 3 notas, que muestre al final las leyendas pertinentes
"""

nombreApllido = input("Ingrese su nombre y apellido: ")

primeraNota = input("Primera nota: ")

segundaNota = input("Segunda nota: ")

terceraNota = input("Tercera nota: ")

promedio = (int(primeraNota) + int(segundaNota) + int(terceraNota)) /3

print("El promedio del alumno" + nombreApllido + " es " + str(promedio))