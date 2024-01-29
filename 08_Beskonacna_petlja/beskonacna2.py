#Zatražiti od korisnika unos broja.
#Provjeriti je li taj broj prost koristeći
#while petlju i break iskaz.

#Prosti brojevi su prirodni brojevi
#koji su bez ostatka djeljivi samo sa 1
#i sa samim sobom i strogo su veći od broja 1.

broj = int(input("Unesite broj:"))
prost = True # pretpostavimo da je broj prost
i = 2 # brojac, krecemo provjeravati je li broj djeljiv s 2

while True:
    if i == broj: # kada dodjemo do kraja, prekidamo petlju
        break
    if broj % i == 0:
        # ako je djeljiv s bilo kojim brojem
        # nije prost
        prost = False
        break

    i += 1 # povecavamo i za 1

if prost:
    print("broj je prost")
else:
    print("broj nije prost")
