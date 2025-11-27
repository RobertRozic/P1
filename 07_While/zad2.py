# Korisnik unosi 10 brojeva i sprema ih u listu brojevi
n = 10

# broj1 =
# broj2 = ...

brojevi = [None] * n
brojevi = [0] * n

print(brojevi)

#brojevi = [2, 5, 7]
#print(brojevi[2])
brojevi[1] = 6
print(brojevi)

for i in range(n):
    brojevi[i] = int(input("Unesi broj:"))

print(brojevi)
