renta = int(input("Indique su renta anual "))

if renta < 10000:
    print("Tu tipo impositivo es del 5%")
elif 10000 < renta < 20000:
    print("Tu tipo impositivo es del 15%")
elif 20000 < renta < 35000:
    print("Tu tipo impositivo es del 20%")
elif 35000 < renta < 60000:
    print("Tu tipo impositivo es del 30%")
elif renta > 60000:
    print("Tu tipo impositivo es del 45%")
    