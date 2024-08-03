import math

def medidas(lista):
    diccionario = {}
    media = sum(lista)/len(lista)
    varianza = sum((x - media) ** 2 for x in lista) / len(lista)
    desviacion_tipica = round(math.sqrt(varianza),2)
    diccionario["Media"] = media
    diccionario["Varianza"] = varianza
    diccionario["Desvio Standar"] = desviacion_tipica  
    return diccionario 
    
print(medidas([1,2,3,4,5]))