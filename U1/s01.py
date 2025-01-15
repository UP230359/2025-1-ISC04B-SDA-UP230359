
def doble(x):
    return x * 2

print("Hola Mundo")

# Tabla de multiplicar de un numero
# numero = 5
numero = int(input("Tabla del número: "))
if numero < 1 or numero > 10:
    print("Número fuera de rango")
    exit()

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
print()    
    
print("El doble de", numero, "es", doble(numero))
print("El doble de " + str(numero) + " es " + str(doble(numero)))
print(f'El doble de {numero} es {doble(numero)}')
print('El doble de {} es {} '.format(numero,doble(numero)))

