deposito_inicial = int(input("Ingrese el monto a depositar "))

interes_anual = 4

tiempo = int(input("Ingrese la cantidad de anos a invertir "))

def calculo_de_inversion(deposito, interes, tiempo):
    
    print(f"El capital inicial es de ${deposito}")
    
    for ano in range(1, tiempo+1):
        
        capital_obtenido = deposito + (deposito*interes)/100
        
        deposito = capital_obtenido
        
        print(f"El capital obtenido el el ano {ano} es de ${capital_obtenido:.2f}")
        
calculo_de_inversion(deposito_inicial, interes_anual, tiempo)
        