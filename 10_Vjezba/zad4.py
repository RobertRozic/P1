# Koristeći beskonačnu petlju i break iskaz
# od korisnika tražiti unos imena datoteke.
# Ime datoteke je potrebno unijeti s ekstenzijom
#(npr. jpg, txt).
# Ukoliko se ne unese točka,
# zatražiti od korisnika ponovni unos sve dok ne unese
# ispravan format.
# Nakon toga ispisati o kojoj
# ekstenziji se radi i koliko slova
# ima naziv datoteke bez ekstenzije.
while True:
    unos = input("Unesi naziv datoteke:")
    if unos.find(".") > -1: # ako nema tocke, onda je -1
        break

# unos test.txt
tocka = unos.find(".")
ekstenzija = unos[tocka+1:] # od indexa+1 do ktraja
print("Ekstenzija je:", ekstenzija)
naziv = unos[:tocka] # od pocetka do indeksa
print("Naziv je:", naziv)
print("Broj slova u nazivu je:", len(naziv))

