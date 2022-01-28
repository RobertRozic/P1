'''Napisati program koji od korisnika traži unos učenika u dnevnik.
Imena spremati u jedan, a prezimena u drugi niz.
Za dodavanje učenika napisati funkciju koja kao parametre prima ime i prezime i ne vraća ništa.
Korisnik unosi učenike sve dok se ne unese x ili X.
Nakon unosa, program ispisuje ime - prezime - šifru učenika (šifra je pozicija/index u nizu).
Simulirati nasumično otvaranje dnevnika tako da se slučajnim odabirom ispiše ime jednog od učenika.'''

# Inicijalizirati prazne liste imena i prezimena
imena = []
prezimena = []

# Definiranje funkcije koja prima 2 parametra (ime i prezime)
def unosUcenika(ime, prezime):
  # U listu imena dodajemo ime koje smo poslali kao parametar
  imena.append(ime)
  # Isto cinimo s prezimenom u listu prezimena
  prezimena.append(prezime)
  # Ne stavljamo return jer je naznaceno da
  # funckija ne vraca nikakvu vrijednost
  
# Pokrecemo beskonacnu petlju, jer nam nije poznat broj ponavljanja 
while 1:
  # Od korisnika trazimo unos imena
  unos1 = input("Unesi ime:")
  unos2 = input("Unesi prezime:")
  # ukoliko je korisnik unio znak 'x' kao ime ili prezime,
  # izlazimo iz petlje
  if unos1.lower() == 'x' or unos2.lower() == 'x':
    # za izlaz iz petlje koristimo break izkaz
    break
  # Ukoliko nismo izasli iz petlje, pozivamo funckiju za unos ucenika
  # Kao parametre, saljemo dva unosa
  # (prvi parametar je ime, drugi prezime)
  unosUcenika(unos1, unos2)
  
# Prvo prebrojimo koliko je uneseno ucenika
# Uneseno je ucenika onoliko kolika je duljina liste imena/prezimena 
broj_ucenika = len(imena)

# Nakon sto znamo br. ucenika, mozemo pokrenuti for petlju za ispis
for i in range(broj_ucenika):
  # i ce nam biti indeks, tj. pozicija u listi imena/prezimena
  # pomocu indeksa i pristupamo imenu i prezimenu na toj poziciji
  print(imena[i], prezimena[i], i)  
 
# Nasumicno otvaranje dnevnika je ustvari dohvacanje random indeksa
# od 0 do broja ucenika
import random
# Koristimo randrange kako nam ne bi bio ukljucen i broj ucenika
# (jer krecemo od 0), ako je 8 ucenika, max. indeks je 7
x = random.randrange(0, broj_ucenika)

# Nakon sto dohvatimo slucajni indeks
# dohvacamo ime i prezime na tom indeksu i ispisujemo
print("Nasumicno je otvoren:", imena[x], prezimena[x])
