#Napisati program koji generira kvadratnu matricu dimenzija 5x5.
#Elementi su nasumični (random) brojevi od 1 do 9.
#Zatim napisati program koji računa zbroj elemenata na glavnoj i obrnutoj dijagonali matrice.

import random

r = 5
s = 5
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
        if j==i or i + j == 4:
            zbroj += matrica[i][j]

print("Zbroj elemenata na glavnoj i obrnutoj dijagonali:", zbroj)


            
