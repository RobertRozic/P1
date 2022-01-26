import random

r = 3
s = 3

m1 = []
m2 = []

# Popunjavanje 1 matrice
for i in range(r):
  red = []
  for j in range(s):
    # Unos je nasumicni broj
    unos = random.randint(1, 9)
    red.append(unos)
  m1.append(red)

# Popunjavanje 2 matrice
for i in range(r):
  red = []
  for j in range(s):
    # Unos je nasumicni broj
    unos = random.randint(1, 9)
    red.append(unos)
  m2.append(red)

# Ispis prve matrice
print("----- Prva matrica ------")
for i in range(r):
  for j in range(s):
    print(m1[i][j], end=" ")
  print()


# Ispis druge matrice
print("----- Druga matrica ------")
for i in range(r):
  for j in range(s):
    print(m2[i][j], end=" ")
  print()

m3 = []

for i in range(r):
  red = [0] * s
  m3.append(red)
  for j in range(s):
    m3[i][j] = m1[i][j] + m2[i][j]

# Ispis trece matrice
print("----- Treca matrica ------")
for i in range(r):
  for j in range(s):
    print(m3[i][j], end=" ")
  print()
