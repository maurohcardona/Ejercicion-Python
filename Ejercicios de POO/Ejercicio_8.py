class CuentaBancaria():
    def __init__(self, numero_cuenta, saldo, titular) -> None:
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        self.titular = titular
        
    def depositar(self, monto):
        self.saldo += monto
        print(f"Ha depositado ${monto}, su saldo actual es de ${self.saldo}")
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Ha retirado ${monto}, su saldo actual es de ${self.saldo}")
        else:
            print(f"Su saldo es insuficiente para realizar la extraccion, su saldo es de ${self.saldo}")
            
    def mostrar_saldo(self):
        print(f"Su saldo actual es de ${self.saldo}")
        

class Banco():
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.cuentas = []
        
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print(f"se ha agregado la cuenta  de {cuenta.titular}")
        
    def mostar_cuentas(self):
        if len(self.cuentas) > 0:
            for cuenta in self.cuentas:
                print(f"Cuenta numero: {cuenta.numero_cuenta}, saldo: ${cuenta.saldo}, titular: {cuenta.titular}")
        else:
            print("El banco no posee cuentas aun")
        
banco = Banco("Banco provincia")

cuenta_mauro = CuentaBancaria(1, 0, "Mauro Cardona")
cuenta_juan = CuentaBancaria(2, 200 , "Juan Cardona")

banco.mostar_cuentas()
banco.agregar_cuenta(cuenta_mauro)
cuenta_mauro.depositar(100)
cuenta_mauro.retirar(50)
cuenta_mauro.mostrar_saldo()
banco.mostar_cuentas()
banco.agregar_cuenta(cuenta_juan)
banco.mostar_cuentas()