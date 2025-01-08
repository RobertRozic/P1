'''
Napiši program koji od korisnika traži unos broja.

Program zatim prolazi kroz svih sljedećih 50 brojeva
od tog broja. npr. Za uneseni broj 5, sve brojeve od 5 do 55.

Izračunaj zbroj svako drugog broja
i aritmetičku sredinu svih brojeva
djeljivih s 5 i ispiši ih.

Provjeri je li izračunati zbroj manji od 300.
Ako jest, ispiši prvi broj u nizu koji je djeljiv s 5,
inače ispiši prvi broj u nizu koji je djeljiv s 3.
'''
unos = int(input("Unesi broj:"))

zbroj_svako_drugog = 0
zbroj_dsp = 0
brojac_dsp = 0

prvi_s_pet = None
prvi_s_tri = None

for i in range(unos, unos+50):
    if i % 2 == 0:
        zbroj_svako_drugog += i
    if i % 5 == 0:
        if not prvi_s_pet:
            prvi_s_pet = i
        zbroj_dsp += i
        brojac_dsp += 1
    if i % 3 == 0:
        if not prvi_s_tri:
            prvi_s_tri = i

print("Zbroj svako drugog", zbroj_svako_drugog)
print("Aritmeticka sredina", zbroj_dsp/brojac_dsp)

if zbroj_svako_drugog < 300:
    print("Prvi djeljiv s 5", prvi_s_pet)
else:
    print("Prvi djeljiv s 3", prvi_s_tri)
    

