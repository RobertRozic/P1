# Napisati program koji će ispisati
# umnožak 5 slučajno odabranih brojeva od 1 do 100.

# ukljucivanje random biblioteke/modula
import random

umnozak = 1 # definiramo pocetnu vrijednost varijable umnozak

# kod koji se ponavlja 5 put
for i in range(5):
    broj = random.randint(1, 100)
    # broj = random.randrange(1, 101)
    #umnozak = umnozak * broj
    umnozak *= broj

print(umnozak)
    
