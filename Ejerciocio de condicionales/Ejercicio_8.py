puntuacion_empleado = float(input("Ingrese la puntuacion del empleado "))

salario_basico = 2400

if puntuacion_empleado == 0.0:
    print(f"El nivel del empleado fue inaceptable, y cobra un salario de ${salario_basico}")

elif puntuacion_empleado == 0.4:
     print(f"El nivel del empleado fue aceptable, y cobra un salario de ${salario_basico * (puntuacion_empleado+1)}")
     
elif puntuacion_empleado >= 0.6:
     print(f"El nivel del empleado fue meritorio, y cobra un salario de ${salario_basico * (puntuacion_empleado+1)}")
     
else:
    print("La puntuacion del empleado no es valida")