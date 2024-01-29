'''
Napisati program koji od korisnika traži
unos učenika u dnevnik.

Imena spremati u jedan, a prezimena u drugi niz.

Za dodavanje učenika napisati funkciju
koja kao parametre prima ime i prezime
i ne vraća ništa.

Korisnik unosi učenike sve dok se ne unese x ili X.

Nakon unosa, program ispisuje ime - prezime - šifru učenika
(šifra je pozicija/index u nizu).

Simulirati nasumično otvaranje dnevnika
tako da se slučajnim odabirom ispiše ime jednog od učenika.
'''
import random

imena = []
prezimena = []

# definiranje funkcije za unos
def unos(a, b):
    imena.append(a)
    prezimena.append(b)

#unos("Ivan", "Ivic")
#unos("Ana", "Anic")

while True:
    ime = input("Unesi ime: ")
    prezime = input("Unesi prezime:")
    if ime.lower() == "x" or prezime.lower() == "x":
        print("Izlaz iz programa:")
        break
    unos(ime, prezime) # poziv funkcije za unos

print("Imena:", imena)
print("Prezimena:", prezimena)

broj = len(imena)

print("----- Ucenici u dnevniku: -----")
# Ispis svih ucenika sa sifrom, imenom i prezimenom
for i in range(broj):
    print(i, imena[i], prezimena[i])
print("----- ------------- -----")

# nasumicni broj od 0 do onoliko koliko ima upisanih ucenika
nasumicni = random.randint(0, broj)

print("Nasumicno odabrani:", imena[nasumicni], prezimena[nasumicni])





















