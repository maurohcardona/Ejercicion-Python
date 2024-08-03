palabra = input("Ingrese una palabra: ")

lista = []

es_palindromo = True

for letra in palabra:
    lista.append(letra)
    
for i in range(len(lista)):
    if lista[i] == lista[-i-1]:
        es_palindromo = True
    else:
        es_palindromo = False
        break
    
if es_palindromo ==True:
    print(f"la palabra {palabra} es un palindromo")
else:
    print(f"la palabra {palabra} no es un palindromo")