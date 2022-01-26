'''Korištenjem while petlje i break izkaza od korisnika tražiti unos brojeva u niz sve dok ne unese “x” ili
“X” . Unesene brojeve dinamički spremati u niz.
Napisati funkciju koja kao argument prima niz i računa prosjek samo parnih brojeva.
Funkcija kao rezultat vraća taj prosjek u glavni program.
'''

# Definiranje funkcije na pocetku programa
def prosjekParnih(niz):
  # definiramo praznu listu gdje cemo spremati parne elemente
  parni = []
  # prolazimo kroz sve elemente u nizu
  for el in niz:
    # ako naidjemo na paran element,
    # njega dodajemo u niz parnih brojeva
    if el % 2 == 0:
      parni.append(el)
  # racunamo prosjek tako sto podijelimoo sumu i broj elemenata
  # u nizu parnih brojeva
  prosjek = sum(parni)/len(parni)
  # funckija kao rezultat vraca prosjek
  return prosjek
      
brojevi = []

while 1:
  # Trazimo unos brojeva
  # ne radimo pretvorbu u int kako bi mogli provjeriti je li unos x
  unos = input("Unesi broj:")
  # unos pretvaramo u malo slovo, kako bi
  # osigurali da se program gasi i kada se unese veliko slovo X
  if unos.lower() == 'x':
    break
  # ukoliko nismo izasli iz programa, unos dodajemo u niz brojeva
  brojevi.append(int(unos))
  
# nakon zavrsenog unosa niz brojeva saljemo u ranije definiranu funkciju
# funckija vraca prosjek parnih brojeva i mi ga ispisujemo
print(prosjekParnih(brojevi))
