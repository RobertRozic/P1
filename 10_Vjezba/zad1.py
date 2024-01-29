'''
Definiraj funkciju koja kao parametar prima 2 broja
te vraća niz brojeva djeljivih s 3 između njih.

Zatražiti od korisnike unos intervala
i ispisati duljinu te aritmetičku sredinu niza
koji smo dobili pozivom ranije definirane funkcije.
'''
# Definiranje funkcije koja prima dva parametra
def djeljiviSTri(prvi, drugi):
    niz = [] # niz u koji spremamo djeljive brojeve
    # for petljom prolazimo kroz sve brojeve izmedju
    # dva parametra
    for i in range(prvi, drugi):
        if i % 3 == 0: # djeljiv s 3 ako mu je ostatak dijeljenja 0
            niz.append(i)
    return niz # vracamo niz djeljivih brojeva
#rez = djeljiviSTri(1, 100)

# Poziv funkcije i print
#print(djeljiviSTri(1, 100))

a = int(input("Unesi pocetak intervala:"))
b = int(input("Unesi kraj intervala:"))

# pozivamo funkciju parametrima a i b
rez = djeljiviSTri(a, b) # spremamo u varijablu rez

# duljina niza
duljina = len(rez)
print("Duljina niza je:", duljina)

# aritmeticka sredina / prosjek
suma = sum(rez)
print("Zbroj je:", suma)
print("Prosjek je:", int(suma/duljina))


