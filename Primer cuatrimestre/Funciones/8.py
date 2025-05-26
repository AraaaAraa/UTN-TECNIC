""" 8-Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande. """


def maxYmin(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        print(numero1, "es el numero mas grande")
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        print(numero2, "es el numero mas alto")
        return numero2
    elif numero3 > numero1 and numero3 > numero2:
        print(numero3, "es el maximo")
        return numero3
