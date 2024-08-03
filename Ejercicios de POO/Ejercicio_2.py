class Persona():
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self) -> str:
        return (f"La persona se llama {self.nombre} y tiene {self.edad} años")
    
    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}, ahora tienes {self.edad} años")
        
        
persona1 = Persona("Mauro", 35)

print(persona1)
persona1.cumpleaños()
persona1.cumpleaños()
persona1.cumpleaños()