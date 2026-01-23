# Napisati program koji će ispisati
# umnožak 5 slučajno odabranih brojeva od 1 do 100.

import random

umnozak = 1
brojevi = []

for i in range(5):
    broj = random.randint(1,100)
    #print("Nasumicni broj:", broj)
    brojevi.append(broj)
    umnozak *= broj

print("Izbrani brojevi su:", brojevi)
print("Umnozak brojeva je:", umnozak)






