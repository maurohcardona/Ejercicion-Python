class Marino():
    def __init__(self) -> None:
        pass
    
    def hablar(self):
        print("Hola, soy un animal marino!")
        
class Pulpo(Marino):
    def __init__(self) -> None:
        super().__init__()
        
    def hablar(self):
        print("Hola, soy un pulpo!")
        
class Foca(Marino):
    def __init__(self, mensaje) -> None:
        super().__init__()
        self.mensaje = mensaje
        
    def hablar(self):
        print(self.mensaje)
        
foca = Foca("Hola soy una foca!")

foca.hablar()
    