numero = int(input("Ingrese un numero para chequear si es un numero primo "))
primo = True

for i in range(2, numero):
    if numero%i == 0:
        print(f"El numero {numero} no es numero primo ya que puede dividirse por {i}")
        primo = False
    
if primo:
    print(f"El numero {numero} es un numero primo!!")