def jeLiSavrsen(x):
    zbroj = 1
    for i in range(2, int(x/2)+1):
        if x%i == 0:
            zbroj += i
    return zbroj == x

    if zbroj == x:
        return "Broj je savrsen"

    return "Broj nije savrsen"
    

print("Savrseni brojevi od 1 do 1000 su:")
for i in range(1, 100000):
    if jeLiSavrsen(i):
        print(i)
    
