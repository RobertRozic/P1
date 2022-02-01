artikli = []
cijene = []

def dodajArtikal(naziv, cijena):
  artikli.append(naziv)
  cijene.append(cijena)
  

while 1:
  unos1 = input("Unesite naziv artikla: ")
  if unos1.lower() == 'x':
  	break;
  unos2 = float(input("Unesite cijenu artikla: "))
  dodajArtikal(unos1, unos2)
  
for i in range(len(artikli)):
  print(str(i), " | ", artikli[i], " Cijena: ", cijene[i])

sifra = int(input("Unesite sifru artikla: "))
print("Odabrani artikal: ", artikli[sifra], "Cijena:", cijene[sifra])
kolicina = int(input("Unesite kolicinu artikla:"))

ukupno = kolicina * cijene[sifra]
pdv = ukupno * 0.17

print("Ukupno:", ukupno, "PDV 17%:", pdv)
