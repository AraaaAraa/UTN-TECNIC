from modulacion import pedirNumero
from modulacion2 import contarPrimos
from modulacion3 import mostrarResultado

def principal():
    numero = pedirNumero()
    cantPrimos = contarPrimos(numero)
    mostrarResultado(cantPrimos)

principal()
