import random

while 1:
  unos = int(input("Unesi dvoznamenkasti broj:"))
  if (unos > 9 and unos < 100):
    break;
    
brojevi = []
for i in range(unos):
  broj = random.randint(1, 500)
  brojevi.append(broj)
  
novi = brojevi[::2]

print("Aritmeticka sredina:", sum(novi)/len(novi))  

