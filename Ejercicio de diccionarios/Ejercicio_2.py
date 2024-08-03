datos = {"nombre": "", "edad": "", "direccion": "", "telefono": ""}

datos["nombre"] = input("Ingrese su nombre: ")
datos["edad"] = input("Ingrese su edad: ")
datos["direccion"] = input("Ingrese su direccion: ")
datos["telefono"] =input("Ingrese su numero de telefono: ")

print(f"{datos['nombre']}, tiene {datos['edad']}, años, vive en la direccion {datos['direccion']} y su numero de telefono es: {datos['telefono']}")

