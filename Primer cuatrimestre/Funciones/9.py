""" 9-Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado. """

def potencia(base, expo):
    resultado = base ** expo
    return resultado

base = int(input("Ingrese el numero que desea potenciar: "))
expo = int(input("Ingrese el numero exponente: "))
resultado = potencia(base, expo)

print(resultado)
