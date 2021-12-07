# Tocan broj elemenata u listi
#n = 10
#brojevi = [0] * n
#
#for i in range(n):
#  brojevi[i] = int(input("Unesi broj"))
#
#print(brojevi)

# Dinamicna lista

brojevi = []

unos = 1

while unos != 0:
  unos = int(input("Unesite broj:"))
  if unos != 0:
    brojevi.append(unos)
  
suma = 0
print(brojevi)

for i in brojevi:
  print(i)
  suma += i
print(suma)


