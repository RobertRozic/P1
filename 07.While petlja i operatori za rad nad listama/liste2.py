# Zatrazi unos brojeva od korisnika
# sve dok ne unese broj veci od 50
brojevi = []

unos = int(input("Unesi broj:"))

while unos < 50:
    brojevi.append(unos)
    unos = int(input("Unesi broj:"))

print(brojevi)

#1, 5, 10, 42, 62

# Svojstvo liste je da je iterabilna
index = 0
for broj in brojevi:
    brojevi[index] = broj + 5
    index += 1

print(brojevi)
