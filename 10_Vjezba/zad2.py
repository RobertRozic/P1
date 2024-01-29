'''
Korištenjem while petlje i break izkaza
od korisnika tražiti unos brojeva u niz
sve dok ne unese “x” ili “X” .

Unesene brojeve dinamički spremati u niz.

Napisati funkciju koja kao argument prima niz
i računa prosjek samo parnih brojeva.

Funkcija kao rezultat vraća taj prosjek u glavni program.
'''

niz = [] # definiramo prazan niz
# beskonacna petlja
while True: # while 1:
    unos = input("Unesi broj:") # trazimo unos teksta (string)
    if unos.lower() == "x": # pretvaramo unos u mala slova i usporedjujemo s x
        print("Izlaz iz programa!")
        break
    niz.append(int(unos)) # unos pretvaramo u int i dodajemo u niz - dinamicki

def prosjekParnih(brojevi):
    parni = [] # prazan niz u koji spremamo parne
    for broj in brojevi:
        if broj % 2 == 0: # broj je paran
            parni.append(broj) # dodaj u niz
    prosjek = sum(parni)/len(parni)
    return prosjek

rez = prosjekParnih(niz) # pozivamo funckiju i prosljedjujemo niz
print("Prosjek unesenih parnih brojeva je:", rez)
