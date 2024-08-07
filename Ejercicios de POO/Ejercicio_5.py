class Fabrica():
    def __init__(self, llantas, color, precio) -> None:
        self.llantas = llantas
        self.color = color
        self.precio = precio
        
class Moto(Fabrica):
    def __init__(self, llantas, color, precio) -> None:
        super().__init__(llantas, color, precio)
        
    def datos(self):
        print(f"El vehiculo posee {self.llantas} llantas, es de color {self.color} y vale ${self.precio}")
        
        
class Carro(Fabrica):
    def __init__(self, llantas, color, precio) -> None:
        super().__init__(llantas, color, precio)
        
    def datos(self):
        print(f"El vehiculo posee {self.llantas} llantas, es de color {self.color} y vale ${self.precio}")
        
