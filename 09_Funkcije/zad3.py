# Računalo zamisli jedan broj od 1 do 10.
# Korisnik ga pokuša pogoditi.
# Ukoliko ga pogodi ispisati „Pogodak”,
# inače „Broj je veći od zamišljenog”
# ili „Broj je manji od zamišljenog”.

from random import randint

zamisljeni_broj = randint(1,10)

'''
korisnikov_pokusaj = int(input("Pokusaj pogoditi zamisljeni broj: "))
while korisnikov_pokusaj != zamisljeni_broj:
    if korisnikov_pokusaj < zamisljeni_broj:
        print("Vas pokusaj je manji od zamisljenog broja!")
    else:
        print("Vas pokusaj je veci od zamisljenog broja!")
    korisnikov_pokusaj = int(input("Pokusaj pogoditi zamisljeni broj: "))
'''

br_pokusaja = 0
while 1:
    korisnikov_pokusaj = int(input("Pokusaj pogoditi zamisljeni broj: "))
    br_pokusaja += 1
    if korisnikov_pokusaj == zamisljeni_broj:
        break
    if korisnikov_pokusaj < zamisljeni_broj:
        print("Vas pokusaj je manji od zamisljenog broja!")
    else:
        print("Vas pokusaj je veci od zamisljenog broja!")

print("Pogodak!")
print("Trebalo vam je", br_pokusaja, "pokusaja!")
