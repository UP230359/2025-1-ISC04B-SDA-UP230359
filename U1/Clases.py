from datetime import date  # Para manejar fechas

class Persona:
    def __init__(self, nombre, sueldo, fecha_nacimiento):
        self.nombre = nombre
        self.sueldo = sueldo
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info(self):
        return (f"Nombre: {self.nombre}, "
                f"Sueldo: ${self.sueldo}, "
                f"Fecha de Nacimiento: {self.fecha_nacimiento}, "
                f"Mes: { self.fecha_nacimiento.month } ")
        
    def __str__(self):
        return ("{" + "nombre:" + self.nombre + ", " +
                      "sueldo:" + str(self.sueldo) + ", " +
                      "fecha:"  + str(self.fecha_nacimiento) +"}")
