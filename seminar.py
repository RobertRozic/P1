
ime = 'Robert'
prezime = 'Rozic'
ocjena = 5

ucenici = []

def unos(ime, prezime, ocjena):
  podatak = [ime, prezime, ocjena]
  ucenici.append(podatak)


for i in range(5):
  ime = input("unesi ime:")
  prezime = input("unesi prezime:")
  ocjena = int(input("unesi ocjenu:"))
  unos(ime, prezime, ocjena)


print(ucenici)
