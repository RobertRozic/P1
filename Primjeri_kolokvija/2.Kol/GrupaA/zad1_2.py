def razloziNaZnamenke(n):
  niz = []

  while n > 0:
    niz.append(n % 10)
    n = n // 10

  return niz
  
noviNiz = []

for i in range(3):
  unos = int(input("Unesite broj"))
  rezultat = razloziNaZnamenke(unos);
  noviNiz += rezultat

print("Znamenka 4 se pojavljuje " + str(noviNiz.count(4)) + " puta.")
