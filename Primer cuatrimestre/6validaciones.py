""" 1- Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados. """

# clave = input("Ingrese su clave: ")

# while clave != "Holamundo":
#     clave = input("La clave es erronea, vuelva a intentarlo a continuacion: ")

# print ("Bienvenido al sistema!")

""" 2- Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos. """

# clave = input("Ingrese su clave: ")
# contador = 1
# mensaje = ""
# while clave != "Holamundo" and contador != 3:
#      print("La clave es erronea. Solo tiene 3 intentos y ustes esta en el numero: ", contador)
#      clave = input("Vuelva a intentarlo a continuacion: ")
#      contador += 1

# if clave == "Holamundo":
#      mensaje = print("Bienvenido al sistema!")
# else:
#     mensaje = print("Ya terminaron sus 3 intentos.")

""" 3- Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive. """

nota = False 

while nota == False:
    nota = int(input("Ingrese la nota: "))

    if nota <= 10 and nota >= 1:
        print ("Su nota es: ", nota)
        nota = True
    else:
        nota = int(input("Error, numero no valido ingrese la nota nuevamente: "))


""" 5- Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla. """


