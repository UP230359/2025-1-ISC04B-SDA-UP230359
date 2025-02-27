import os
import tkinter as tk

class TablaApp:
    
    def __init__(self, master):
        self.master = master
        master.title("Tabla de Multiplicar")
        master.geometry("400x300")
        
        self.label = tk.Label(master, text="Ingrese un número:", width=15) # 20 Caracteres
        self.label.grid(row=0, column=0, sticky='w', padx=10)
        
        self.entry = tk.Entry(master, width=5) # 5 Caracteres
        self.entry.grid(row=0, column=1)
        
        self.button = tk.Button(master, text="Mostrar Tabla", command=self.mostrar_tabla)
        self.button.grid(row=0, column=2, padx=20) # 20 pixeles de separación
        
        self.text_area = tk.Text(master,  width=15, height=11)
        self.text_area.grid(row=1, column=1, sticky="w", pady=10) # 10 pixeles de separación
      
        
    def mostrar_tabla(self):
        try:
            numero = int(self.entry.get())
            self.text_area.delete(1.0, tk.END) # 1.0 = fila 1, columna 0. 
            for i in range(1, 11):
                resultado = numero * i
                self.text_area.insert(tk.END, f"{numero} x {i} = {resultado}\n")
        except ValueError:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "Por favor, ingrese un número entero.")    

     
if __name__ == "__main__":
    os.system('cls')    
    root = tk.Tk()
    app = TablaApp(root)
    root.mainloop()    
    print(". . .H e c h o")      
   
