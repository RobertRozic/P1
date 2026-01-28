'''
Definiraj funkciju koja kao parametar prima 2 broja
te vraća niz brojeva djeljivih s 3 između njih.

Zatražiti od korisnike unos intervala
i ispisati duljinu te aritmetičku sredinu
niza koji smo dobili pozivom
ranije definirane funkcije.
'''
# Definiramo funkciju imena djeljviSTri
# Ta funkcija prima dva parametra, a i b
# Parametri predstavljaju pocetak i kraj intervala
def djeljiviSTri(a, b):
    brojevi = [] # definiramo prazan niz
    # Za svaki broj u rasponu od a do b+1
    for i in range(a, b+1):
        if i % 3 == 0: # ako je i djeljivo s 3
            brojevi.append(i) # i dodajemo u niz

    return brojevi # funkcija vraca niz brojeva

# Od korisnika zatrazimo unos granica intervala
pocetak = int(input("Unesi pocetak intervala: "))
kraj = int(input("Unesi kraj intervala: "))

# Ono sto funkcija vrati se sprema u rezultat
rezultat = djeljiviSTri(pocetak,kraj)

# Ispisujemo rezultat
print(rezultat)

# Duljina niza odnosno rezultata funkcije
print("Duljina niza:", len(rezultat))

# Stari nacin
'''
zbroj = 0
brojac = 0
for element in rezultat:
    zbroj += element
    brojac += 1

print("Aritmeticka sredina:", zbroj/brojac)
'''

prosjek = sum(rezultat)/len(rezultat)
print("Aritmeticka sredina je:", prosjek)


