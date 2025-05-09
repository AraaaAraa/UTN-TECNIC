"""
Cree un programa que pida el nombre, número de comisión, asignatura,
docente y si el usuario estuvo presente, luego que muestre los datos por
consola con las leyendas pertinentes
"""

nombre = input("Ingrese su nombre: ")

apellido = input("Ingrese su apellido: ")

numeroDcomision = input("Ingrese su numero de comision: ")

clase = input("Su clase es: ")

profe = input("Su profesor es: ")

presente = input("¿Estuvo presente o ausente? ")

nombreCompleto = ("Su nombre es ") + nombre + " " + apellido

nombreEdad = nombreCompleto + ", su numero de comision es " + numeroDcomision

datosClase = nombreEdad + ", su clase es " + clase + " con el profesor " + profe + " en la que estuvo " + presente

print("Hola! " + datosClase)