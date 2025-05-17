""" 4- Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5: """

ingreso = int(input("Ingrese el numero que desee: "))
contador = 0

for contador in range (1, 11):
    print( contador ,"x", ingreso, "=", ingreso * contador )
    contador + 1
