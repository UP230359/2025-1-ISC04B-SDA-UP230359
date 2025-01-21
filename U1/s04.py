import cmath
# None = Null

a = 5
b = 0
# [código si se cumple] if [condición] else [código si no se cumple]
r = a/b if b!=0 else -1

y=(lambda x:x+3)(4)   # El 4 es el valor de x
print(y)

lista = [15, 4, 9,11]
y=list(map(lambda x:x+3,lista))  # lista es el valor de cada x
print("lista: ", y)

divisibles=[]
for x in lista:
  if x%3 == 0:
      divisibles.append(x)
print("Divisibles entre 3:" , divisibles)

divisibles = list(filter(lambda x: x%3==0, lista)) 
print("Divisibles entre 3:" , divisibles)



import math

def resolver_ecuacion_cuadratica_una_linea(a, b, c):
    return ((-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)) if b**2 - 4*a*c >= 0 else \
           ((-b / (2*a) + math.sqrt(-b**2 + 4*a*c) / (2*a) * 1j), (-b / (2*a) - math.sqrt(-b**2 + 4*a*c) / (2*a) * 1j))

def resolver_ecuacion_cuadratica(a, b, c):  # regresa una tupla con las dos soluciones
    return ((-b + cmath.sqrt(b**2 - 4*a*c)) / (2*a), 
            (-b - cmath.sqrt(b**2 - 4*a*c)) / (2*a))

# Ejemplo de uso
a, b, c = 1, -3, 2  # Cambia los valores de a, b, c según tu necesidad
print(resolver_ecuacion_cuadratica(a, b, c))
print(resolver_ecuacion_cuadratica_una_linea(a, b, c))

def contador(n):
    if n == 0:
        print("BOOM!")
    else:
        print(n)
        contador(n-1) 

contador(5) 

def factorial_R(n):
    if n == 1:
        return 1
    return n * factorial_R(n-1)

r= factorial_R(4)
