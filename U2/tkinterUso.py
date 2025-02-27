import tkinter as tk
import getpass
# https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html

class UI:

    def __init__(self, parent=None):
        self.parent = parent
        self.parent.geometry("800x600")
        self.parent.title("Test Vocacional")
        self.parent.resizable(False, False)

        #self.frame = tk.Frame(self.parent,  bg="#f0f0f0")
        #self.frame.pack(fill='both', expand=True)        
        self.create_widgets()

    def create_widgets(self):
        texto = "Bienvenido " + getpass.getuser() + " al Test Vocacional"
        self.label = tk.Label(self.parent, text=texto, font=("Arial", 20))
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        print(self.label.cget("text")) # obtener el texto del label
        #print(self.label.configure())  # obtener la configuración del label
        self.label.pack(pady=10) # pady: padding en el eje y  (pack, grid, place)
        #self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10) # grid: permite ubicar los widgets en una grilla

        self.campo_texto = tk.Entry(self.parent, font=("Arial", 15))
        self.campo_texto.pack(pady=10)
        self.campo_texto.insert(0, "Ingrese su nombre")  
        print(self.campo_texto.get()) # obtener el texto del campo de texto
        #self.campo_texto.delete(0, tk.END) # borrar el texto del campo de texto
        print(self.campo_texto.index(tk.END)) # obtener la posición del final del texto

        self.button = tk.Button(self.parent, text="Iniciar", font=("Arial", 15), bg="#38EB5C", activebackground="CadetBlue", anchor="center", height=3, width=5 , command=self.iniciar_test) # width: ancho del botón medida en caracteres
        self.button.pack(pady=10) 
        # self.button.invoke() # ejecutar el comando del botón
        
        self.check = tk.Checkbutton(self.parent, text="Probando")
        self.check.pack()

    def iniciar_test(self):
        print(self.campo_texto.get())
        self.label.config(text="Test Iniciado")
        self.button.config(text="Siguiente", command=self.siguiente_pregunta)

    def siguiente_pregunta(self):
        self.label.config(text="Siguiente Pregunta")
        self.button.config(text="follow me", command=self.siguiente_pregunta2)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = UI(root)
    root.mainloop() # iniciar el bucle de eventos
