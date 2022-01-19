def dvoznamenkast(x):    
    return x >= 10 and x <=99

def predzadnja(x):
    return int(x%100/10)

for i in range(3):
    broj = int(input("Unesite broj:"))
    if dvoznamenkast(broj):
        break

if not dvoznamenkast(broj):
    print("Pogresan unos")
else:
    zadnja = broj % 10
    predzadnja = predzadnja(broj)
    print("zadnja: ", zadnja, " predzadnja: ", predzadnja)
    if (zadnja + predzadnja) % 3 == 0:
        print("Zbroj je djeljiv s tri")
    else:
        print("Zbroj nije djeljiv s tri")
    
    
