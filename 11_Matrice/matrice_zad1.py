# Učitaj 2 matrice dimenzija mxn
# i formiraj treću kao zbroj prve dvije
# i ispisati je.
import random

r = 3
s = 3

m1 = []
m2 = []

for i in range(r):
    red = []
    red2 = []
    for j in range(s):
        unos = random.randint(1, 9)
        unos2 = random.randint(1, 9)
        red.append(unos)
        red2.append(unos2)
    m1.append(red)
    m2.append(red2)

for red in m1:
    print(red)

print("----------")

for red in m2:
    print(red)

m3 = []
for i in range(r):
    red = [0] * s
    m3.append(red)
    for j in range(s):
        m3[i][j] = m1[i][j] + m2[i][j]
    

print("----------")

for red in m3:
    print(red)



    

