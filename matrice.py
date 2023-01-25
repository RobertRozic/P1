r = 2
s = 3
'''
matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(r)
    #matrica += [red]

#print(matrica)

matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(red)

print(matrica)
for i in range(r): # i predstavlja broj retka
    for j in range(s): # j predstavlja broj stupca
        matrica[i][j] = int(input("Unesi broj:"))

print(matrica)


matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(red)
    for j in range(s):
        matrica[i][j] = int(input("Unesi broj:"))

print(matrica)

'''
import random

r = 5
s = 5
matrica = []

# Kod za popunjavanje matrice
for i in range(r):
    red = []
    for j in range(s):
        broj = random.randint(1, 9)
        red.append(broj)
    matrica.append(red)

#print(matrica)

'''
for red in matrica:
    print(red)

# Kada zelimo pristupiti svakom elementu u matrici
# koristimo dvostruku for petlju!
for red in matrica:
    for element in red:
        print(element)
'''

for i in range(r):
    for j in range(s):
        print(matrica[i][j], end=' ')
    print()


