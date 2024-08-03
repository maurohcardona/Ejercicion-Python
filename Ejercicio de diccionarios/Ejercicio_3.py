frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

fruta = input("Ingrese la fruta que desea: ").title()

if fruta in frutas:
    peso = float(input("Ingrese los kilos que desea: "))
    costo = frutas[fruta]*peso
    print(f"El costo de {peso} kg de {fruta} es de ${costo}")
else:
    print("La fruta seleccionada no se encuentra")