studenti = []

# Funkcija za pretragu studenata po fakultetu
def filterPoFakultetu(naziv):
  # Kreiramo praznu listu gdje cemo ubacivati studente koje smo filtrirali
  novi = []
  # prolazimo kroz listu studenata
  for student in studenti:
    # Ukoliko je fakultet studenta (fakultet nam je na indesku 2)
    # jednak fakultetu koji je poslan kao parametar "naziv"
    # dodaj ga u novu listu
    if student[2].lower() == naziv.lower():
      novi.append(student)
  # Iz funkcije vracamo niz studenata    
  return novi;   
  
# Funkcija za ispis zaglavlja
def printZaglavlje():
  print("----------------------")
  print("Ukupan broj studenata:", len(studenti))
  # pomocu funkcije dohvati sve studente FPMOZ-a
  fpmoz = filterPoFakultetu("FPMOZ")
  # ispisi duljinu tog niza
  print("FPMOZ:", len(fpmoz))
  print("----------------------")

# Funkcija za unos studenta
def unosStudenta():
  ime = input("Unesi ime: ")
  prezime = input("Unesi prezime:")
  fakultet = input("Fakultet: ")
  # Student nam je zapisan u obliku liste
  # indeks 0 - ime, indeks 1 - prezime, indeks 2 - fakultet...
  student = [ime, prezime, fakultet]
  # U listu studenata, ubacujemo studenta
  studenti.append(student) 

# Funkcija za ispis svih studenata
def ispisStudenata():
  print("----------------------")
  print("Studenti:")
  for student in studenti:
    print(student[0], student[1], student[2])
  print("----------------------")

while True:
  # Pozivamo funkciju za ispis zaglavlja
  printZaglavlje()
  # Navodimo sve opcije koje korisnik moze odabrati
  print("----------------------")
  print("1) Unos studenta")
  print("2) Ispis svih studenata")
  print("0) Izlaz")
  print("----------------------")
  # Od korisnika trazimo unos, pretvaramo unos u integer
  unos = int(input("Odaberite opciju:"))
  # Provjeravamo koju opciju je odabrao korisnik
  # Ovisno o odabranoj opciji, pozivamo funkciju koju smo definirali
  if unos == 0:  
    # Ukoliko korisnik unese 0, izlazi se iz beskonacne petlje 
    break
  elif unos == 1:
    unosStudenta()
  elif unos == 2:
    ispisStudenata()
