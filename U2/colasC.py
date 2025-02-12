class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
                
    def __str__(self):
        return self.dato + "->" + str(self.sig)

class Cola:
    def __init__(self):
        self.primero = None
        
    def isEmpty(self):  #estaVacio()
        #return True if self.primero==None else False
        #return True if not self.primero else False
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
    
    def size():
        pass
          
            
cola = Cola()
print(cola.isEmpty())

#cola.encolar("Jesus")
#cola.encolar("Maria")



       
    