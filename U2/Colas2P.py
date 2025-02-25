import os

class Nodo:

    def __init__(self,dato):
        self.dato = dato
        self.sig = None
         
    def __str__(self):
        return str(self.dato) + "->" + str(self.sig)
    
class Cola:

    def __init__(self):
        self.primero= None
        self.ultimo= None
        self.size=0

    def vacio(self):
        return True if self.primero == None else False
     
    def queue(self,dato):
        nuevo=Nodo(dato)
        self.size+=1
        if self.vacio():
            self.primero=nuevo
            self.ultimo=nuevo
        else:
            actual=self.ultimo
            if actual.sig==None:
                actual.sig=nuevo
            self.ultimo=nuevo

def main():
    cola=Cola()
    cola.queue("Jesus")
    cola.queue("Maria")
    cola.queue("Jose")
    cola.queue("Santo")
    print(cola.primero)
    print(cola.ultimo)
    print(cola.size)


if __name__ == "__main__":
    os.system ('cls')#limpiar 
    main()
    print("...hecho")
