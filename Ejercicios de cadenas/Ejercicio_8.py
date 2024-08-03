precio = input("Introduce el precio con dos decimales ")

print(f"El precio es {precio[:precio.find(".")]} euros con {precio[precio.find(".")+1:]} centimos")