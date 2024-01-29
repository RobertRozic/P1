'''
Zatražiti od korisnika unos broja
te izgenerirati niz od toliko nasumičnih brojeva
u intervalu [1, 500].

Zatim inicijalizirati novi niz
u kojemu će biti svako 3. element iz prethodnog niza.

Nakon toga ispisati najveći i najmanji član novog niza.
'''
import random # ucitavanje random modula

broj = int(input("Unesi broj:")) # zatrazi unos korisnika
brojevi = [] # niz u koji spremamo random brojeve

for i in range(broj): # ponavljanje onoliko puta koliko unese korisnik
    #nasumicni = random.randint(1, 500)
    brojevi.append(random.randint(1, 500)) # dinamicko dodavanje random broja

print(brojevi) # ispis

brojevi2 = brojevi[2::3] # svako treci
print(brojevi2)

# Najveci i najmanji
print("Najveci:", max(brojevi2))
print("Najmanji:", min(brojevi2))




