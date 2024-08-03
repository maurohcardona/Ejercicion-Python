lista = []

for i in range(1, 11):
    lista.append(i)
    
lista.sort(reverse=True)

for numero in lista:
    print(numero, end=", ")