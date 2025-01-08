#Napisati funkciju koja kao parametre prima ime i prezime te generira random broj između 1 i 30 koji predstavlja sretni broj osobe.
#Zapis u programu spremiti u niz oblika [ime, prezime, broj].
#Zatim funkcija te podatke zapisuje u datoteku osobe.txt u formatu "ime,prezime,broj".
#Svaki novi zapis prelazi u novi red.
import random

datoteka = open("osobe.txt", "w")

def unosOsobe(ime, prezime):
    broj = str(random.randint(1,30))
    zapis = [ime, prezime, broj]
    osoba = ",".join(zapis)
    datoteka.write(osoba + "\n")

#U glavnom programu od korisnika zatražiti unos osoba sve dok se unese x ili X.
#Ime mora sadržavati više od 2 slova. 
#Ukoliko je ispravno unešeno ime (više od 2 slova) pozivati funkciju definiranu u drugom zadatku koja će unesene podatke spremiti u datoteku,
#inače preskočiti poziv funkcije za unos.
while 1:
    ime = input("Unesite ime: ")
    if ime.lower() == "x":
        break
    elif len(ime) <= 2:
        print("Ime mora biti duze od 2 slova!")
    else:
        prezime = input("Unesite prezime: ")
        unosOsobe(ime, prezime)

datoteka.close()


    
