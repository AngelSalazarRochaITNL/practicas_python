# 5 Manejo de información
# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{llave}”: “{Valor}”


def imprimir_datos(nombre, **datos):
    print("Nombre: {}".format(nombre))
    for clave, valor in datos.items():
        print("{}: {}".format(clave, valor))

imprimir_datos("Juan", edad=30, ciudad="Buenos Aires", profesion="Ingeniero")
