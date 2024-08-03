creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_creditos = 0

for asignatura, creditos in creditos.items():
    print(f"{asignatura} tiene {creditos} creditos")
    total_creditos += creditos
    
print(f"El numero total de creditos es de {total_creditos} creditos")