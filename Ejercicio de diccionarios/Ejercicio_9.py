facturas = {}
continuar = True
cobrado = 0
adeudado = 0

while continuar:
    seleccion = input("Marque 'a' para agregar una factura nueva, 'p' para pagar una factura o 't' para terminar: ")
    if seleccion == "a":
        num_factura = input("Ingrese le numero de la factura a agregar: ")
        facturas[num_factura] = float(input("Ingrese el costo de la factura: "))
        adeudado += facturas[num_factura]
    elif seleccion == "p":
        num_factura = input("Ingrese le numero de la factura a pagar: ")
        if num_factura in facturas:
            cobrado += facturas[num_factura]
            adeudado -= facturas[num_factura]
            del facturas[num_factura]
        else:
            print("Ese numero de factura es no se encuentra en el sistema")
    elif seleccion == "t":
        print("Programa terminado")
        break
    else:
        print("La opcion seleccionada no es una opcion valida")
    print(facturas)
    print(f"El monto total cobrado es de ${cobrado} y el adeudado es de ${adeudado}")
        
    
        

