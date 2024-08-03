diccionario = {}
palabras = input("Introduzca las palabras a agregar en el diccionario: ").split(",")

for palabra in palabras:
    clave, valor = palabra.split(":")
    diccionario[clave] = valor
    

frase = input("Ingrese una frase en español: ").split()
traduccion = []

for palabra in frase:
    if palabra in diccionario.keys():
        traduccion.append(diccionario[palabra])
    else:
        traduccion.append(palabra)

print(" ".join(traduccion))


#pelota:ball,cama:bed,silla:chair,chico:boy



