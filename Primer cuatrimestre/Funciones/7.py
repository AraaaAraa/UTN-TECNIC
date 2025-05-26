""" 7-Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario. """

def seleccion(numero):
    bandera = True
    parOimpar = numero % 2
    if parOimpar == 0:
        print("Es par")
        bandera = True
    else:
        print("Es impar")
        bandera = False
    
    return bandera


numero = int(input("Ingrese el numero: "))

seleccion(numero)
