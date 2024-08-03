"""
Ejercicio 5: Clase Empleado y Clase Empresa
Crea una clase Empleado con los atributos nombre, puesto y salario.
Añade un método mostrar_informacion que imprima los detalles del empleado.
Crea una clase Empresa con un atributo nombre y un método agregar_empleado que añada un empleado a una lista de empleados.
Añade un método mostrar_empleados en la clase Empresa que imprima los detalles de todos los empleados.
Crea instancias de Empleado y Empresa, y prueba los métodos.
"""

class Empleado():
    def __init__(self, nombre, puesto, salario) -> None:
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        
    def mostrar_informacion(self):
        print(f"El empleado se llama {self.nombre}, trabaja en el area de {self.puesto} y cobra un salario de ${self.salario}")
        
class Empresa():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.empleados = []
        
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        
    def mostrar_empleados(self):
        print("Lista de empleados: ")
        for empleado in self.empleados:
            empleado.mostrar_informacion()
            
            
banco_rio = Empresa("Banco Rio")
empleado1 = Empleado("Mauro Cardona","Bioquimico", 1500)
empleado1.mostrar_informacion()
banco_rio.agregar_empleado(empleado1)
banco_rio.mostrar_empleados()
        