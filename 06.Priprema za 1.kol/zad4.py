'''
Napisati program koji od korisnika traži unos troznamenkastog broja.
Nakon toga provjeriti je zadnja znamenka tog broja djeljiva s 3.
Ukoliko korisnik ne unese troznamenkasti broj, ispisati da je unos pogrešan.
'''

broj = int(input("Unesi troznamenkasti broj"))

'''
if broj > 99 and broj < 1000: # broj je troznamenkast
    
else:
    print("Pogresan unos.")
'''

if broj < 100 or broj >= 1000:
    print("Pogresan unos")
else:
    print("Dobar unos!")
    # 456
    zadnja = broj % 10 # zadnja znamenka
    #predzadnja = broj // 10 % 10
    # Ako je ostatak dijeljenja s 3 jednak 0, broj je djeljiv s 3
    if zadnja % 3 == 0:
        print("Zadnja znamenka je djeljiva s 3!")
    else:
        print("Zadnja znamenka nije djeljiva s 3!")
    #print("Zadnja znamenka je", zadnja)
    #print("Predzanja", predzadnja)
