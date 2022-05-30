# 10. Zatražiti od korisnika unos sve dok ne unese troznamenkasti broj. Ukoliko ne unese
# troznamenkasti broj, ispisati “Pogrešan unos”. Provjeriti je li uneseni broj djeljiv s 3.

import random

while 1:
  unos = int(input("Unesi troznamenkasti broj:"))
  if (unos > 99 and unos < 1000):
    break
  else:
    print("Pogresan unos.")  
    
if unos % 3 == 0:
  print("Uneseni broj je djeljiv s 3.")
else:
  print("Uneseni broj nije djeljiv s 3.")
