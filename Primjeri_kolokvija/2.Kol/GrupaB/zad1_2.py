def jeLiProst(broj):
    prost = True
    i = 2
    while i < broj:
        if broj % i == 0:
            prost = False
            break
        i += 1
    return prost
  

import random

a = int(input("Unesite pocetak intervala: "))
b = int(input("Unesite kraj intervala: "))

prosti = []
for i in range(15):
  broj = random.randint(a,b)
  if jeLiProst(broj):
    prosti.append(broj)
 
print(len(prosti))
