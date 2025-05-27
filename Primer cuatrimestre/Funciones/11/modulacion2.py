""" 11-Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible. """

def esPrimo(n):
    divisores = 0
    for k in range(1, n + 1):
        if n % k == 0:
            divisores += 1
    return divisores == 2

def contarPrimos(hasta):
    cantPrimos = 0
    for i in range(1, hasta + 1):
        if esPrimo(i):
            print(i, "Este número es primo")
            cantPrimos += 1
    return cantPrimos
