def jeLiPalindrom(rijec):
	rijecUnatrag = rijec[::-1]
	return rijec == rijecUnatrag # usporedimo je li rijec jednaka citajuci je unazad
	
unos = input("Unesite tekst: ")

# skloni razmake:
unos = unos.replace(" ", "")

# pretvori sve u mala (ili velika) slova
unos = unos.lower()

if(jeLiPalindrom(unos)):
	print("Unos je palindrom!")
else:
	print("Unos nije palindrom!")
