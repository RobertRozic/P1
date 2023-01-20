'''
Računalo zamisli jedan broj od 1 do 10.
Korisnik ga pokuša pogoditi.
Ukoliko ga pogodi ispisati „Pogodak”,
inače „Broj je veći od zamišljenog” ili
„Broj je manji od
zamišljenog”.
'''

import random


# broj koji racunalo zamisli
broj = random.randint(1, 1000)
print("Zamislio sam broj!")

while True:
    pokusaj = int(input("Pokusaj: "))
    if pokusaj == broj:
        print("Pogodak!")
        break
    elif pokusaj < broj:
        print("Pokusajte s vecim brojem!")
    else:
        print("Pokusajte s manjim brojem!")
    
    


