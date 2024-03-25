r = 2 # broj redaka
s = 3 # broj stupaca
# matrica, prazan niz
matrica = []

# jedan od nacina
for i in range(r):
    red = [0] * s # red s brojem stupaca koji su 0
    for j in range(s):
        tekst = "Unesi element u redak: " + str(i) + ", stupac: " + str(j) 
        unos = int(input(tekst))
        red[j] = unos
    matrica.append(red)

print(matrica)

# drugi nacin
for i in range r:
    red = [0] * s
    matrica.append(red)
    for j in range(s):
        unos = int(input("Unesi element:"))
        matrica[i][j] = unos
        
print(matrica)




        




