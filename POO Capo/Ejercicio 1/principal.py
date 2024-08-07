from ejercicio_1 import Cliente, Cuenta, Movimiento

cliente_1 = Cliente(34922207, "Antonio", "Martinez")
cuenta_1 = Cuenta(cliente_1.apellido, 0)
cuenta_2 = Cuenta(cliente_1.apellido, 50)
movimiento_1 = Movimiento("Haberes", 500)
movimiento_2 = Movimiento("Aguinaldo", 100)
movimiento_3 = Movimiento("Alquiler", -20)
movimiento_4 = Movimiento("Regalias", 500)
movimiento_5 = Movimiento("Expensas", -50)
movimiento_6 = Movimiento("Compras", -100)

cliente_1.agregar_cuenta(cuenta_1)
cliente_1.agregar_cuenta(cuenta_2)
cuenta_1.añadir_movimiento(movimiento_1)
cuenta_1.añadir_movimiento(movimiento_2)
cuenta_1.añadir_movimiento(movimiento_3)
cuenta_2.añadir_movimiento(movimiento_4)
cuenta_2.añadir_movimiento(movimiento_5)
cuenta_2.añadir_movimiento(movimiento_6)

cliente_1.mostrar_cuentas()


