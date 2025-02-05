import random

class Carta:
    def __init__(self, cara, palo):
        self.cara = cara
        self.palo = palo
'''
    def __str__(self) -> str:
        return str(self.cara) + "-" + self.palo
'''

      
def cartas():
  caras = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
  palos = ["C", "E", "B", "O"];  # Corazones, Espadas, Bastos, Oros 

  ncaras = len(caras)
  npalos = len(palos)
  ncartas = ncaras * npalos

  mazo = {}
  for i in range(ncartas):
      palo = i //  ncaras  # Palo sort
      cara = i %   ncaras  # cara NO sort
      mazo[i]=(caras[cara], palos[palo])
  return mazo

cartas = cartas()
print(cartas)
muestra = 10
aleatorios = random.sample(range(len(cartas)), muestra)
print('Unicos', aleatorios)
# borrar del diccionario las 10 cartas seleccionadas

jugador ={}
for i in aleatorios:
  jugador.update({ i : cartas.pop(i) })
print('Cartas restantes', cartas)
print('Jugador', jugador)


jugadores = []
for j in range(2): # 2 jugadores
  jugador = {}
  
  aleatorios = random.sample(range(len(cartas)), muestra)
  for i in aleatorios:
    jugador.update({ i : cartas.pop(i) })  #~ 
    jugadores[j].append(jugador)

print('Cartas restantes', cartas)
print('Jugadores', jugadores)
