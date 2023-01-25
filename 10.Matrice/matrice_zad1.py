'''
Učitaj 2 matrice dimenzija mxn i formiraj treću
kao zbroj prve dvije i ispisati je.
'''
import random

r = 4
s = 4

m1 = []
m2 = []

# Popunjavanje prve matrice
for i in range(r):
    red = []
    for j in range(s):
        broj = random.randint(1, 9)
        red.append(broj)
    m1.append(red)

for i in range(r):
    for j in range(s):
        print(m1[i][j], end=' ')
    print()

print("---------------------")

# Popunavanje druge matrice
for i in range(r):
    red = []
    for j in range(s):
        broj = random.randint(1, 9)
        red.append(broj)
    m2.append(red)

for i in range(r):
    for j in range(s):
        print(m2[i][j], end=' ')
    print()

print("---------------------")

m3 = []
for i in range(r):
    red = []
    for j in range(s):
        zbroj = m1[i][j] + m2[i][j]
        red.append(zbroj)
    m3.append(red)

for i in range(r):
    for j in range(s):
        print(m3[i][j], end=' ')
    print()
