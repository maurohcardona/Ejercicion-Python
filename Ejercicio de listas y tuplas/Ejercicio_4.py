numeros_ganadores = input("Ingrese los numero ganadores separados por un espacio: ")

lista_numeros = (list(map(int, numeros_ganadores.split(" "))))

lista_numeros.sort()

print(lista_numeros)


