'''
Napisati program u Pythonu koji će učitavati 10 brojeva.
Naći i ispisati aritmetičku sredinu učitanih
brojeva uzimajući u obzir samo one brojeve
koji su veći ili jednaki 2 i manji ili jednaki 5.
'''
# Definiramo zbroj i brojac
zbroj = 0
brojac = 0

for i in range(10):
    #print("Unesi", i+1, ". broj: ", end="")
    poruka = "Unesi " + str(i+1) + ". broj: "
    unos = int(input(poruka))
    # Provjera hocemo li broj uzeti u obzir
    if unos >= 2 and unos <= 5:
        #zbroj = zbroj + broj
        zbroj += unos # kratica
        #brojac = brojac + 1
        brojac += 1 # kratica

# Izlazimo iz for petlje, racunamo prosjek
prosjek = zbroj/brojac
print("Aritmeticka sredina je:", prosjek)

        

