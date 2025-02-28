import tkinter as tk
import getpass
# https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html

class UI:
    def __init__(self, parent=None):
        self.parent = parent
        self.parent.geometry("800x600")
        self.parent.title("Test Vocacional")
        self.parent.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        texto = "Bienvenido " + getpass.getuser() + " a SDA"
        self.label = tk.Label(self.parent, text=texto, font=("Arial", 20))
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.label.pack(pady=10) #  (pack, grid, place)

        self.campo_texto = tk.Entry(self.parent, font=("Arial", 15))
        self.campo_texto.pack(pady=10)
        self.campo_texto.insert(0, "Ingrese su nombre")  
        #self.campo_texto.delete(0, tk.END) # borrar el texto del campo de texto
        #print(self.campo_texto.index(tk.END)) # obtener la posición del final del texto

        self.button = tk.Button(self.parent, text="Iniciar", font=("Arial", 15), bg="#38EB5C", activebackground="CadetBlue", anchor="center", height=3, width=15 , command=self.iniciar_test)
        self.button.pack(pady=10) 
        # self.button.invoke() # ejecutar el comando del botón

    def iniciar_test(self):
        texto = self.campo_texto.get()
        if texto == "":
            texto = "Anónimo"
        self.label.config(text="Bienvenido " + texto)
        self.button.config(text="Siguiente", command=self.siguiente_pregunta)

    def siguiente_pregunta(self):
        self.label.config(text="Eso es todo ....")
        self.button.config(text="follow me", command=self.siguiente_pregunta2)
        
    def siguiente_pregunta2(self):
        quit()        

if __name__ == "__main__":
    root = tk.Tk()
    app = UI(root)
    root.mainloop() # iniciar el bucle de eventos
