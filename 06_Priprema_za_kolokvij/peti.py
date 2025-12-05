'''
Napišite program koji će ispisati sve brojeve od 1 do 10,
a za svaki broj ispisati ako je paran ili neparan.
'''
#print(list(range(1,11,1)))

for i in range(1,11,1):
    if i % 2 == 0:
        print("Broj", i, "je paran.")
    else:
        print("Broj", i, "je neparan.")
