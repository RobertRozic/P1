# Zatrazi od korisnika unes 10 brojeva
# i spremi ih u listu
n = 10
brojevi = [0] * n
brojevi[4] = 7
brojevi[9] = 10
print(brojevi)

brojevi = [1, 3, 5]
print(brojevi)

print(brojevi[1])

n = 10
brojevi = [0] * n

for i in range(n):
    brojevi[i] = int(input('Unesi broj:'))

print(brojevi)

#brojevi[10] = 20
#brojevi[11] = 21

brojevi.append(20)
brojevi.append(21)

print(brojevi)
