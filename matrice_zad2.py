'''
Napisati program koji generira kvadratnu matricu dimenzija 5x5.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na glavnoj dijagonali matrice.
(glavna dijagonala ide od gornjeg lijevog u donji desni kut matrice).
'''
import random

r = 5
s = 5

matrica = []

for i in range(r):
    red = []
    for j in range(s):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

for i in range(r):
    for j in range(s):
        print(matrica[i][j], end=' ')
    print()

zbroj = 0
for i in range(r):
    for j in range(s):
        if i == j: # glavna dijagonala
            zbroj += matrica[i][j]

print("Zbroj elemenata na obrnuta dijagonali je", zbroj)

zbroj = 0
for i in range(r):
    for j in range(s):
        if i + j == s - 1: # obrnuta dijagonala
            zbroj += matrica[i][j]

print("Zbroj elemenata na obrnutoj dijagonali je", zbroj)
