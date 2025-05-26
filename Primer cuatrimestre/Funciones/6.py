""" 6-Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar. """

def seleccion(numero):
    parOimpar = numero % 2
    if parOimpar == 0:
        print("Es par")
    else:
        print("Es impar")

numero =  int(input("Ingrese un numero: "))

seleccion(numero)
