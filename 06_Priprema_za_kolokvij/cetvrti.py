"""
Napisati program koji od korisnika traži
unos troznamenkastog broja.

Ukoliko korisnik ne unese troznamenkasti broj,
ispisati da je unos pogrešan.

Nakon toga provjeriti je zadnja znamenka
tog broja djeljiva s 3.
"""
unos = int(input("Unesite troznamenkasti broj: "))

'''
#if unos > 99 and unos < 1000:
if unos >= 100 and unos <= 999:
    print("Ispravan unos!")
else:
    print("Pogresan unos!")
'''

if unos < 100 or unos > 999:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
    # Provjera je li zadnja znamenka djeljiva s 3
    # 456 ostatak dijeljena s 10 je zadnja znamenka
    zadnja = unos % 10
    if zadnja % 3 == 0:
        print("Zadnja znamenka je djeljiva s 3!")
    else:
        print("Zadnja znamenka nije djeljiva s 3!")
    
    
    







