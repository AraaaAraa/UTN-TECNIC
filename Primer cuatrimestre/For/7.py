""" 7-Mostrar los números pares que hay desde la unidad hasta el número 50. """

ingreso = int(input("Ingrese el numero deseado: "))

for ingreso in range(ingreso, 51):
    if ingreso % 2 == 0:
        print(ingreso)
