# Napiši program koji od korisnika traži unos duljine
# 2 stranice pravokutnika.
# Ukoliko su stranice jednake, ispisati: Unijeli ste kvadrat.
# U slučaju da je unesen broj manji od 0 ispisati
# "Jedna stranica je manja od 0".
# Ako je prva stranica veća od druge,
# ispisati opseg, inače ispisati površinu tog pravokutnika.

# od korisnika trazimo unos dvije stranice
# znamo da se unose cijeli brojevi i onda input
# odmah pretvaramo u integer funkcijom int()
a = int(input("Unesi prvu stranicu: "))
b = int(input("Unesi drugu stranicu: "))

# Ako su a i b jednaki, radi se o kvadratu
if a == b:
    print("Unijeli ste kvadrat!")

# Ako je unesen broj manji od 0, pogresan unos
if a < 0 or b < 0:
    print("Jedna od stranica je manja od 0")
# Inace radimo ostatak programa, za ispravan unos    
else:
    # Ako je a vece od b, ispisujemo opseg
    if a > b:
        o = 2 * a + 2 * b # formula za opseg
        print("Opseg je:", o)
    else:
        p = a*b # povrsina pravokutnika
        print("Povrsina je:", p)
    
