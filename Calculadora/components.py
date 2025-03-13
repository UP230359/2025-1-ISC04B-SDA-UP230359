import math
import tkinter
from tkinter import messagebox

class Nodo:
    def __init__(self, value):
        self.valor = value
        self.sig = None
        
    def __str__(self):
        return str(self.valor) + "->" + str(self.sig)
    
class Stack:  # Creamos la clase Stack
    def __init__(self):
        self.items = []

    def is_empty(self):  # Metodo para verificar si la pila esta vacia
        return self.items == []

    def push(self, item):  # Metodo para insertar elementos a la pila
        self.items.insert(0, item)
        # self.items.append(item)

    def pop(self):  # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)
        # return self.items.pop()

    def print_stack(self):  # Metodo para mostrar los elementos de la pila
        print(self.items)

    def peek(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0
    
class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
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
    
class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        self.create_widgets()

    def create_widgets(self):
        tkinter.Label(self.root, text="Valor A:").grid(row=0, column=0)
        self.entry_a = tkinter.Entry(self.root, width=10)
        self.entry_a.grid(row=0, column=1)

        tkinter.Label(self.root, text="Valor B:").grid(row=1, column=0)
        self.entry_b = tkinter.Entry(self.root, width=10)
        self.entry_b.grid(row=1, column=1 )

        self.result_label = tkinter.Label(self.root, text="Resultado: ")
        self.result_label.grid(row=2, column=0)

        buttons = [('+', self.sumar), ('-', self.restar), ('*', self.multiplicar), ('/', self.dividir)]
        for i, (text, command) in enumerate(buttons):
            tkinter.Button(self.root, text=text, command=command, width=5, padx=15, pady=5).grid(row=3, column=i)

    def get_values(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
            return None, None

    def sumar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a + b}")

    def restar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a - b}")

    def multiplicar(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            self.result_label.config(text=f"Resultado: {a * b}")

    def dividir(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            if b != 0:
                self.result_label.config(text=f"Resultado: {a / b}")
            else:
                messagebox.showerror("Error", "No se puede dividir por cero")