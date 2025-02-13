import os

class Nodo:
    def __init__(self, value):
        self.valor = value
        self.sig = None
        
    def __str__(self):
        return str(self.valor) + "->" + str(self.sig)

class Cola:
    def __init__(self):
        self.primero = None
        
    def isEmpty(self):
        #return True if self.primero == None else  False          
        return not self.primero

    def encolar(self, valor):
        nuevo = Nodo(valor)
        if self.isEmpty():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual:
                if actual.sig == None:
                    actual.sig = nuevo
                    break
                actual = actual.sig    
            
    def size(self):
        pass
    

        


cola = Cola()
print(cola.isEmpty())
cola.encolar("Jesus")
cola.encolar("Maria")
cola.encolar("Jose")
cola.encolar("Santo")



