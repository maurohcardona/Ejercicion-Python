munecos = int(input("Ingrese la cantidad de munecos vendidos "))

payasos = int(input("Ingrese la cantidad de payasos vendidos "))

peso_total_munecos = munecos * 75

peso_total_payasos = payasos * 112


def peso_total(peso_munecos, peso_payasos):
    
    peso_totales = peso_munecos + peso_payasos
    
    if peso_totales <= 1000:
        
        print(f"El peso total del paquete sera de {peso_totales} gramos")
    
    else:
        
        peso_totales = peso_totales/1000
        print(f"El peso total del paquete sera de {peso_totales} Kilogramos")
    
    
peso_total(peso_total_munecos,peso_total_payasos)
