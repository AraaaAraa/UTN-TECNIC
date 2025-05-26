"""4-Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área."""

def triangulo (base, altura):
    calculo = base * altura
    print (calculo)

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

triangulo(base, altura)
