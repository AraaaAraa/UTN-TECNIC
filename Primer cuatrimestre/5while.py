'''Mostrar 10 repeticiones de números descendentes desde el 10 al 1.'''

# numero = 10
# while numero >0:
#     numero -= 1
#     print(numero + 1)

'''Mostrar la suma de los números desde el 1 hasta el 10.'''

# numero = 0
# while numero < 10:
#     numero += 1
#     print(numero)

"""Mostrar la suma de los números pares desde el 1 hasta el 10.  """

# numero = 0
# while numero < 10:
#     numero += 2
#     print (numero)

""" 5-Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla. """

# contador = 0
# ingrso=[]

# while contador < 5:
#     ingreso = input("Ingrese 5 numeros al azar: ")
#     elp = print ("ingresaste: " + str(ingreso))
#     contador += 1

# contador = 0
# numeros = []

# while contador < 5:
#     numero = float(input("Ingresa un número: "))
#     numeros.append(numero)
#     contador += 1

# suma = sum(numeros)
# promedio = suma / len(numeros)

# print("La suma de los números es:", suma)
# print("El promedio es:", promedio)


""" 6-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos. """

# num_acumulado = 0
# continuar = "si"
# contador = 0
# while continuar == "si":

#     ingreso = int(input("Ingrese los numeros que desea calcular: "))

#     num_acumulado += ingreso

#     contador += 1

#     continuar = input ("¿Le gustaria continuar ingresando numeros?: ")

# promedio = num_acumulado / contador3
# print (num_acumulado)
# print (promedio)
     


"""7-Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos."""
# num_posi = 0
# num_nega = 1
# cerrar_num = "si" 

# while cerrar_num == "si":
#      num =  int(input ("Ingrese los numeros que usted desee: "))
     
#      if num > 0:
#           num_posi += num 
#      elif num < 0:
#           num_nega *= num
     
#      cerrar_num = input("¿Desea continuar?: ")

# print (num_posi)
# print (num_nega)


""" 8-Ingresar 10 números enteros. Determinar el máximo y el mínimo. """


# acumulador = 1
# num_mayor = -9999
# num_menor = 9999

# while acumulador <= 10 :
#     num = int(input("Ingrese el numero entero: "))
    
#     if num < num_menor:
#         num_menor = num
#     if num > num_mayor:
#         num_mayor = num 
    

#     acumulador += 1

# print (num_mayor)

# print(num_menor)

""" 9-Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos. """

# acumulador = 0
# contador = 0
# respuesta = "si"
# numero = 0

# while respuesta == "si":
#     numero = int(input("Ingresa un mumero: "))
#     acumulador += numero
#     contador += 1

#     print(numero)

#     if contador >= 5:
#         respuesta = input("Queres continuar?: si/no ")
#         if respuesta == "no":
#             break


# print("la suma de los numero es: " , acumulador , "Tu promedio de numeros es: " , acumulador / contador)

'''10-Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.'''

# acumulador = 0
# contador = 0
# respuesta = "si"
# numero = 0

# while respuesta == "si":
#     numero = int(input("Ingresa un mumero: "))
#     acumulador += numero
#     contador += 1

#     print(numero)

#     if contador >= 5 and contador <= 10:
#         respuesta = input("Queres continuar?: si/no ")
#         if respuesta == "no":
#             break


# print("la suma de los numero es: " , acumulador , "Tu promedio de numeros es: " , acumulador / contador)

'''11-Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
A-La suma acumulada de los números negativos.
B-La suma acumulada de los números positivos.
C-La cantidad de números negativos ingresados.
D-El promedio de los números positivos.
E-El número positivo más grande.
F-El porcentaje de números negativos ingresados, respecto del total de ingresos. '''


# basta = "si"
# ingreso = 0
# num_posi = 0
# num_nega = 0
# num_max = -9999
# contador_g = 0
# contador_nega = 0
# contador_posi = 0
# promedio_posi = 0
# promedio_nega = 0

# while basta == "si":
#     ingreso = int(input('Ingrese un numero: '))
#     if ingreso > 0:
#         num_posi += ingreso
#         contador_posi += 1 
#         if ingreso > num_max:
#             num_max = ingreso
#     elif ingreso < 0:
#         num_nega += ingreso
#         contador_nega += 1
#     contador_g += 1

#     basta = input("Desea continuar?: ")

# promedio_posi = num_posi / contador_posi
# promedio_nega = num_nega / contador_nega
# porcentaje_nega = (contador_nega / contador_g) * 100
# print ("La suma de los numeros positivos es: ", num_posi)
# print ("La suma de los numeros negativos es: ", num_nega)
# print("La cantidad de numeros negativos ingresados fueron: ", contador_nega)
# print("El promedio de numeros positivos es: ", promedio_posi)
# print("El promedio de numeros negativos es: ", promedio_nega)
# print("El numero positivo mas grande es: ", num_max)
# print ("El porcentaje de numeros negtivos es: ", porcentaje_nega)



