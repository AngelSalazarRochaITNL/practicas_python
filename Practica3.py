# 3 Entrada de datos y manipulación.
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
# manera inversa letra por letra

print("Escribe tu nombre; ")
nombre = input()
nombre = nombre[::-1]

for l in nombre:
    print(l)