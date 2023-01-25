'''
Definiraj funkciju koja kao parametar prima 2 broja te vraća niz brojeva djeljivih s 3 između njih.
Zatražiti od korisnike unos intervala i ispisati duljinu te aritmetičku sredinu niza koji smo dobili pozivom
ranije definirane funkcije.
'''

def djeljiviSTri(niz):
  # Definiranje praznog niza u koji cemo spremati
  # elemente koji su djeljivi s 3
  djeljivi = []
  # prolazak kroz svaki element u nizu
  for element in niz:
    if element % 3 == 0:
      # ako je element djeljiv s 3 spremamo ga u niz djeljivi
      djeljivi.append(element)
  # vracamo iz funkcije niz djeljivih brojeva
  return djeljivi

a = int(input("Unesi pocetak intervala"))
b = int(input("Unesi krej intervala"))

# dohvacamo niz elemenata u tom intervalu
elementi = list(range(a, b))

# u varijablu djeljivi spremamo rezultat funkcije
djeljivi = djeljiviSTri(elementi)

# koristeci ugredjenu funckciju sum, zbrajamo elemente niza
zbroj = sum(djeljivi)

# koristeci ugradjenu funkciju len dobijamo duljinu niza
duljina = len(djeljivi)

# dijeljenjem sume i duljine niza racunamo prosjek
prosjek = zbroj/duljina
print("Prosjek brojeva djeljivih s 3 u vasem intervalu je: ", prosjek)
