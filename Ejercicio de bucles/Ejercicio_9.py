contraseña_correcta = "estufa10"

contraseña_usuario = ""

while contraseña_correcta != contraseña_usuario:
    contraseña_usuario = input("Ingrese la contraseña: ")
    if contraseña_usuario !=contraseña_correcta:
        print("Contraseña incorrecta!")
    else:
        print("¡Contraseña correcta!")
        break
        
    