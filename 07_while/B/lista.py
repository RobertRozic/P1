# unosi brojeve sve dok se ne unese broj veci od 50
# Ispisi sve unesene brojeve

brojevi = []

unos = int(input("Unesi broj: "))

while(unos < 50):
    brojevi.append(unos)
    unos = int(input("Unesi broj: "))

for broj in brojevi:
    print(broj)
