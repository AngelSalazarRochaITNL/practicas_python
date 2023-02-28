#Ejercicio 1 - Angel Salazar, Francisco De la Rosa
n = int(input("Valor de n: "))
m = int(input("Valor de m: "))
l = [n]
while n>1:
    l.append(int(n / m))
    n = n/m
if l.pop() == 0:
    print("Secuencia invalida")
else:
    l.append(1)
    print(l)