numeros = input("Ingrese numeros separados por comas: ")

lista_numeros = list(map(int,(numeros.split(","))))

media = 0

for numero in lista_numeros:
    media += numero
    
media = media/len(lista_numeros)

print(media)

desvio_estandar = (sum((x - media) ** 2 for x in lista_numeros) / len(lista_numeros))**(1/2)


print(desvio_estandar)