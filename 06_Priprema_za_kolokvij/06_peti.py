# Napišite program koji će ispisati sve brojeve od 1 do 10,
# a za svaki broj ispisati ako je paran ili neparan.
for i in range(1, 11):
    #print(i)
    if i % 2 == 0:
        print(i, "Paran")
    else:
        print(i, "Neparan")
