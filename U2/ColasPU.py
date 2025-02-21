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
            self.ultimo.sig = nuevo
            self.ultimo = nuevo
                
                        
    def dequeue(self):
        if self.isEmpty():
            return None
        valor = self.primero.valor
        return valor
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.primero.valor
        
    
            
    
def main():
    cola = Cola()
    cola.enqueue(5)
    cola.enqueue(10)
    cola.enqueue(15)
    print("primero: ", cola.primero)
    print("ultimo: ",cola.ultimo)
    print(cola.peek())
    print("---------")
    '''
    print(cola.primero)
    print(cola.ultimo)
    
    print(cola.dequeue())
    print(cola.dequeue())
    print(cola.dequeue())
    print(cola.dequeue())
    print(cola.dequeue())
    
    print(cola.primero)
    print(cola.ultimo)
    '''
    
if __name__ == "__main__":  
    os.system("cls") 
    main()
    os.system("pause")
