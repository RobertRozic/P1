'''
Na početku programa od korisnika tražiti unos 5 artikala
s njihovim cijenama.

Artikle i njihove cijene spremati u 2 niza
- artikli (niz naziva artikla)
i cijene(niz floatova) pomoću funkcije.

Ispisati pozicija - naziv - cijena
korisniku kao cjenik artikala.

Napisati program za ispis računa:
Korisnik iz unesene baze artikala bira artikal
na poziciji i unosi kupljenu količinu.
Ponavljati unos artikla sve dok se ne unese “x”.

Program množi cijenu artikla
s količinom te sumu zapisuje u novi niz - racun.

Zbrojiti sve elemente u nizu račun
i korisniku izbaciti ukupnu cijenu računa.
'''
artikli = ["mlijeko", "jaja", "kruh", "sok", "brasno"]
cijene = [2.3, 3.4, 1.5, 3, 2.7]

# funkcija za unos u nizove
def unos(a, b):
    artikli.append(a)
    cijene.append(b)

#for i in range(5): # unos 5 artikala
#    naziv = input("Unesi naziv:")
#    cijena = float(input("Unesi cijenu:"))
#    unos(naziv, cijena)

print(artikli, cijene)

# Ispis sifri, artikala i cijena
print("-- Sifra --- Naziv --- Cijena")
for i in range(5):
    print(i, artikli[i], cijene[i])
print("-----------------------------")

racun = [] # spremamo ukupnu cijenu u ovaj niz

# beskonacna petlja
while True:
    sifra = input("Unesite sifru:")
    # ako unese x izlaz iz programa
    if sifra.lower() == "x":
        break
    # pretvaramo sifru u integer kako bi koristili kao index
    sifra = int(sifra) # pretvaramo u integer
    print("Izabrani artikal je:", artikli[sifra]) # ispis naziva
    kolicina = int(input("Unesite kolicinu: ")) # unos kolicine
    total = cijene[sifra] * kolicina # mnozimo cijenu s kolicinom
    racun.append(total) # spremamo u racun

# zbroj svega u racunu
print("Ukupna cijena je:", sum(racun))
    



