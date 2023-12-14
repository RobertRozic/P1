'''
Napisati program koji od korisnika traži unos 8 brojeva.
Izračunati umnožak svih unesenih brojeva koji su ili djeljivi s 3 ili manji od 4.
Dohvatiti drugi, peti i sedmi uneseni broj, te ih na kraju programa ispisati sa "." umjesto razmakom između njih.
Ukoliko je umnožak veći od 1000 ispisati umnožak, a inače ispisati zbroj svih brojeva koji nisu uzeti u obzir
'''

umnozak = 1
ostali = 0

for i in range(8):
  broj = int(input('Unesi broj: '))
  if broj % 3 == 0 or broj < 4:
    umnozak *= broj
  else:
    ostali += broj
  if i == 1:
    drugi = broj
  if i == 4:
    peti = broj
  if i == 6:
    sedmi = broj


print(drugi, peti, sedmi, sep=".")

if umnozak > 1000:
  print("Umnozak", umnozak)
else:
  print("Zbroj ostalih", ostali)
