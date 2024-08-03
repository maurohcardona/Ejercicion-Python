class Persona():
    def __init__(self,nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        print(f"La persona se llama {self.nombre} {self.apellido}")
        
        
class Estudiante(Persona):
    def __init__(self, nombre, apellido, carrera) -> None:
        super().__init__(nombre, apellido)
        self.carrera = carrera
        
    def mostrar_carrera(self):
        print(f"La carrera de {self.nombre} es {self.carrera}")
        
estudiante1 = Estudiante("Mauro", "Cardona", "Bioquimico")
estudiante1.nombre_completo()
estudiante1.mostrar_carrera()