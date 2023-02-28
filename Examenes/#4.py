
## 4. una cadena a diccionario con su frecuencia

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


maximo_valor = max(dicStr.values())

# Busca el elemento con el mayor valor
maximo_valor = max(dicStr.values())

# Busca las claves correspondientes al valor máximo
elementos_con_maximo_valor = [clave for clave, valor in dicStr.items() if valor == maximo_valor]

# Si hay elementos con el mismo valor máximo, imprime todos ellos
if len(elementos_con_maximo_valor) > 1:
    print("El elemento(s) con el valor máximo es/son:")
    for elemento in elementos_con_maximo_valor:
        print(f"{elemento}, {dicStr[elemento]}")
else:
    print(f"{elementos_con_maximo_valor[0]}, {dicStr[elementos_con_maximo_valor[0]]}")

# Como quieres que el te quiera si el que quiero que el quiera no me quiere como quiero que el quiera