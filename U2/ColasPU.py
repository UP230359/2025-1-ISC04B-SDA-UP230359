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
        self.ultimo = None
        self.size = 0
        
    def isEmpty(self):
        #return True if self.primero == None else  False          
        return not self.primero
    
    def enqueue(self, valor):
        nuevo = Nodo(valor)
        self.size += 1
        if self.isEmpty():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            pass
    
def main():
    cola = Cola()
    cola.enqueue(5)
    


if __name__ == "__main__":  
    os.system("cls") 
    main()
    print(". . . Hecho")
    os.system("pause")
