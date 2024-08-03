simbolos = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

solicitud = input("Ingrese la moneda: ")

if solicitud in simbolos:
    print(simbolos[solicitud])
else:
    print("La moneda ingresada no es correcta")
    
#OTRA SOLUCION

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
