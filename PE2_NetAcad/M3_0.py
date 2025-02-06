from datetime import date  # Para manejar fechas

class Persona:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha_nacimiento = fecha
    
    def mostrar_datos(self):
        print(f'Nombre: {self.nombre}, Fecha Nacimiento: {self.fecha_nacimiento} ', end='')

class Estudiante(Persona):
    counter = 0
    def __init__(self, nombre, fecha_nacimiento, carrera):
        #super().__init__(nombre, fecha_nacimiento)
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.carrera = carrera
        Estudiante.counter += 1
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Carrera: {self.carrera}')

    def __pareja(self):
        return ("Adivina Adivinanza")        


class Profesor(Persona):
    def __init__(self, nombre, fecha_nacimiento, sueldo):
        super().__init__(nombre, fecha_nacimiento)
        self.sueldo = sueldo

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Sueldo: {self.sueldo}')


class ProfesorTitular(Profesor):
    def __init__(self, nombre, fecha_nacimiento, sueldo, departamento):
        super().__init__(nombre, fecha_nacimiento, sueldo)
        self.departamento = departamento
    
    def mostrar_datos(self):
        super().mostrar_datos()
        print(f'Departamento: {self.departamento}')

    def __str__(self):
        return ("{" + "Nombre:" + self.nombre + ", " 
                    + "fecha:"  + str(self.fecha_nacimiento) + ", "
                    + "sueldo:" + str(self.sueldo) + ", "
                    + "departamento:" + self.departamento 
                    + "}")        


def printBases(cls):    # Indica la clase padre, (Muestra la Herencia)
    print('( ', end='')
    for x in cls.__bases__: # 
        print(x.__name__, end=' ')
    print(')')

# Ejemplo de uso

juanito = Persona('Juan Pérez', date(1980, 5, 25))
print(juanito.nombre)
estudiante = Estudiante('Pepito', date(2005, 5, 23), 'ISC')
estudiante.mostrar_datos()


estudiantes = []
estudiantes.append(Estudiante("Ana López", date(1985, 12, 15), "MTR"))
estudiantes.append(Estudiante("Pedro Infante", date(1970, 3, 3), "ELE"))
print("pedrito: ",estudiantes[1].nombre) # ?? 
estudiantes[1].mostrar_datos() # ?? 

profesor = Profesor('Candido Pérez', date(1980,5, 25) , 123.45)
profesor_titular = ProfesorTitular('Gutierritos', date(1970, 10, 1), 500, 'ISC')

print("Datos del Estudiante:")
estudiante.mostrar_datos()
print("\nDatos del Profesor:")
profesor.mostrar_datos()
print("\nDatos del Profesor Titular:")
profesor_titular.mostrar_datos()
print("---------->")
print(profesor_titular)
print("<----------")
print("Clase: ", type(profesor_titular).__name__)     # type(obj) es la clase a la que pertenece el objet
print("Clase: ", profesor_titular.__class__.__name__)

print("Herencia: ", ProfesorTitular.__bases__) # Indica la clase padre
printBases(ProfesorTitular) # Muestra la Herencia

print("dict: ", profesor_titular.__dict__) 
print("str:  ", profesor_titular)

print("nombre:", profesor_titular.nombre)
print("nombre:", getattr(profesor_titular, 'nombre'))

print("pareja: ", estudiante._Estudiante__pareja()) # método oculto

print("Modulos")
print(ProfesorTitular.__module__)  # __main__ 
print(profesor_titular.__module__) # __main__

texto3=""
texto1= "UPA"
texto2= "UPa"
texto3 += texto1 
print(texto1 is texto3) # is compara si son el mismo objeto
print(texto1 == texto3) # == compara si son iguales los valores

for est in estudiantes:
    print(est.mostrar_datos())
print("Total de Estudiantes: ", Estudiante.counter)
