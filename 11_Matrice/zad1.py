# Učitaj 2 matrice dimenzija mxn
# i formiraj treću kao zbroj prve dvije i ispisati je.

r = 2
s = 3

matrica1 = []
matrica2 = []

# Matrica 1
print("Matrica 1")
for i in range(r):
    red = []
    print("Red" + str(i))
    for j in range(s):
	    unos = int(input("Unesite broj: "))
	    red.append(unos)
    matrica1.append(red)
    
# Matrica 2
print("Matrica 2")
for i in range(r):
    red = []
    print("Red" + str(i))
    for j in range(s):
	    unos = int(input("Unesite broj: "))
	    red.append(unos)
    matrica2.append(red)

# ispis matrica 1
print("Matrica 1")
for red in matrica1:
    for element in red:
        print(element, end=" ")
    print()

# ispis matrica 2
print("Matrica 2")
for red in matrica2:
    for element in red:
        print(element, end=" ")
    print()

matrica3 = []

for i in range(r):
    red = []
    for j in range(s):
        zbroj = matrica1[i][j] + matrica2[i][j]
        red.append(zbroj)
    matrica3.append(red)

print("Matrica 3")
for red in matrica3:
    for element in red:
        print(element, end=" ")
    print()
        





