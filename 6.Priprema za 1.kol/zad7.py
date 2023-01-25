# Napišite program koji će ispisati svako drugi broj od 1 do 20,
#a za svaki broj ispisati ako je djeljiv sa 3 ili sa 5.
for i in range(1, 20, 2):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

# Zatrazi od korisnika unos 10 brojeva, na kraju ispisi peti uneseni broj
for i in range(10):
    broj = int(input("Unesi broj"))
    if i == 4:
        peti = broj

print("Peti uneseni broj je", peti)
