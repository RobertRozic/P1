'''Na početku programa od korisnika tražiti unos 5 artikala s njihovim cijenama.
Artikle i njihove cijene spremati u 2 niza - artikli (niz naziva artikla) i cijene(niz floatova) pomoću
funkcije.
Ispisati pozicija - naziv - cijena korisniku kao cjenik artikala.
Napisati program za ispis računa:
Korisnik iz unesene baze artikala bira artikal na poziciji i unosi kupljenu količinu.
Ponavljati unos artikla sve dok se ne unese “x”.
Program množi cijenu artikla s količinom te sumu zapisuje u novi niz - racun.
Zbrojiti sve elemente u nizu račun i korisniku izbaciti ukupnu cijenu računa.'''

# Inicijalizirati prazne liste artikala i cijena
artikli = []
cijene = []
# artikle i cijene cemo spremati paralelno, u isto vrijeme
# prvi artikal koji ubacimo bit ce na indeksu 0 u artiklima,
# a ujedno i na indeksu 0 u cijenama, tako cemo znati da je to upravo njegova cijena

# Definiranje funckije za unos artikala u liste
# Funkcija prima 2 argumenta, naziv i cijena
def dodajArtikal(naziv, cijena):
  artikli.append(naziv)
  cijene.append(cijena)
  # nemamo return iskaza jer funckija ne vraca nista

# Od korisnika trazimo unos 5 artikala pomocu for petlje
for i in range(5):
  # Naziv artikla je obican input string
  naziv = input("Unesite naziv: ")
  # Cijenu artikla pretvaramo u float
  cijena = float(input("Unesite cijenu: "))
  dodajArtikal(naziv, cijena)

# Nakon sto korisnik unese artikle, ispisujemo cjenik
print("---------- Cjenik ----------")

for i in range(5):
  # i ce nam biti indeks, tj. pozicija u listi artikala/cijena
  # pomocu indeksa i pristupamo nazivu i cijeni artikla na toj poziciji
  print(i, artikli[i], "Cijena:", cijene[i])

print("--------------------------")

# Definiramo praznu listu racun
# Tu cemo spremati konacne cijene pojedinog artikla na racunu
racun = []

# Pokrecemo beskonacnu petlju kako bi omogucili unos artikala na racun
while 1:
  # Od korisnika trazimo unos sifre artikla
  # Sifra artikla je ustvari njegova pozicija u listi naziva/cijena
  sifra = input("Unesite sifru artikla:")
  # ukoliko je korisnik unio znak x ili X, prekidamo unos racuna
  if (sifra.lower() == 'x'):
    break;
  # Sifru pretvaramo u integer, kako bi mogli pristupati elementima u listi
  sifra = int(sifra)
  # Ispisujemo podatke o odabranom artiklu.
  # Imenu i cijeni pristupamo pomocu sifre tj. indeksa
  print("Odabrani artikal:", artikli[sifra], "po cijeni:", cijene[sifra])
  # Zatim od korisnika trazimo unos kolicine i pretvaramo u float
  kolicina = float(input("Unesite kolicinu:"))
  # Ukupna cijena tog artikla je cijena puta kolicina koju kupujemo
  total = cijene[sifra] * kolicina
  # Konacno, taj ukupan iznos spremamo u listu ukupnih iznosa artikala
  # odnosno racun
  racun.append(total)

print("--------------------------")

# Korisniku ispisujemo racun
print("-------Vaš račun----------")
# sumu radimo preko for petlje, prolazeci kroz svaki iznos
# u listi racun
suma = 0
for broj in racun:
  suma += broj

print("Total:", suma)

# Sumu mozemo i izracunati ugradjenom funkcijom sum()
print("Total:", sum(racun))

