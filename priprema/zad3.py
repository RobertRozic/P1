'''
Napisati program u Pythonu koji će učitavati 10 brojeva.
Naći i ispisati aritmetičku sredinu učitanih brojeva uzimajući u obzir samo one brojeve koji su veći ili
jednaki 2 ili manji ili jednaki 5.
'''
#Aritmeticka sredina je suma brojeva / broj brojeva

# Zbroj na pocetku postavljamo na 0
zbroj = 0
# brojac brojeva koji ispunjavaju uvjet
brojac = 0

# Kod koji je unutar for petlje ce se izvrsiti 10 puta
for i in range(10):
    broj = int(input("Unesi broj: "))
    # Svaki broj koji korisnik unese, se zbroji na varijablu zbroj
    #zbroj = zbroj + broj
    if broj == 2 or broj <= 5:
        zbroj += broj
        # Svaki put kada se ispuni uvjet, brojac povecamo za 1
        brojac += 1

print("Zbroj je", zbroj)
print("Aritmeticka sredina", zbroj/brojac)

