'''
Napiši program koji od korisnika traži unos
troznamenkastog broja i provjerava
je li zbroj njegovih znamenki paran ili neparan.

Ako je zbroj paran, ispisati
"Zbroj znamenki je paran",
inače "Zbroj znamenki je neparan".

Ukoliko korisnik ne unese troznamenkast broj,
ispisati "Pogrešan unos!"
'''

unos = int(input("Unesi troznamenkasti broj:"))

# if unos > 99 and unos < 1000:
# if unos >= 100 and unos < 1000:
#if unos > 99 and unos <= 999:
'''
if unos >= 100 and unos <= 999:
    print("Ispravan unos!")
else:
    print("Pogresan unos!")


if unos < 100 or unos > 999:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
'''
troznamenkast = unos >= 100 and unos <= 999

'''
if troznamenkast:
    print("Ispravan unos!")
else:
    print("Pogresan unos!")
'''

if not troznamenkast:
    print("Pogresan unos!")
else:
    print("Ispravan unos!")
    # 345
    treca = unos % 10
    druga = (unos % 100) // 10
    prva = unos // 100
    # 7345
    #cetvrta = unos % 10
    #treca = (unos % 100) // 10
    #druga = (unos % 1000) // 100
    #prva = unos // 1000
    zbroj = prva + druga + treca
    print("Prva", prva)
    print("Druga", druga)
    print("Treca", treca)
    print("Zbroj", zbroj)
    if zbroj % 2 == 0:
        print("Zbroj je paran!")
    else:
        print("Zbroj je neparan!")
    
    

'''
troznamenkast_novi = False
for i in range(100, 1000):
    if i == unos:
        troznamenkast_novi = True

print("Boolean:", troznamenkast_novi)
'''

    

