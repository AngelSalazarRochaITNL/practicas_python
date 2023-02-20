abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
x = 0
for l in abc:
    x+=1
    if x == 3:
        abc.remove(l)
        x = 1
print(abc)