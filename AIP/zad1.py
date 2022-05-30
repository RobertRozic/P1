# 1. Zatražiti od korisnika unos promjera kruga. Izračunati površinu kruga.

# Upit korisnika za unos promjera i spremanje u varijablu "r"
r = input("Unesi promjer kruga:")

# Pretvaranje varijable r u integer kako bi mogli s njom izvoditi matematicke operacije
r = int(r)

# Racunanje povrsine, formula je r na kvadrat puta pi
# U pythonu, potenciranje se vrsi dvostrukim znakom puta (**)
p = r**2*3.14

# Ispis povrsine
print("Povrsina kruga je:", p)
