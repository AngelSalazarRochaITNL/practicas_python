
## una cadena a diccionario con su frecuencia

dicStr = {}
    
def Exist(palabra) -> bool:
    for key in dicStr:
        if key == palabra:
            return True
    return False

def StrToMap(str):
    strList = str.split()
    for p in strList:
        if Exist(p):
            dicStr[p] += 1
        else:
            dicStr[p] = 1

StrToMap(input("Escribe una frase; "))

elemento_con_maximo_valor = max(dicStr.items(), key = lambda x: x[1])

elementos_con_segundo_maximo_valor = [clave for clave, valor in diccionario.items() if valor == segundo_maximo_valor]


print(elemento_con_maximo_valor + segundo_elemento)
    

# Como quieres que el te quiera si el que quiero que el quiera no me quiere como quiero que el quiera