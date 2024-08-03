fecha = input("Ingrese una fecha con el formato dd/mm/aa: ")

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

fecha = list(map(int,fecha.split("/")))

print(f"{fecha[0]} de {meses[fecha[1]]} de {fecha[2]}")