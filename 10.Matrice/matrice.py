# Definiranje broja redaka i stupaca
r = 2
s = 3

matrica = [] #[1, 2, 3]

#matrica = [[1, 2, 3], [4, 5, 6]]
#print(matrica)

for i in range(r):
  noviRed = [0] * s
  matrica.append(noviRed)
  # ili
  # matrica += [noviRed]

#print(matrica)

matrica = [[3, 5, 7], [1, 4, 2]]
#print(matrica[0][2])
'''
for i in range(r):
  for j in range(s):
    matrica[i][j] = int(input("Unesi element matrice na poziciji " + str(i) + ", " + str(j)))

for i in range(r):
  noviRed = [0] * s
  matrica.append(noviRed)
  for j in range(s):
    matrica[i][j] = int(input("Unesi element matrice"))
'''

# Kroz matricu prolazimo dvostrukom for petljom
#for red in matrica:
#  print(red) #ispisi reda matrice
  #for element in red:
  #  print(element) # ispis svih elemenata matrice

matrica = [[3, 5, 7], [1, 4, 2]]

for i in range(r):
  for j in range(s):
    print(matrica[i][j], end=" ")
  print()
