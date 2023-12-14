'''
Napiši program koji od korisnika traži unos četveroznamenkastog broja kojem je predzadnja znamenka manja od 8.
Ukoliko unese pogrešan broj, ispisati poruku "Pogrešan unos"

Program zatim dohvaća predzadnju znamenku i ispisuje koji dan u tjednu predstavlja ta znamenka.
npr. ako je predzadnja znamenka 1, ispisuje "ponedjeljak" itd.
'''

broj = int(input("Unesite cetveroznamenkasti broj cija predzadnja znamenka je manja od 8"))

predzadnja = broj//10%10

if broj < 1000 or broj > 9999 or predzadnja > 7:
    print("Pogresan unos")
else:
    if predzadnja == 1:
        print("Ponedjeljak")
    elif predzadnja == 2:
        print("Utorak")
    elif predzadnja == 3:
        print("Srijeda")
    elif predzadnja == 4:
        print("Cetvrtak")
    elif predzadnja == 5:
        print("Petak")
    elif predzadnja == 6:
        print("Subota")
    else:
        print("Nedjelja")
        
