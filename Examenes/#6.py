l1 = ["a","b",2,3]
l2 = ["c","d",3,4]

def mismosYDiferentes(l1,l2):
    lc = []
    lnc = []
    for i in l1:
        for j in l2:
            if i == j:
                lc.append(i)
            else:
                for k in lnc:
                    if k == i:
                        if k == j:
                # lnc.append(i)
                # lnc.append(j)
    return lc,lnc

print(mismosYDiferentes(l1,l2))