'''
Napiši program koji definira vaše ime i godine.
Zatim od korisnika zadražite unos imena i godine rođenja te izračunajte korisnikov broj godina.
Ispisati je li korisnik programa mlađi ili stariji od vas i za koliko godina.
Poruka treb uključivati imena korisnika npr. "Korisnik Marko je stariji od korisnika Ivan za 4 god."
'''

moje_ime = 'Robert'
moje_godine = 26

ime = input('Unesi ime: ')
godina_rodjenja = int(input('Unesi godinu rodjenja: '))
godine = 2023 - godina_rodjenja

razlika = abs(moje_godine - godine)
if moje_godine > godine:
	print("Korisnik", ime, "je mladji od korisnika", moje_ime, "za", razlika, "godine")
elif moje_godine < godine:
	print("Korisnik", ime, "je stariji od korisnika", moje_ime, "za", razlika, "godine")
else:
	print("Korisnici imaju isto godina.")
