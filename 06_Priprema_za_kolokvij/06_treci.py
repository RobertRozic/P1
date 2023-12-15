# Napisati program u Pythonu koji će učitavati 10 brojeva.
# Naći i ispisati aritmetičku sredinu
# učitanih brojeva uzimajući u obzir
# samo one brojeve koji su veći ili
# jednaki 2 i manji ili jednaki 5.
zbroj = 0 # varijabla zbroj s pocetnom vrijednosti 0
brojac = 0 # brojac koji broji koliko je brojeva uzeto u obzir

for i in range(3):
    broj = int(input("Unesi broj:")) # unos broja
    #zbroj = zbroj + broj
    if broj >= 2 and broj <= 5:
        brojac += 1
        zbroj += broj

print("Prosjek je", zbroj/brojac)
