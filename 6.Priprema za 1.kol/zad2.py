'''
Napiši program koji od korisnika traži unos duljine 2 stranice pravokutnika.
Ukoliko su stranice jednake, ispisati: Unijeli ste kvadrat.
U slučaju da je unesen broj manji od 0 ispisati "Jedna stranica je manja od 0".
Ako je prva stranica veća od druge, ispisati opseg, inače ispisati površinu tog
pravokutnika.
'''

a = int(input("Unesi prvu stranicu pravokutnika: "))
b = int(input("Unesi drugu stranicu pravokutnika: "))

if a < 0 or b < 0:
    print("Jedna stranica je manja od 0.")
else:
    if a == b:
        print("Unijeli ste kvadrat!")
    
    if a > b:
        o = 2 * (a + b) # Formula za opseg pravokutnika
        print("Opseg pravokutnika je: ", o)
    else:
        p = a * b # Formula za površinu pravokutnika
        print("Površina pravokutnika je", p)
