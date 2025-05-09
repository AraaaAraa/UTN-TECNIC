"""
Cree un programa que permite ingresar el nombre de un producto, el
precio y que calcule el IVA.
"""

nombreDproducto = input("Ingrese el nombre del producto: ")

precio = input("Ingrese el precio del producto: ")

iva = int(precio) * 1.21

print("El producto " + nombreDproducto + " tiene el precio con el iva es " + str(iva))