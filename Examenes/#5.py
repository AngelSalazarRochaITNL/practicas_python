# #Ejercicio 5 - Angel Salazar, Francisco De la Rosa
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
l7 = []
l8 = []
l9 = []
l10 = []

for i in range(1,11):
    l1.append(i)
    l2.append(i+10)
    l3.append(i+20)
    l4.append(i+30)
    l5.append(i+40)
    l6.append(i+50)
    l7.append(i+60)
    l8.append(i+70)
    l9.append(i+80)
    l10.append(i+90)

def sumaDeListas(n = int(input("Valor de n: "))):
    suma = l1[n]+l2[n]+l3[n]+l4[n]+l5[n]+l6[n]+l7[n]+l8[n]+l9[n]+l10[n]
    return suma

print(sumaDeListas())