'''
Napiši program koji definira 2 vasa omiljena filma sa IMDB i njihove prosjecne ocjene kao decimalne brojeve.
Zatražite od kosinika unos ocjene za svaki od navedenih filmova, i ispisite mu je li njegov unos manji ili veći od prosječne ocjene tog filma i za koliko.
'''

# Definiranje filmova i prosjecnih ocjena
film1 = 'Inception'
ocjena1 = 8.8
film2 = 'The Prestige'
ocjena2 = 8.5

# Upit za ocjene korisnika
ocjena_korisnika1 = float(input("Kako bi ocjenili film " + film1 + " "))
ocjena_korisnika2 = float(input("Kako bi ocjenili film " + film2 + " "))

# Usporedba ocjene korisnika s ocjenom s IMDB
if ocjena_korisnika1 > ocjena1:
    print("Vasa ocjena za film", film1, "je veca od prosjecne ocjene na IMDB za", ocjena_korisnika1 - ocjena1)
else:
    print("Vasa ocjena za film", film1, "je manja od prosjecne ocjene na IMDB za", ocjena1 - ocjena_korisnika1)

if ocjena_korisnika2 > ocjena2:
    print("Vasa ocjena za film", film2, "je veca od prosjecne ocjene na IMDB za", ocjena_korisnika2 - ocjena2)
else:
    print("Vasa ocjena za film", film2, "je manja od prosjecne ocjene na IMDB za", ocjena2 - ocjena_korisnika2)

