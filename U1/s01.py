print("Hola Mundo")
a = 2
b = 3
print("Multiplicar ", a, " x ", b, " = ", a*b, "{}")
print("Multiplicar " + str(a) + " x " + str(b) + " = " + str(a*b))
print('Multiplicar {} x {} = {} '.format(a,b,a*b))
print(f'Multiplicar {a} x {b} = {a*b} ')

a= "UPA"
a = "UNI"

lista = [11,22,33,44,55]
lista.append(66)
lista[2]= 99
lista.pop(2)
del lista[2]
print(lista[1:3])
print(lista)
lista.insert(20,100)
print(lista)

print("--------")

tupla = (11,22,33,44,55, "hola")
# tupla[2]= 99 # Error
print(tupla[1:3])




sepa = set([4.0, 'Cadena', True])
print(sepa)
sepa.add(5.0)
sepa.add('Cadena2')
sepa.add('Cadena')
print(sepa)

diccionario = {'key1': 1.0, 'key2': False, "matricula": '2019-1234'}
print(diccionario)
print(diccionario['matricula'])
