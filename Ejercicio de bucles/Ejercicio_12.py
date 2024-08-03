frase = input("Introduzca una frase: ")

letra = input("Introduzca una letra: ")

contador = 0

if frase.count(letra) > 0:  
    print(f"La letra {letra} aparece {frase.count(letra)} veces en la frase")
else:
    print(f"La letra {letra} no aparece en la frase")

for i in range(len(frase)):
    if frase[i] == letra:
        contador += 1
        
if contador > 0:
    print(f"La letra {letra} aparece {contador} veces en la frase")
else:
    print(f"La letra {letra} no aparece en la frase")