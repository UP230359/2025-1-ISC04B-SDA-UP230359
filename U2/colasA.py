class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
              
    def __str__(self):
        return self.dato + "->" + str(self.sig)

class Cola:
    
    def __init__(self):
        self.primero = None
        
    def isEmpty(self): # estaVacio
        return True if self.primero == None else False
        return self.primero == None
        return not self.primero
        
            
    def encolar(self, dato):
        nuevo = Nodo(dato)
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
        return 0
    
    
    
cola = Cola()
cola.encolar("Jesus")
cola.encolar("Maria")
cola.encolar("Jose")
print(cola.primero)





    