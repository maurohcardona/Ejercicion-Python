precios = [50, 75, 46, 22, 80, 65, 8]
precio_menor = sorted(precios)
precio_mayor = sorted(precios, reverse=True)

print(f"El menor de los precios es de $ {precio_menor[0]}")
print(f"El mayor de los precios es de $ {precio_mayor[0]}")

# OTRA SOLUCION

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))