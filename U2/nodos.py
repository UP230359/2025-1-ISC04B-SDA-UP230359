class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
                
    def __str__(self):
        return self.dato + "->" + str(self.sig)

    def getData(self):
        return self.dato
    
    def setData(self, dato):
        self.dato = dato
        
nodo1 = Nodo("Chuy")

#print(nodo1.dato)
#print(nodo1.getData())
#print(nodo1.sig)

nodo1.setData("Jesus")
print("nodo1:",nodo1)
#print(nodo1.dato)

nodo2 = Nodo("Maria")
print("nodo2:",nodo2)

nodo1.sig = nodo2
print(nodo1)

nodo3 = Nodo("Jose")
nodo2.sig = nodo3
print("--->")
print(nodo1)
print(nodo2)
print(nodo3)

print(nodo1.sig.sig.dato)
#print(nodo1.sig.sig.sig.dato)

