# Spremaj unesene brojeve korisnika
# sve dok se ne unese broj veci od 50

brojevi = []

unos = int(input("Unesi broj:"))

while unos < 50:
    brojevi.append(unos)
    unos = int(input("Unesi broj:"))

#print(brojevi)

for broj in brojevi:
    print(broj)


