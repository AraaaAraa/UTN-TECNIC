''' Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
Si es invierno: solo se viaja a Bariloche.
Si es verano: se viaja a Mar del plata y Cataratas.
Si es otoño: se viaja a todos los lugares.
Si es primavera: se viaja a todos los lugares menos Bariloche. '''

estacion = input("Ingrese estacion en la quiere viajar: ")
lugar = input("Ingrese el lugar a donde quiere viajar: ")

if estacion == "invierno":
    match lugar:
        case "bariloche":
            print ("Se viaja")
        case _ :
            print ("No se viaja")
elif estacion == "verano":
    match lugar:
        case "mar del plata":
            print ("Se viaja")
        case "cataratas":
            print("Se viaja")
        case _ :
            print("No se viaja")
elif estacion == "otoño":
    print ("Se viaja")
elif estacion == "primavera":
    match lugar:
        case "bariloche":
            print ("No se viaja")
        case _:
            print ("Se viaja")
else:
    print("Escriba bien porfavor")