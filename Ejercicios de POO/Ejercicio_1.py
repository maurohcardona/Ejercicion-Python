class Estudiante():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        
    def __str__(self) -> str:
        return(f"El nombre del estudiante es {self.nombre} y tiene una nota de {self.nota}")
    
    def isaprobado(self):
        if self.nota > 6:
            print("El alumno ha aprobado")
        else:
            print("El alumno no ha aprobado")
        

estudiante1 = Estudiante("Mauro", 10)

print(estudiante1)
estudiante1.isaprobado()