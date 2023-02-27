d = {}
x = "si"
total = 0
while x == "si":
    d [input("Ingrese la materia: ")] = input("Ingrese el numero de creditos: ")
    x = input("Seguir capturando?")
for m in d:
    print("La materia",m,"tiene",d.get(m),"creditos")
    total += int(d.get(m))
print("Con una suma total de creditos de:",total)

