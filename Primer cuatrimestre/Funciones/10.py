""" 10-Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario. """


def primo(numero):
    esPrimo = True
    for i in range(2, numero):
        if numero % i == 0:
            esPrimo = False
    if numero > 1 and esPrimo == True:
        return esPrimo
    else:
        return esPrimo



numero = int(input("Ingrese el numero: "))
esPrimo = primo(numero)

print (esPrimo)
