osobe = []
godine = []

def dodajOsobu(ime, god):
  osobe.append(ime)
  godine.append(god)

while 1:
  unos1 = input("Unesite ime osobe: ")
  if unos1.lower() == 'x':
  	break;
  unos2 = int(input("Unesite godine: "))
  dodajOsobu(unos1, unos2)
  
for i in range(len(osobe)):
  print(str(i), " | ", osobe[i], " Godine: ", godine[i])

sifra1 = int(input("Unesite sifru prve osobe: "))
sifra2 = int(input("Unesite sifru druge osobe: "))

razlika = godine[sifra1] - godine[sifra2]
print("Razlika u godinama je:", razlika)

if razlika < 0:
  print("Druga osoba je starija")
elif razlika > 0:
  print("Prva osoba je starija")
else:
  print("Osobe imaju jednako godina")
