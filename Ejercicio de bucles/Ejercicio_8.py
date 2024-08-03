numero = int(input("Ingrese un numero entero positivo "))

for i in range(1, numero+1, 2):
    for j in range(i,-1,-2):
        print(j, end=" ")
    print("")