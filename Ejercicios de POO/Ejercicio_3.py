class Calculadora():
    def __init__(self, valor1, valor2) -> None:
        self.valor1 = valor1
        self.valor2 = valor2
        
    def suma(self):
        print(f"El resultado de {self.valor1} + {self.valor2} es = {self.valor1 + self.valor2}")
        
    def resta(self):
        print(f"El resultado de {self.valor1} - {self.valor2} es = {self.valor1 - self.valor2}")
        
    def multiplicacion(self):
        print(f"El resultado de {self.valor1} x {self.valor2} es = {self.valor1 * self.valor2}")
        
    def division(self):
        print(f"El resultado de {self.valor1} / {self.valor2} es = {self.valor1 / self.valor2}")
        
cal1 = Calculadora(10,5)

cal1.suma()
cal1.resta()
cal1.multiplicacion()
cal1.division()