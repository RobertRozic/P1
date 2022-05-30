# 9. Od korisnika zatražiti unos broja. Izgenerirati niz od toliko nasumičnih brojeva u
# intervalu [1, 200]. Zatim inicijalizirati novi niz u kojemu će biti svako 2. element iz
# prethodnog niza i ispisati njegovu aritmetičku sredinu.

import random

unos = int(input("Unesi broj:"))

brojevi = []
for i in range(unos):
  broj = random.randint(1, 200)
  brojevi.append(broj)

novi = brojevi[::2]

print("Aritmeticka sredina je:", sum(novi)/len(novi))

