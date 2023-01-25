'''Na primjer programa kase iz prethodnog zadatka pri ispisu računa nakon izlaza “x” naredbom, ispisati
oblik racuna:
Sifra -- Naziv -- kolicina-- cijena -- total
...
Artikli…
1 Jaja 5 0.2 1
...
Ukupno:
Porez 17%: izračunati porez'''

# Preuzimamo kod iz prethodnog zad6.py
artikli = []
cijene = []

def dodajArtikal(naziv, cijena):
  artikli.append(naziv)
  cijene.append(cijena)

for i in range(5):
  naziv = input("Unesite naziv: ")
  cijena = float(input("Unesite cijenu: "))
  dodajArtikal(naziv, cijena)

print("---------- Cjenik ----------")

for i in range(5):
  print(i, artikli[i], "Cijena:", cijene[i])

print("--------------------------")

# Definiramo praznu listu racun
# U listu cemo spremati liste s podacima o kupljenim artiklima
# u obliku [sifra, kolicina, total]
# pomocu sifre cemo dohvatiti naziv i cijenu artikla
# a kolicinu i total spremamo podatak
racun = []

# Pokrecemo beskonacnu petlju kako bi omogucili unos artikala na racun
while 1:
  sifra = input("Unesite sifru artikla:")
  if (sifra.lower() == 'x'):
    break;
  sifra = int(sifra)
  print("Odabrani artikal:", artikli[sifra], "po cijeni:", cijene[sifra])
  kolicina = float(input("Unesite kolicinu:"))
  total = cijene[sifra] * kolicina
  # Podatke o kupnji spremamo u formatu listu
  podaci = [sifra, kolicina, total]
  # Tu listu dodajemo u prethodno definiranu listu racun
  racun.append(podaci)

print("--------------------------")

# Korisniku ispisujemo racun
print("-------Vaš račun----------")
print("Sifra -- Naziv -- kolicina-- cijena -- total")
suma = 0
# Prolazimo kroz svaki element u listi racun
for element in racun:
  # Kako nam je element takodjer lista
  # koju smo definirali po nasim pravilima
  # znamo da se na indeksu 0 nalazi sifra
  sifra = element[0]
  # na indeksu 1 nam se nalazi kolicina
  kolicina = element[1]
  # na indeksu 2 nam se nalazi total tog artikla 
  total = element[2]
  # total zbrajamo na ukupnu sumu
  suma += total
  # Zatim informacije ispisujemo u trazenom formatu
  print(sifra, artikli[sifra], kolicina, cijene[sifra], total)

# Kako bi dobili vrijdnost osnovice, ukupno dijelimo sa 1.17
# jer je suma = osnovica * 1.17
osnovica = suma / 1.17
# rezultat cemo zaokruziti na 2 decimale
osnovica = round(osnovica, 2)

# pdv je razlika sume i osnovice
print("PDV 17%:", round(suma - osnovica))
print("Total:", suma)
