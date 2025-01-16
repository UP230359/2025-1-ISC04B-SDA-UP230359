

y=(lambda x:x+3)(4)   # El 4 es el valor de x
print(y)

lista = [4,7,1]
y=list(map(lambda x:x+3,lista))  # lista es el valor de cada x
print("lista: ", y)

y=list(map(lambda x:x+3,lista))  # lista es el valor de cada x
print("lista: ", y)

mayores = list(filter(lambda x: x>2, lista)) 
print("Mayores:" , mayores)

