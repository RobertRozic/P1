'''
Napiši program koji od korisnika traži unos
četveroznamenkastog broja koji je djeljiv s 3.

Ukoliko unese pogrešan broj, ispisati poruku
"Pogrešan unos"

Program zatim provjerava je li zbroj prve
i zadnje znamenke veći ili manji od 10 te
ispisuje povratnu poruku.
'''
unos = int(input("Unesi cetveroznamenkasti broj koji je djeljiv s 3: "))

#if unos <= 9999 and unos > 999:
#if unos < 10000 and unos >= 1000:
#if unos <= 9999 and unos >= 1000:
'''
if unos < 10000 and unos > 999 and unos % 3 == 0:
    print("Broj je cetveroznamenkast i djeljiv s 3!")
else:
    print("Pogresan unos!")
'''

# Obrnuto
if unos >= 10000 or unos <= 999 or unos % 3 != 0:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
    prva = unos // 1000 # 5678
    print("Prva znamenka", prva)
    zadnja = unos % 10 # 5001 // 10 500 i ostatak 1
    print("Zadnja znamenka", zadnja)
    zbroj = prva + zadnja
    print("Zbroj", zbroj)
    if zbroj > 10:
        print("Zbroj je veci od 10")
    else:
        print("Zbroj je manji od 10")
    

'''
cetveroznamenkast_djeljiv_s_tri = unos < 10000 and unos > 999 and unos % 3 == 0
print("Boolean:", cetveroznamenkast)

if cetveroznamenkast_djeljiv_s_tri:
    print("Ispravan unos!")
else:
    print("Pogresan unos!")

if not cetveroznamenkast_djeljiv_s_tri:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
'''



    
    
