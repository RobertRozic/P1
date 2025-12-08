'''
Napiši program koji od korisnika traži unos
četveroznamenkastog broja koji je djeljiv s 3.

Ukoliko unese pogrešan broj, ispisati poruku
"Pogrešan unos"

Program zatim provjerava je li zbroj prve i zadnje
znamenke veći ili manji od 10 te ispisuje povratnu poruku.
'''
unos = int(input("Unesi cetveroznamenkasti broj: "))

if unos < 1000 or unos > 9999 or unos % 3 != 0:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
    prva = unos//1000
    zadnja = unos % 10
    zbroj = prva + zadnja
    if zbroj > 10:
        print("Zbroj prve i zadnje je veci od 10!")
    else:
        print("Zbroj prve i zadnje nije veci od 10!")

#if unos >= 1000 and unos <= 9999 and unos % 3 == 0:
#    print("Ispravan unos!")
#else:
#    print("Pogresan unos!")




