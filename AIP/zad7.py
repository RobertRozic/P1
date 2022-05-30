# 7. Napisati program u Pythonu koji će učitavati 10 brojeva. Naći i ispisati aritmetičku
# sredinu učitanih brojeva uzimajući u obzir samo one brojeve koji su veći ili jednaki 2 i
# manji ili jednaki 5.

# Postavimo dvije varijable na 0
zbroj = 0 # U varijablu zbroj zbrajamo sve vrijednosti koje zadovoljavaju uvjet
brojac = 0 # Varijablu brojac koristimo za brojanje koliko brojeva smo uzeli u obzir
for i in range(10):
    broj = int(input("Unesite broj:"))
    # brojevi veci ili jednaki dva I menji ili jednaki 5
    if broj >= 2 and broj <= 5:
        zbroj += broj
        brojac += 1

# Podijelimo zbroj s brojacem kako bi dobbili aritmeticku sredinu brojeva
print("Aritmeticka sredina je:", zbroj/brojac)

