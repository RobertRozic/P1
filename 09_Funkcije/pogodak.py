# Računalo zamisli jedan broj od 1 do 10.

# Korisnik ga pokuša pogoditi.
# Ukoliko ga pogodi ispisati „Pogodak”,
# inače „Broj je veći od zamišljenog” ili
# „Broj je manji od zamišljenog”.

import random

broj = random.randint(1,10)
brojac = 0
while True:
    unos = int(input("Pogodi koji sam broj zamislio: "))
    brojac += 1
    if broj == unos:
        print("Pogodak!")
        print("Trebalo vam je", brojac, "pokusaja!")
        break
    elif broj < unos:
        print("Zamislio sam manji broj od", unos)
    else:
        print("Zamislio sam veci broj od", unos)
