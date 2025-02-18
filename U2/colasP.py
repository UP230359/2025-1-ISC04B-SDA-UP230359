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
        self.size = 0
        
    def isEmpty(self):
        #return True if self.primero == None else  False          
        return not self.primero

    def encolar(self, valor):
        nuevo = Nodo(valor)
        self.size += 1
        if self.isEmpty():
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.sig:
                actual = actual.sig
            actual.sig = nuevo
            '''            
            while actual:
                if actual.sig == None:
                    actual.sig = nuevo
                    break
                actual = actual.sig
            '''                

    def desencolar(self):
        if self.isEmpty():
            return None
        else:
            valor = self.primero.valor
            self.primero = self.primero.sig
            self.size -= 1
            return valor        

    def len(self):
        contador = 0
        actual = self.primero
        while actual:
            contador += 1
            actual = actual.sig
        return contador

    def get_datos(self):
        lista = []
        actual = self.primero
        while actual:
            lista.append(actual.valor)
            actual = actual.sig
        return lista
    
    def posicion(self, valor):
        contador = 0
        actual = self.primero
        while actual:
            contador += 1
            if actual.valor == valor:
                return contador
            actual = actual.sig
        return None

    def posicion2(self, valor):
        lista = self.get_datos()
        posicion = lista.index(valor)  if valor in lista else -1    
        return posicion

def main():
    cola = Cola()
    print(cola.isEmpty())
    cola.encolar("Jesus")
    cola.encolar("Maria")
    cola.encolar("Jose")
    cola.encolar("Santo")

    print(cola.primero)
    print(cola.get_datos())
    print(cola.len())
    print(cola.size)
    print(cola.posicion("Marias"))
    print(cola.posicion2("Marias"))

if __name__ == "__main__":  
    os.system("cls") 
    main()
    print(". . . Hecho")
    os.system("pause")

    


