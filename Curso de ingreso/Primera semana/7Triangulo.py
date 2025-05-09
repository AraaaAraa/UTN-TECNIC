"""
Cree un programa que pida los lados de un triangulo y calcule la
supercie
"""

base = input("Ingrese su lado del triangulo: ")

altura = input("Ingrese altura del triangulo: ")

superficie = (int(base) * int(altura)) / 2

print("La superficie del triangulo es " + str(superficie))