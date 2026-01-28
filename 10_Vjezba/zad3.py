'''
Zatražiti od korisnika unos broja
te izgenerirati niz od toliko nasumičnih brojeva
u intervalu [1, 500].

Zatim inicijalizirati novi niz u kojemu će biti
svako 3. element iz prethodnog niza.
Nakon toga ispisati najveći i najmanji član novog niza.
'''
# Ucitavanje biblioteke "random" u nas program
import random

# Unos korisnika
unos = int(input("Unesi broj:"))

# Definiramo prazan niz u koji cemo spremati generirane brojeve
brojevi = []

# For petlja range ovisan o unosu korisnika
for i in range(unos):
    broj = random.randint(1,500) # Dohvat random integera od 1 do 500 (ukljucuje 500)
    brojevi.append(broj) # Dinamicko dodavanje broja u niz

print(brojevi) # ispis

novi = brojevi[::3] # Novi niz - svako treci element prethodnog

print("Novi niz:", novi)
print("Najveci je:", max(novi))
print("Najmanji je:", min(novi))

    
