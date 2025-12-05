'''
Napiši program koji od korisnika traži
unos duljine 2 stranice pravokutnika.

Ukoliko su stranice jednake, ispisati:
Unijeli ste kvadrat.

U slučaju da je unesen broj manji od 0 ispisati
"Barem jedna stranica je manja od 0".

Ako je prva stranica veća od druge, ispisati opseg,
inače ispisati površinu tog pravokutnika.
'''
# Od korisnika trazimo unos dvije stranice
a = input("Unesi prvu stranicu prvokutnika: ")
b = input("Unesi drugu stranicu pravokutnika: ")

# Pretvorba u integer
a = int(a)
b = int(b)

if a < 0 or b < 0:
    print("Barem jedna stranica je manja od 0!")
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
    
    # Provjera jesu li a i b jednaki
    if a == b:
        print("test")
        print("Unijeli ste kvadrat!")
    elif a > b:
        #o = 2 * a + 2 * b
        o = 2 * (a + b)
        print("Opseg je: ", o)
    else:
        p = a * b
        print("Povrsina je: ", p)




