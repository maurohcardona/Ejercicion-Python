palabra = input("Ingrese una palabra: ")

vocales = ["a", "e", "i", "o", "u"]
conteo = []

a = conteo.append(palabra.count("a"))
e = conteo.append(palabra.count("e"))
i = conteo.append(palabra.count("i"))
o = conteo.append(palabra.count("o"))
u = conteo.append(palabra.count("u"))

for index, vocal in enumerate(vocales):
    print(f"La vocal {vocal} aparece {conteo[index]} veces")