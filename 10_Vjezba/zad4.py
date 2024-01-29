'''
Koristeći beskonačnu petlju i break iskaz
od korisnika tražiti unos imena datoteke.

Ime datoteke je potrebno unijeti s ekstenzijom (npr. jpg, txt).
Ukoliko se ne unese točka, zatražiti od korisnika ponovni
unos sve dok ne unese ispravan format.

Nakon toga ispisati o kojoj ekstenziji se radi
i koliko slova ima naziv datoteke bez ekstenzije.
'''

while True:
    datoteka = input("Unesi datoteku s ekstenzijom: ")
    if "." in datoteka: # datoteka.find(".") > -1:
        print("Ispravan unos!")
        break

# ako smo dosli do ovog dijela programa
# korisnik je unio ispravno datoteku (ima tocka)

# prezentacija.pptx
tocka = datoteka.find(".") # index tocke
ekstenzija = datoteka[tocka+1:]

# naziv
naziv = datoteka[:tocka]

print("Ekstenzija je:", ekstenzija)
print("Naziv je:", naziv)
print("Broj slova:", len(naziv))

# 2. nacin
# funckija split
rez = datoteka.split(".")
print(rez)

print("Naziv:", len(rez[0]))
print("Ekstenzija:", rez[1])










