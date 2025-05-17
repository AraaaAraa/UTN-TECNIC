""" 8-Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente"""

ingreso = int(input("Ingrese el numero: "))
contador = 1 
acumulador = 1

for fila in range(1, ingreso + 1):  
    for contador in range(1, fila + 1): 
        print(contador, end=" ")
    print()
