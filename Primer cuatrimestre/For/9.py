""" 9- Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados. """

ingreso = int(input("Ingrese el número: "))
contador = 0 
for num in range(1, ingreso + 1):
    if ingreso % num == 0:
        print(num)
        contador += 1

print("Cantidad de divisores encontrados:", contador)
