'''
Napisati program koji od korisnika traži
unos učenika u dnevnik.

Imena spremati u jedan, a prezimena u drugi niz.

Za dodavanje učenika napisati funkciju
koja kao parametre prima ime i prezime i ne vraća ništa.

Korisnik unosi učenike sve dok se ne unese x ili X.

Nakon unosa, program ispisuje ime - prezime - šifru učenika
(šifra je pozicija/index u nizu).

Simulirati nasumično otvaranje dnevnika
tako da se slučajnim odabirom ispiše ime jednog od učenika.
'''
import random

imena = []
prezimena = []

def dodajUcenika(ime, prezime):
    imena.append(ime)
    prezimena.append(prezime)

#Rucno pozivanje funkcije
#dodajUcenika("Pero", "Peric")

while True:
    unos1 = input("Unesi ime:")
    #if unos1 == 'x' or unos1 == 'X':
    if unos1.lower() == 'x':
        break
    unos2 = input("Unesi prezime:")
    dodajUcenika(unos1, unos2)

print(imena)
print(prezimena)

duljina = len(imena)
for i in range(duljina):
    print(i, "-", imena[i], '-', prezimena[i])
    
odabir = random.randrange(0, duljina)
print("Nasumicni ucenik je:", imena[odabir], prezimena[odabir])
