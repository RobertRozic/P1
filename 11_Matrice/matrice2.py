r = 2 # broj redaka
s = 3 # broj stupaca
# matrica, prazan niz
matrica = []

for i in range(r):
    red = [0] * s # red s brojem stupaca koji su 0
    matrica.append(red)

print(matrica)

for i in range(r):
    for j in range(s):
        tekst = "Unesi element u redak: " + str(i) + ", stupac: " + str(j) 
        unos = int(input(tekst))
        matrica[i][j] = unos

print(matrica)

