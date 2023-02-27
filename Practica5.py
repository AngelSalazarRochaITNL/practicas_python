# 5 Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{llave}”: “{Valor}”

a = {
    "Nombre": "Angel",
    "Apellidos": "Salazar Rocha",
    "Edad": 23
}

def dictionarys(*dic):
    print(dic)

print(dictionarys({"nombre":"Angel"}, {"nombre": "Slim"}))
