
def multiplicar(*args):
    resultado = 1
    for valor in args:
        resultado *=valor
    return resultado
print("Multiplicación de los numeros; ",multiplicar(1,2,3,4,5,6,7))
