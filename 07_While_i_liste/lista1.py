'''
# Lista
n = 10 # lista od 10 brojeva
brojevi = [0] * n

print("Brojevi prije:", brojevi)
# Korisnik unosi 10 brojeva i spremamo ih u listu
for i in range(n):
    print(i)
    # index
    brojevi[i] = int(input('Unesi broj: '))

print("Brojevi poslije:", brojevi)
'''
# dinamicka lista
brojevi = []
brojevi.append(5)
brojevi.append(7)
print("Lista", brojevi)
