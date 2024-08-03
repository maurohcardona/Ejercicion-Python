def binario(numero):
    r = numero
    bin = []
    while r > 0:
        bin.append(r%2)
        r = r//2
    bin.reverse()
    return "".join(list(map(str,bin)))

def decimal(numero):
   lista = [int(x) for x in str(numero)]
   lista.reverse()
   potencias = []
   for index, numero in enumerate(lista):   
    potencias.append(numero*(2**(index)))
   print(sum(potencias))
    
    

# print(binario(19))
decimal(1011)
