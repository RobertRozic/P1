'''
Napiši program koji od korisnika traži unos duljine
2 stranice pravokutnika.
Ukoliko su stranice jednake, ispisati: Unijeli ste kvadrat.
U slučaju da je unesen broj manji od 0 ispisati
"Jedna stranica je manja od 0".
Ako je prva stranica veća od druge,
ispisati opseg, inače ispisati površinu tog pravokutnika.
'''

# trazimo unos od korisnika
a = input("Unesi prvu stranicu pravokutnika: ")
b = input("Unesi drugu stranicu pravokutnika: ")

# pretvaramo u int kako bi mogli obavljati aritmeticke operacije
a = int(a)
b = int(b)

# provjerili smo jesu li uenseni pozitvni brojevi
if a < 0 or b < 0:
    print("Barem jedna stranica je manja od 0!")
    print("Pogresan unos!")
else:
    if a == b:
        print("Unijeli ste kvadrat!")
        
    if a > b:
        o = 2 * a + 2 * b
        print("Opseg je:", o)
    else:
        p = a * b
        print("Povrsina je:", p)



