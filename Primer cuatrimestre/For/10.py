""" 10- Ingresar un número. Determinar si el número es primo o no."""

ingreso = int(input("Ingrese el número: "))
esPrimo = True

for i in range(2, ingreso):
    if ingreso % i == 0:
        esPrimo = False

if ingreso > 1 and esPrimo:
    print("Es primo")
else:
    print("No es primo")
