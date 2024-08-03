asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
asignaturas_reprobadas = []



for asignatura in asignaturas:
    nota = int(input(f"Ingrese la nota para la asignatura {asignatura}: "))
    if nota < 7:
        asignaturas_reprobadas.append(asignatura)
    
        
print(asignaturas_reprobadas)
