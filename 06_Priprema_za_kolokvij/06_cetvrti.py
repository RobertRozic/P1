# Napisati program koji od korisnika traži
# unos troznamenkastog broja.
# Nakon toga provjeriti je li
# zadnja znamenka tog broja djeljiva s 3.
# Ukoliko korisnik ne unese troznamenkasti broj,
# ispisati da je unos pogrešan.
broj = int(input("Unesi troznamenkasi broj:"))

#if broj > 99 and broj < 1000:
if broj >= 100 and broj <= 999: # provjera je li broj troznamenkast
    print("Unijeli ste troznamenkast broj!")
    zadnja = broj % 10 # zadnja znamenka
    if zadnja % 3 == 0: # ako je ostatak dijeljenja s 3 jednak 0
        print("Zadnja znamenka je djeljiva s 3")
    else:
        print("Zadnja znamenka nije djeljiva s 3")
else:
    print("Pogresan unos")
