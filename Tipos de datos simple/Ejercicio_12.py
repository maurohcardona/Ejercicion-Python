pan_viejo_vendido = int(input("Intoduce el numero de barras de pan viejo vendidas "))

descuento_pan_viejo = 60

costo_pan_nuevo = 3.49

costo_final = ((costo_pan_nuevo * descuento_pan_viejo)/100)*pan_viejo_vendido

print(f"El costo total del pan viejo vendido es de ${costo_final:.2f}")