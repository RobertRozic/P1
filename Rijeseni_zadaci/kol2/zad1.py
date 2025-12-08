# Napisati funkciju koja prima dva broja kao parametre
# Vratiti listu brojeva
# između njih koji u sebi imaju znamenku 3 ili 6
# Od korisnika zatražiti unos dva broja
# Ispisati rezultirajuću listu te najveći
# parni i neparni broj iz liste
def imaTriISest(a, b):
    niz = []
    for i in range(a, b):
        if '3' in str(i) or '6' in str(i):
            niz.append(i)
    return niz

prvi = int(input("Unesi prvi broj:"))
drugi = int(input("Unesi drugi broj:"))

rezultat = imaTriISest(prvi,drugi)
print(rezultat)

parni = []
neparni = []

for broj in rezultat:
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)

print("Najveci parni", max(parni))
print("Najveci neparni", max(neparni)) 
