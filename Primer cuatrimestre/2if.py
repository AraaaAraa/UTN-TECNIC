''' 
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...

'''

#Modo 1

nota = int( input("Ingrese su nota aqui: "))

if nota >= 6 and nota < 11:
    print (f"Promoción directa, la nota es ... {nota}")
elif nota >= 4 and nota <= 5:
    print (f"Aprobado, la nota es ... {nota}")
elif nota <= 3:
    print (f"Desaprobado, la nota es ... {nota}")
else: 
    print("Ingrese bien su nota porfavor")



#Modo 2

import random
notas = int(random.randint (1, 10))

if notas >= 6 and notas < 11:
    print (f"Promoción directa, la nota es ... {notas}")
elif notas >= 4 and notas <= 5:
    print (f"Aprobado, la nota es ... {notas}")
elif notas <= 3:
    print (f"Desaprobado, la nota es ... {notas}")