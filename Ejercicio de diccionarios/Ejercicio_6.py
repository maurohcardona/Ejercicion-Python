datos = {}
continuar = True

while continuar:
    clave = input("Que dato desea agregar: ")
    valor = input(f"{clave}: ")
    datos[clave] = valor
    print(datos)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si" or "si"