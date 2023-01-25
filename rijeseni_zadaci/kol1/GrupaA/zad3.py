'''
Napisati program koji od korisnika traži unos 12 brojeva.
Izračunati aritmetičku sredinu svih parnih unesenih brojeva.

Provjeriti je li zbroj prvog i cetvrtog unesenog broja djeljiv s 5.
Ukoliko jest, ispiši kvadrat aritmetičke sredine, a inače ispiši rezultat cjelobrojnog djeljenja aritmetičke sredine i broja neparnih unesenih brojeva.
'''

zbroj_parnih = 0
brojac_parnih = 0
brojac_neparnih = 0

for i in range(12):
  broj = int(input('Unesi broj: '))
  if i == 0:
    prvi = broj
  if i == 3:
    cetvrti = broj
  if broj % 2 == 0:
    zbroj_parnih += broj
    brojac_parnih += 1
  else:
    brojac_neparnih += 1

aritmeticka = zbroj_parnih / brojac_parnih

if (prvi + cetvrti) % 5 == 0:
  print("Kvadrat aritmeticke sredine:", aritmeticka**2)
else:
  print("Cjelobrojno:", aritmeticka//brojac_neparnih)
