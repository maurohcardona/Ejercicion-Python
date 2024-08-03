clientes = {}
continuar = True
NIF = 1

while continuar:
    opcion = input("(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        direccion = input("Ingrese la direccion: ")
        telefono = input("Ingrese el numero de telefono: ")
        correo = input("Ingrese el correo: ")
        preferente = input("Ingrese 'si' si se trata de un cliente preferente: ") == "si"
        clientes[NIF] = {"Nombre": nombre, "Direccion": direccion, "Telefono": telefono, "Correo": correo, "Preferente": preferente}
        NIF+=1
        print(clientes)
    
    elif opcion == "2":
        nif = int(input("Ingrese el NIF del cliente a eliminar: "))
        if nif in clientes:
            del clientes[nif]
        else:
            print("El NIF ingresado no pertenece a la base de datos")
    
    elif opcion == "3":
        nif = int(input("Ingrese el NIF del cliente a mostrar: "))
        if nif in clientes:
            print(clientes[nif])
        else:
            print("El NIF ingresado no pertenece a la base de datos")
    
    elif opcion == "4":
        print("Lista de todos los clientes:")
        for clave, valor in clientes.items():
            print(f"El NIF: {clave} se llama {valor["Nombre"]}")
    
    elif opcion == "5":
        print("Lista de todos los clientes preferenciales:")
        for clave, valor in clientes.items():
            if valor["Preferente"] == True:
                print(f"El NIF: {clave} se llama {valor["Nombre"]}")
                
    elif opcion == "6":
        print("Programa finalizado")
        continuar = False
        
    
    else:
        print("La opcion indicada no es una opcion valida")
            
        