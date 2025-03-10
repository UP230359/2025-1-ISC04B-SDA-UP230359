# Functions
# Remember - Python reads your code from top to bottom

# There are at least four basic types of functions in Python:
# built-in functions    : print()  https://docs.python.org/3/library/functions.html
# pre-installed modules : import 
# user-defined functions: def
# the lambda functions  : lambda   

import numpy as np

def isPar(x):
    if x % 2 == 0:
        return True
    else:
        return False
print(isPar(50))

y=(lambda x:x+3)(4)   # El 4 es el valor de x
print(y)

lista = [4,7,1]
ordenada = sorted(lista)
print(ordenada)

y=[]
for i in range(0, len(lista)):
    y.append(lista[i] + 3)
print("lista: ", y)
 

y=list(map(lambda x:x+3,lista))  # lista es el valor de cada x
print("lista: ", y)

mayores = list(filter(lambda x: x>2, lista)) 
print("Mayores:" , mayores)

# Operador Ternario
# [código si se cumple] if [condición] else [código si no se cumple]

a = 10
b = 0
c = a/b if b!=0 else -1
print(c)



