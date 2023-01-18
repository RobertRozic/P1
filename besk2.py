'''
Tražiti od korisnika unos dvoznamenkastog broja u 10 pokušaja.
Prekinuti traženje unosa ukoliko unese dvoznamekasti broj.
Ukoliko nije unio dvoznamenkasti broj, ispisati “Pogrešan unos”
Inače zbrojiti njegove znamenke i ispisati je li zbroj znamenki
djeljiv s 3
'''

for i in range(10):
    broj = int(input("Unesi dvoznamenkasti broj: "))
    if broj > 9 and broj < 100:
        break

if broj > 9 and broj < 100:
    #zadnja = broj % 10
    #predzadnja = broj // 10
    #zbroj = zadnja + predzadnja
    brojStr = str(broj)
    zbroj = int(brojStr[0]) + int(brojStr[1])
    print("Zbroj znamenki:", zbroj)
else:
    print("Pogresan unos!")
