'''
Definiraj funkciju koja
kao parametre prima 2 broja
te vraća niz brojeva djeljivih s 3
između njih.
Zatražiti od korisnika unos
intervala i ispisati duljinu te aritmetičku sredinu niza
koji smo dobili pozivom ranije definirane funkcije.
'''
# Definiranje funckije imena djeljiviSTri
# Funkcija prima parametre a i b 
def djeljiviSTri(a, b):
    brojevi = [] # Definiramo prazan niz brojeva
    # Prolazimo kroz sve brojeve izmedju a i b
    for i in range(a, b+1):
        if i % 3 == 0: # Provjeravamo je li broj djeljiv s 3
            brojevi.append(i) # Dinamicki dodajemo na kraj niza

    return brojevi # Vracamo niz brojeva

# Pozivamo funkciju rucno
#rezultat = djeljiviSTri(1,10)

# Od korisnika trazimo unos pocetka i kraja intervala
pocetak = int(input("Unesi pocetak intervala:"))
kraj = int(input("Unesi kraj intervala:"))

# Pozivamo funckiju
# Ono sto funkcija vraca spremamo u varijablu rezultat
rezultat = djeljiviSTri(pocetak, kraj)

print("Rezultat je:", rezultat)
print("Duljina niza:", len(rezultat))

# Stari nacin prosjeka
'''
zbroj = 0
brojac = 0
for el in rezultat:
    zbroj += el
    brojac += 1

print("Aritmeticka sredina:", zbroj/brojac)
'''

prosjek = sum(rezultat)/len(rezultat)
print("Aritmeticka sredina:", prosjek)
