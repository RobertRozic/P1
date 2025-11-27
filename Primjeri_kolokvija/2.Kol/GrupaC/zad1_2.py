def jeLiSavrsen(broj):
    zbroj = 0
    for i in range(1, broj):
      if broj % i == 0:
        zbroj += i

    return zbroj == broj
  

import random

a = int(input("Unesite pocetak intervala: "))
b = int(input("Unesite kraj intervala: "))

brojevi = []
for i in range(20):
  broj = random.randint(a,b)
  brojevi.append(broj)
  
for br in brojevi:
  if jeLiSavrsen(br):
  	print(br)
