fecha_nacimiento = input("Ingrese la fecha de nacimineto en formato dd/mm/aa ")


dia = fecha_nacimiento[:fecha_nacimiento.find("/")]
mes = fecha_nacimiento[fecha_nacimiento.find("/")+1:fecha_nacimiento.find("/", 3)]
año = fecha_nacimiento[fecha_nacimiento.find("/", 3)+1:]

print(f"Usted nacio el {dia} del mes {mes} del año {año} ")