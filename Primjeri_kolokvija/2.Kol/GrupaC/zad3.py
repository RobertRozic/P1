def paranTroznamenkasti(broj):
  return broj < 1000 and broj > 99 and broj % 2 == 0

niz = [];

while 1:
  unos = int(input("Unesite paran troznamenkasti broj: "))
  niz.append(unos)
  if paranTroznamenkasti(unos):
    break
    
print("Aritmeticka sredina:", sum(niz)/len(niz))

