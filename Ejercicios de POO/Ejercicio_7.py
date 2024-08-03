"""
Ejercicio 3: Clase Banco y CuentaBancaria
Crea una clase CuentaBancaria con los atributos numero_cuenta, saldo y titular.
Añade métodos para depositar, retirar y mostrar_saldo.
rea una clase Banco con un atributo nombre y un método agregar_cuenta que añada una cuenta a una lista de cuentas.
Añade un método mostrar_cuentas en la clase Banco que imprima los detalles de todas las cuentas.
Crea instancias de CuentaBancaria y Banco, y prueba los métodos.
    
"""




class Universidad():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
        
class Carrera(Universidad):
    def __init__(self, nombre, especialidad) -> None:
        super().__init__(nombre)
        self.especialidad = especialidad
        
class Estudiante(Carrera):
    def __init__(self, nombre, especialidad, nombre_alumno, edad) -> None:
        super().__init__(nombre, especialidad)
        self.nombre_alumno = nombre_alumno
        self.edad = edad
        
    def __str__(self) -> str:
        return (f"El alumno se llama {self.nombre_alumno}, tiene {self.edad} años, estudia {self.especialidad} en la universidad {self.nombre}")
    
        
persona = Estudiante("UBA", "Bioquimica", "Mauro Cardona", 35)

print(persona)