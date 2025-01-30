# Zatražiti od korisnika unos broja
# te izgenerirati niz od toliko nasumičnih brojeva
# u intervalu [1, 500].
# Zatim inicijalizirati novi niz
# u kojemu će biti svako 3. element iz prethodnog niza.
# Nakon toga ispisati najveći i najmanji član novog niza.

import random

broj = int(input("Unesi broj:"))

brojevi = []
for i in range(broj):
    broj = random.randint(1, 500)
    brojevi.append(broj)

print(brojevi)

# Od niza brojeva uzimamo svako treci
noviNiz = brojevi[::3]
print(noviNiz)

print("Najveci je", max(noviNiz))
print("Najmanji je", min(noviNiz))


