
def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *=valor
    return resultado
print("Multiplicación de los numeros; ",multiplicar(3,5,2))
