ingreso = int(input("Ingrese el número: "))
contadorPrimos = 0


for i in range(1, ingreso + 1):
    divisores = 0
    for k in range(1, i + 1):
        if i % k == 0:
            divisores += 1
    if divisores == 2:
        contadorPrimos += 1
        print(i, "Este numero es primo")

print("La cantidad de numeros primos que hay son: ", contadorPrimos)
