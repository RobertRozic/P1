import random

r = 5
s = 5

matrica = []

for i in range(r):
  red = []
  for j in range(s):
    # Unos je nasumicni broj
    unos = random.randint(1, 9)
    red.append(unos)
  matrica.append(red)

# Ispis matrice
print("----- Matrica ------")
for i in range(r):
  for j in range(s):
    print(matrica[i][j], end=" ")
  print()

zbroj = 0
for i in range(r):
  for j in range(s):
    if i == j:
      zbroj += matrica[i][j]

print("Zbroj elemenata na glavnoj dijagonali je:", zbroj)
