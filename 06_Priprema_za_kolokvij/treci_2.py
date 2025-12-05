'''
Napisati program u Pythonu koji će učitavati 10 brojeva.
Naći i ispisati aritmetičku sredinu učitanih brojeva
uzimajući u obzir samo one brojeve
koji su veći ili jednaki 2 i manji ili jednaki 5.
'''
zbroj = 0
brojac = 0

for i in range(10):
    poruka = "Unesi " + str(i+1) + ". broj: "
    unos = int(input(poruka))
    if unos >= 2 and unos <= 5:
        #zbroj = zbroj + unos
        zbroj += unos #kratica
        #brojac = brojac + 1
        brojac += 1 #kratica

print("Izvan petlje")
print("Broj brojeva uzetih u obzir:", brojac)
prosjek = zbroj/brojac
print("Aritmeticka sredina je:", prosjek)


    

