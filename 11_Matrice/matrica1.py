# Definiramo broj redaka i stupaca
r = 2
s = 3

# Inicijalizacija
matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(red)
    #matrica += [red]

#print(matrica)

# Prvi red
'''matrica[0][0] = 3
matrica[0][1] = 5
matrica[0][2] = 7'''

# Drugi red
'''matrica[1][0] = 1
matrica[1][1] = 4
matrica[1][2] = 2'''

print(matrica)

for i in range(r):# petlja za svaki red
    for j in range(s): #petlja za svaki stupac
        matrica[i][j] = int(input("Unesi broj za koordinate:" + str(i) + "," +str(j)))

print(matrica)


