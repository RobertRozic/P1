'''
Napiši program koji od korisnika traži unos 10 brojeva.

Izračunaj zbroj neparnih unesenih brojeva
i prosjek parnih unesenih brojeva.

Ukoliko nije upisan ni jedan parni ili
ni jedan neparni broj ispisati gresku, inače nastaviti program
provjerom je li suma neparnih brojeva veća od 20.

Ako jest, ispiši prvi uneseni neparni broj,
inače ispiši zadnji uneseni parni broj.
'''
zbroj_neparnih = 0
zbroj_parnih = 0
brojac_parnih = 0
#brojac_neparnih = 0

prvi_neparni = None
zadnji_parni = None

for i in range(10):
    unos = int(input("Unesi broj:"))
    if unos % 2 == 1: # neparan
        zbroj_neparnih += unos
        if not prvi_neparni:
            prvi_neparni = unos
        #brojac_neparnih += 1
    else:
        zbroj_parnih += unos
        brojac_parnih += 1
        zadnji_parni = unos

if brojac_parnih == 0 or zbroj_neparnih == 0:
    print("Greska!")
else:
    prosjek_parnih = zbroj_parnih / brojac_parnih
    if zbroj_neparnih > 20:
        print("prvi neparni", prvi_neparni)
    else:
        print("zadnji parni", zadnji_parni)
    

        
    
