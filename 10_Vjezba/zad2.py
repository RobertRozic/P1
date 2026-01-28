'''
Korištenjem while petlje i break
iskaza od korisnika tražiti unos brojeva u niz
sve dok ne unese “x” ili “X”.

Unesene brojeve dinamički spremati u niz.

Napisati funkciju koja kao argument prima niz
i računa prosjek samo parnih brojeva.
Funkcija kao rezultat vraća taj prosjek u glavni program.
'''
brojevi = []

while True:
    unos = input("Unesi broj: ")
    #if unos == 'x' or unos == 'X':
    if unos.lower() == 'x':
        break
    brojevi.append(int(unos))

print("Korisnik je unio:", brojevi)

# Funkcija za racunanje prosjeka parnih brojeva
def prosjekParnih(niz): # prima niz
    zbroj = 0 # Postavljamo zbroj na 0
    brojac = 0 # Postavljamo brojac na 0

    # Prolazimo kroz svaki element
    for el in niz:
        if el % 2 == 0: # ako je element paran
            zbroj += el # Zbrajamo ga u zbroj
            brojac += 1 # Povecavamo brojac za 1
            
    return zbroj/brojac

rezultat = prosjekParnih(brojevi)
print("Prosjek unesenih parnih brojeva je:", rezultat)
    
