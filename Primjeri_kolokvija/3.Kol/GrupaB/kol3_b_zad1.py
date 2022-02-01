#Napisati program koji generira matricu dimenzija 4x6.
#Elementi su nasumični brojevi od 1 do 9.
#Zatim napisati program koji računa zbroj svih elemenata koji nisu na rubovima #matrice.

import random

r = 4
s = 6
matrica = []

for i in range(r):
    red = []
    for j in range(s):
        unos = random.randint(1,9)
        red.append(unos)
    matrica.append(red)

for red in matrica:
    for element in red:
        print(element, end=" ")
    print()
	
zbroj = 0
for i in range(r):
    for j in range(s):
        if (i != 0) and (i!=3) and (j != 0) and (j!=5):
            zbroj += matrica[i][j]

print("Zbroj elemenata koji nisu na rubovima matrice:", zbroj)


            
