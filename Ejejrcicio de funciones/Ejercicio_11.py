def frecuencias(frase):
    diccionario = {}
    lista = frase.split(" ")
    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra] = frase.count(palabra)
    return diccionario

def tupla(diccionario):
    tupla = ()
    frecuencia = 0
    clave_valor_maximo = max(diccionario, key=lambda k:diccionario[k])
    return clave_valor_maximo, diccionario[clave_valor_maximo]
        
    
print(frecuencias("hola mauro como estas mauro"))
print(tupla(frecuencias("hola mauro como estas mauro")))