# Zatražiti od korisnika unos broja.
# Provjeriti je li taj broj prost koristeći while petlju
# i break iskaz.

# Prosti brojevi su prirodni brojevi
#koji su bez ostatka djeljivi samo
# sa 1 i sa samim sobom i strogo su veći od broja 1.

broj = int(input("Unesi broj:"))

i = 1 # brojac
prost = True # Prepostavka da je broj prost

while i < broj - 1:
    i += 1
    if broj % i == 0:
        prost = False # Ukoliko naidjemo na broj s kojim je djeljiv, izlazimo iz programa
        break

if prost:
    print("Broj je prost!")
else:
    print("Broj nije prost!")

