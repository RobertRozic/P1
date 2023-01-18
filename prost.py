'''
Zatražiti od korisnika unos broja.
Provjeriti je li taj broj prost koristeći while petlju i break iskaz.
Prosti brojevi su prirodni brojevi koji su bez ostatka djeljivi samo sa 1 i sa samim sobom i strogo su
veći od broja 1.
'''

broj = int(input("Unesi broj: "))
prost = True
i = 2

while True:
    if broj == 2:
        break
    if broj % i == 0:
        prost = False
        break
    i = i+1
    if i >= broj:
        break

if prost:
    print("Broj je prost.")
else:
    print("Broj nije prost.")
