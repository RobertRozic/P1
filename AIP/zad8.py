# 8. Zatražiti od korisnika unos 10 brojeva. Provjeriti je li zbroj prvih 5 brojeva veći od
# prosjeka unesenih brojeva. Na kraju programa ispisati koliko je jednoznamenkastih
# brojeva uneseno.

zbroj = 0
zbroj_prvih_pet = 0
jednoznamenkasti = 0

for i in range(10):
    broj = int(input("Unesite broj:"))
    if i < 5:
        zbroj_prvih_pet += broj
    if broj < 10 and broj >= 0:
        jednoznamenkasti += 1
    zbroj += broj
		
prosjek = zbroj/10
if zbroj_prvih_pet > prosjek:
    print("Zbroj prvih pet je veci od prosjeka unesenih brojeva.")

print("Uneseno je", jednoznamenkasti, "jednoznamenkastih brojeva.")
