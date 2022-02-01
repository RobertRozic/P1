import random

imena = []
prezimena = []

def dodajUcenika(ime, prezime):
  imena.append(ime)
  prezimena.append(prezime)

while 1:
  unos1 = input("Unesite ime ucenika")
  if unos1.lower() == 'x':
  	break;
  unos2 = input("Unesite prezime ucenika")
  dodajUcenika(unos1, unos2)
  
for i in range(len(imena)):
  print(str(i), " | ", imena[i], prezimena[i])

odabir = random.randrange(0, len(imena))

print("Odabrani ucenik:", imena[odabir] + " " + prezimena[odabir])
