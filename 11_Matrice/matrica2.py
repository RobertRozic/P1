r = 2
s = 3

matrica = []

'''for i in range(r):
    red = [0]* s
    matrica.append(red)
    print("Red: ", i)
    for j in range(s):
	    matrica[i][j] = int(input("Unesite broj: "))
'''

for i in range(r):
    red = []
    print("Red: ", i)
    for j in range(s):
	    unos = int(input("Unesite broj: "))
	    red.append(unos)
    matrica.append(red)
print(matrica)

for red in matrica:
    print(red)

for red in matrica:
    for element in red:
        print(element, end=" ")
    print()



