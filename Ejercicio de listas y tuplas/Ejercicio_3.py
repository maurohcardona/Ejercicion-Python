asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []

for asignatua in asignaturas:
    nota = input(f"Ingrese la nota que ha sacado en {asignatua}: ")
    notas.append(nota)
    
for i in range(len(notas)):
    print(f"En {asignaturas[i]} has sacado un {notas[i]}")

