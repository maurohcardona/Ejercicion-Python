capital = int(input("Ingrese el capital a a invertir "))
interes = int(input("Ingrese la tasa de interes anual en % "))
años = int(input("Ingrese la cantidad de años a invertir "))

for i in range(1, años+1):
    capital = capital*(1+interes/100)  
    print(f"El año {i}, se obtuvo una ganancia de ${capital:.2f}")
    
    