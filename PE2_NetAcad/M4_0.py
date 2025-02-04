# Listas por comprension
the_list      = [1 if x % 2 == 0 else 0 for x in range(10)]   # Los corchetes  hacen una comprension
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))   # Los parentesis hacen un  generador
print(the_list)
print(the_generator)
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))

print(list(the_generator))

def contar_hasta(n):
    contador = 1
    while contador <= n:
        yield contador  # Devuelve el valor y pausa la ejecución
        contador += 1

# Uso del generador
for numero in contar_hasta(5):
    print(numero)

def pares():
    n = 0
    while True:
        yield n
        n += 2
print("Generador de pares:")
gen = pares()
print(next(gen))  # 0
print(next(gen))  # 2
print(next(gen))  # 4
