""" 3-Ingresar un número. Mostrar los números desde 0 hasta el número ingresado. """

 ingreso = int(input("Ingrese un numero: "))

 for ingreso in range(-1, ingreso, 1):
     print(ingreso + 1)
