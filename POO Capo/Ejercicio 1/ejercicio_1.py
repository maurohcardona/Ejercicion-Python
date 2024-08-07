class Cliente():
    def __init__(self, dni, nombre, apellido) -> None:
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
    
    def mostrar_cuentas(self):
        if len(self.cuentas) > 0:
            print("Lista de cuentas")
            for cuenta in self.cuentas:
                print(f"Cuenta N°{cuenta.numero}, Saldo: ${cuenta.saldo}")
        else:
            print("No hay cuentas asociadas a este cliente")


class Movimiento():
    def __init__(self, concepto, cantidad) -> None:
        self.concepto = concepto
        self.cantidad = cantidad
        
        
class Cuenta():
    numero_cuenta = 0
    
    def __init__(self, titular, saldo) -> None:
        Cuenta.numero_cuenta += 1 
        self.numero = Cuenta.numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []
        
    def añadir_movimiento(self, movimiento):
        self.movimientos.append(movimiento)
        self.saldo += movimiento.cantidad
        
    def mostrar_saldo(self):
        print(f"El saldo de la cuenta numero {self.numero} es de ${self.saldo}")
        
    