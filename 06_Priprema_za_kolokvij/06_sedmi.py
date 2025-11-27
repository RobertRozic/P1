# Napišite program koji će ispisati sve brojeve od 1 do 20,
# a za svaki broj ispisati ako je djeljiv sa 3 ili sa 5.

for i in range(1, 20):
    if i % 3 == 0:
        print(i, "je djeljiv s 3")
    if i % 5 == 0:
        print(i, "je djeljiv s 5")
