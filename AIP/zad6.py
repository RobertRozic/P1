# 6. Zatražiti od korisnika unos intervala, te dohvatiti 15 nasumičnih brojeva u tom
# intervalu. Ispisati one koji su djeljivi s 5.

import random

# Unos intervala
a = int(input("Unesite pocetak intervala: "))
b = int(input("Unesite kraj intervala: "))

for i in range(15):
  broj = random.randint(a,b) # dohvat random broja u tom intervalu
  if broj % 5 == 0: # provjera je li ostatak dijeljenja s 5 jednak 0
    print(broj) # ispis broja

