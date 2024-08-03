edad = int(input("Ingrese su edad "))
ingresos = int(input("Ingrese sus ingresos mensuales en euros "))

if edad >= 16 and ingresos >= 1000:
    print("Usted esta en condiciones de tributar")
else:
    print("Usted no esta en condiciones de tributar")