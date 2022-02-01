#Napisati funkciju koja kao parametre prima ime i prezime te broj bodova na kolokviju.
#Zapis u programu spremiti u niz oblika [ime, prezime, bodovi].
#Zatim funkcija te podatke zapisuje u datoteku rezultati.txt u formatu "ime,prezime,bodovi".
#Svaki novi zapis prelazi u novi red

datoteka = open("rezultati.txt", "w")

def unos(ime, prezime, bodovi):
    student = [ime, prezime, str(bodovi)]
    student = ",".join(student)
    datoteka.write(student + '\n')

#U glavnom programu od korisnika tražiti unos osoba te broj bodova između 0 i 100.
#Podatke unositi sve dok se kao ime ili prezime ne unese broj 0.
#Ukoliko je ispravno unešen broj bodova (0-100) pozivati funkciju definiranu u #drugom zadatku koja će unesene podatke spremiti u datoteku,
#inače preskočiti poziv funkcije za unos.
while 1:
  ime = input("Unesite ime: ")
  if ime == "0":
    break
  prezime = input("Unesite prezime: ")
  if prezime == "0":
    break
  bodovi = int(input("Unesite broj bodova(0-100): "))
  if (bodovi < 100 and bodovi > 0):
    unos(ime, prezime, bodovi)

datoteka.close()
