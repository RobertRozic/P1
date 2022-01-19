#import math
#print(math.sqrt(16))

#from math import pi as ludolfov_broj
#print(ludolfov_broj)

import random

# Random funkcija vraca brojeve od 0 do 1
#broj = random.random()

# randint vraca integer u odredjenom
# intervalu
# [a, b]
broj = random.randint(1, 10)

# randrange vraca brojeve u intervalu, s korakom
# [a, b)
broj = random.randrange(2,10,2)

print(broj)

# Generiranje 5 random brojeva
# racunanje njihovog umnoska
brojevi = []
for i in range(5):
    a = random.randint(1, 10)
    brojevi.append(a)

print(brojevi)

umnozak = 1
for broj in brojevi:
    umnozak *= broj
    
print(umnozak)    
    
    
    
