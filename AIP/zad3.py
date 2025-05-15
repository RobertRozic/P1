# 3. Zatražiti od korisnika unos 3 riječi. Provjeriti postoje li dvije jednako unesene riječi i
# ispisati korisniku. Zatim ispisati svaku unesenu riječ, ali ispisujući samo svako drugi
# znak

# Trazimo unos tri rijeci i spremamo u varijable a, b i c
a=input("Unesi prvu rijec:")
b=input("Unesi drugi rijec:")
c=input("Unesi treci rijec:")

# Provjera postoje li unesene dvije medjusobno jednake rijeci
if a == b or b == c or c == a:
	print("Unesene su najmanje dvije jednake rijeci")
	
# Ispis svako drugog znaka svake unesene rijeci
print(a[::2])
print(b[::2])
print(c[::2])
