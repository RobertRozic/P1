'''
Napisati program koji će
ispisati umnožak 5 slučajno
odabranih brojeva od 1 do 100
'''
import random
import math

brojevi = [] 
for i in range(5):
    broj = random.randint(1, 100)
    brojevi.append(broj)

umnozak = math.prod(brojevi)
print("Umnozak brojeva je", umnozak)
