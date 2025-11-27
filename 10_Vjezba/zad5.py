'''
Napisati program koji od korisnika traži unos učenika
u dnevnik.

Imena spremati u jedan, a prezimena u drugi niz.
Za dodavanje učenika napisati funkciju
koja kao parametre prima ime i prezime i ne vraća ništa. 
Korisnik unosi učenike sve dok se ne unese x ili X.
Nakon unosa, program ispisuje
ime - prezime - šifru učenika (šifra je pozicija/index u nizu).
Simulirati nasumično otvaranje dnevnika
tako da se slučajnim odabirom ispiše
ime jednog od učenika.
'''
import random

imena = []
prezimena = []

def dodajUcenika(ime, prezime):
    imena.append(ime)
    prezimena.append(prezime)

while 1:
    unosImena = input("Unesi ime:")
    if unosImena.lower() == 'x':
        break
    unosPrezimena = input("Unesi prezime:")
    if unosPrezimena.upper() == 'X':
        break
    dodajUcenika(unosImena, unosPrezimena)

print(imena, prezimena)

for i in range(len(imena)):
    print(imena[i], prezimena[i], i)

otvaranje = random.randint(0, len(imena)-1)
print("Odabran je ucenik:", imena[otvaranje], prezimena[otvaranje])

    

