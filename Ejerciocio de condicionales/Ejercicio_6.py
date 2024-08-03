nombre = input("Ingrese su nombre ")
sexo = input("Ingrese su sexo con 'm' si es hobre o 'f' si es mujer ")

if ("a" <= nombre[0] < "m" and sexo == "f") or (sexo == "m" and "n" < nombre[0] <= "z"):
    print("Tu estas en el grupo A")
else:
    print("Tu estas en el grupo B")

