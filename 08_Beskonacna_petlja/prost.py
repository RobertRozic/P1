#Zatražiti od korisnika unos broja
#Provjeriti je li taj broj prost
#koristeći while petlju i break iskaz.

#Prosti brojevi su prirodni brojevi
#koji su bez ostatka djeljivi samo sa 1
#i sa samim sobom i strogo su veći od broja 1.

broj = int(input("Unesi broj: "))
prost = broj > 1

i = 2
while True:
    if broj <= i:
        break
    
    if broj % i == 0:
        prost = False
        break
    
    i += 1

if prost:
    print("Broj je prost!")
else:
    print("Broj nije prost!")

    
    
