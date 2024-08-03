email = input("Introduzca un mail ")

arroba = email.find("@")

usuario = email[0:arroba]

print(f"{usuario}@ceu.es")

