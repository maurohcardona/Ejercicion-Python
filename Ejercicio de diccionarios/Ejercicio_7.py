cesta = {}
continuar = True
costo_total = 0

while continuar:
    clave = input("Que producto desea agregar: ")
    valor = float(input(f"Ingrese el precio de {clave}: "))
    cesta[clave] = valor
    continuar = input('¿Quieres añadir más productos (Si/No)? ').title() == "Si" 
    
print("Lista de compra")

for producto, precio in cesta.items():
    print(f"{producto}--------- {precio}")
    costo_total += precio

print(f"Total---------- {costo_total}")