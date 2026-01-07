'''
Tražiti od korisnika unos dvoznamenkastog broja
u 10 pokušaja.
Prekinuti traženje unosa ukoliko
unese dvoznamekasti broj.
Ukoliko nije unio dvoznamenkasti broj,
ispisati “Pogrešan unos”
Inače zbrojiti njegove znamenke
i ispisati je li zbroj znamenki djeljiv s 3.
'''
unio_dvoznamenkast = False

for i in range(10):
    broj = int(input("Unesi dvoznamenkasti broj"))
    if broj > 9 and broj < 100:
        unio_dvoznamenkast = True
        break

if not unio_dvoznamenkast:
    print("Pogresan unos!")
else:
    zadnja = broj % 10
    predzadnja = broj // 10
    zbroj = zadnja + predzadnja
    if zbroj % 3 == 0:
        print("Zbroj znamenki je djeljiv s 3")
    else:
        print("Zbroj znamenki nije djeljiv s 3")

