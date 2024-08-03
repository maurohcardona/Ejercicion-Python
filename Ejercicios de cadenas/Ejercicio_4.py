"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número 
de teléfono sin el prefijo y la extensión."""

telefono_cpmpleto = input("Ingrese el numero de telefono completo ")

print('El número de teléfono es ', telefono_cpmpleto[4:-3])

telefono_dividivo = telefono_cpmpleto.split("-")

print(f"El numero de telefono es: {telefono_dividivo[1]}")
