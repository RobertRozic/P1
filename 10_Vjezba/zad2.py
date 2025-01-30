# Korištenjem while petlje i break izkaza
# od korisnika tražiti unos brojeva
# u niz sve dok ne unese “x” ili “X” .
# Unesene brojeve dinamički spremati u niz.
def prosjekParnih(niz):
    parni = []
    for broj in niz:
        if broj % 2 == 0:
            parni.append(broj)
    prosjek = sum(parni)/len(parni)
    return prosjek

niz = []

while True:
    unos = input("Unesi broj:")
    #if unos == 'x' or unos == 'X':
    if unos.lower() == 'x':
        break
    #unos = int(unos)
    #Nakon provjere, unos pretvaramo u int
    niz.append(int(unos))

print("Uneseni brojevi:", niz)
print("Prosjek parnih je:", prosjekParnih(niz))


#Napisati funkciju koja kao
#argument prima niz i računa prosjek samo parnih brojeva.
#Funkcija kao rezultat vraća taj prosjek u glavni program.
