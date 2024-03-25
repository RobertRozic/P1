import random

r = 4
s = 4

matrica = []

# Definiranje matrice
for i in range(r):
    red = []
    for j in range(s):
        unos = random.randint(1, 9)
        red.append(unos)
    matrica.append(red)

#print(matrica)

# Pregledan ispis matricec
for red in matrica:
    print(red)

# Element po element
print("--" * s)
for red in matrica:
    for element in red:
        print(element, end=" ")
    print("")    
print("--" * s)

for i in range(r):
    for j in range(s):
        print(matrica[i][j], end=" ")
    print("") 
    

    
