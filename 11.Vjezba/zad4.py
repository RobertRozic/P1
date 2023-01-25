'''
Koristeći beskonačnu petlju i break iskaz od korisnika tražiti unos imena datoteke.
Ime datoteke je potrebno unijeti s ekstenzijom (npr. jpg, txt).
Ukoliko se ne unese točka, zatražiti od korisnika ponovni unos sve dok ne unese ispravan format.
Nakon toga ispisati o kojoj ekstenziji se radi i koliko slova ima naziv datoteke bez ekstenzije.
'''

# Pokrecemo beskonacnu petlju
while True:
  unos = input("Unesi ime datoteke:")
  # Ukoliko se unese tocka, unos je ispravan i izlazimo iz petlje
  if "." in unos: # ako se u nizu znakova 'unos' nalazi '.'
    break

# Ukoliko dodjemo do ovoga dijela programa
# znamo da se while petlja izvrsila i da je unesena
# ispravna datoteka    

# split funckija nam dijeli string na 2 dijela po zadanom separatoru
# u nasem slucaju po tocki
datoteka = unos.split(".")

# sve do tocke ce biti 0 element liste
# poslije tocke ce biti el. s indeksom 1 itd. ukoliko imamo vise tocaka
ime = datoteka[0]
ekstenzija = datoteka[1]

print("Ekstenzija je:", ekstenzija)

# Koristeci ugradjenu funckiju len,
# dobijamo koliko znakova ima string imena datoteke
print("Broj slova datoteke bez ekstenzije je:", len(ime))

