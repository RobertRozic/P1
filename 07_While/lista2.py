# Korisnik unosi brojeve sve dok ne unese broj manji od 50
# Program mu ispisuje pogresne pokusaje.

# Definiranje prazne liste
brojevi = []

# Korisnik unosi broj
unos = int(input('Unesi broj: '))

# sve dok je uneseni broj veci od 50, pokusava opet
while(unos > 50):
    # u listu brojevi dodaje kao pogresan pokusaj
    brojevi.append(unos)
    # trazi ponovni unos
    unos = int(input('Unesi broj: '))

# for petljom ispisujemo sve brojeve u nasem nizu brojevi
# odnosno pogresni pokusaji
for broj in brojevi:
    print(broj)
