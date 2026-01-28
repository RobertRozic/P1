'''
Koristeći beskonačnu petlju i break iskaz
od korisnika tražiti unos imena datoteke.
Ime datoteke je potrebno unijeti s ekstenzijom (npr. jpg, txt).
Ukoliko se ne unese točka, zatražiti
od korisnika ponovni unos sve dok ne unese ispravan format.

Nakon toga ispisati o kojoj ekstenziji se radi
i koliko slova ima naziv datoteke bez ekstenzije.
'''

# beskonacna petlja
while True:
    unos = input("Unesi ime datoteke:")
    if unos.find(".") > -1: # ako pronadje tocku
        break # izlazi iz beskonacne petlje

tocka = unos.find(".")
print("Tocka se nalazi na indeksu:", tocka)

naziv = unos[:tocka]
print("Naziv je:", naziv)
print("Duljina naziva:", len(naziv))

ekstenzija = unos[tocka+1:]
print("Ekstenzija je:", ekstenzija)

