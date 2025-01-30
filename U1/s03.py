# c:\> pip install numpy
import numpy as np
from datetime import date  # Para manejar fechas
# import Clases as  
from Clases import Persona


counter = -3   # Verdadero si counter es distinto de 0
while counter:
    print("Inside the loop.", counter)
    counter += 1
print("Outside the loop.", counter)

my_list = []  # Creating an empty list.

# Appending elements to the list.
my_list.append(1)

# ------------------------------------------
# Crear una instancia de la clase Persona
persona = Persona("Juan Pérez", 50000, date(1990, 5, 23))
print(persona.mostrar_info())
print(persona)

personas = []
personas.append(Persona("Ana López", 60000, date(1985, 12, 15)))
personas.append(Persona("Pedro Infante", 70000, date(1970, 3, 3)))

print(personas[0].mostrar_info())
print(personas[1].mostrar_info())

# Buscar a una persona por nombre
persona_buscada = next((p for p in personas if p.nombre == "Pedro Infante"), None)
if persona_buscada:
    print("Persona encontrada ->", end=" ")
    print(persona_buscada.mostrar_info())
else:
    print("Persona no encontrada.")

find = "Pedro Infante"
found = False
for i in range(len(personas)):
    found = personas[i].nombre == find
    if found: break
if found:
    print("index: ", i)
else:
    print("absent")  
    
# Obtener el índice de la persona encontrada
indice = next((i for i, p in enumerate(personas) if p.nombre == find), -1)
if indice != -1:
    print(f"Índice de {find}: {indice}")
else:
    print("Persona no encontrada en la lista.")    

