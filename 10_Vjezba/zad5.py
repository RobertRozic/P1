'''
Napisati program koji od korisnika traži
unos učenika u dnevnik.

Imena spremati u jedan, a prezimena u drugi niz.

Za dodavanje učenika napisati funkciju
koja kao parametre prima ime i prezime
dodati ih u niz
i ne vraća ništa.

Korisnik unosi učenike sve dok se ne unese x ili X.

Nakon unosa, program ispisuje ime - prezime - šifru učenika
(šifra je pozicija/index u nizu).

Simulirati nasumično otvaranje dnevnika
tako da se slučajnim odabirom ispiše ime jednog od učenika.
'''

imena = []
prezimena = []

def dodajUcenika(ime, prezime):
    imena.append(ime)
    prezimena.append(prezime)

while True:
    unos1 = input("Unesi ime ucenika:")
    if unos1.lower() == 'x':
        break
    unos2 = input("Unesi prezime ucenika:")
    dodajUcenika(unos1, unos2)
    
print(imena)
print(prezimena)

duljina = len(imena)

for i in range(duljina):
    print(i, '-', imena[i], '-', prezimena[i])

import random
odabir = random.randrange(0,duljina)

print("Nasumicno je odabran:", imena[odabir], prezimena[odabir])



