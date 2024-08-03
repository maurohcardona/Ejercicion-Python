producto = input("Ingrese el nombre del producto ")
precio = float(input("Ingrese el precio del producto "))
unidades = int(input("Ingrese las unidades del producto "))

costo_total = unidades * precio


print(f"Usted ha adquirido {unidades:03} unidades del producto {producto}, con un precio de unitario de ${precio:09.2f} y un costo final de ${costo_total:11.2f}")