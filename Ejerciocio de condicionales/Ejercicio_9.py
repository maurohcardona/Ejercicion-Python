edad = int(input("Ingrese la edad del cliente "))

if edad < 4:
    print("El cliente no paga entrada")
    
elif 4 <= edad <= 18:
    print("El cliente debe paga una entrada de $5")

else:
    print("El cliente debe pagar una entrada de $10")
    

#Otra solucion

edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")
