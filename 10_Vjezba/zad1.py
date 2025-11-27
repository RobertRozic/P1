# Definiraj funkciju koja kao parametar
# prima 2 broja te vraća niz brojeva djeljivih
# s 3 između njih.

# Definiranje funkcije
def djeljiviSTri(a, b): # definiranje funkcije i parametara
    djeljivi = [] # Definiramo prazan niz
    for i in range(a, b): # prolazimo rasponom od a do b
        if i % 3 == 0:
            djeljivi.append(i) # dodajemo na kraj niza sve brojeve djeljive s 3
    return djeljivi # funkcija vraca vrijednost

# u varijablu brojevi spremamo ono sto funckija vrati
#brojevi = djeljiviSTri(1, 10)
# Ispis brojeva
#print(brojevi)

# Zatražiti od korisnike unos
# intervala i ispisati duljinu
# te aritmetičku sredinu niza koji
# smo dobili pozivom ranije definirane funkcije.
x = int(input("Unesi pocetak intervala:"))
y = int(input("Unesi kraj intervala:"))

brojevi = djeljiviSTri(x, y)
print("Rezultat", brojevi)
print("Duljina tog niza je:", len(brojevi))
print("Aritm. sredina", sum(brojevi)/len(brojevi))

''' Stari nacin
suma = 0
brojac = 0
for broj in brojevi:
    suma += broj
    brojac += 1
print("Aritm. sredina:", suma/brojac)
'''









