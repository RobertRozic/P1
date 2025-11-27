'''
brojevi = range(0, 10, 1)

print(brojevi)
print(list(brojevi))


brojevi = range(5, 20, 2)
print(list(brojevi))


brojevi = range(5, 20)
print(list(brojevi))


brojevi = range(7)
print(list(brojevi))

brojevi = range(1, 15, 2)
print(list(brojevi))

brojevi = range(-8, -12, -1)
print(list(brojevi))
'''

for i in range(7):
    print(i)

for i in range(50, 200, 2):
    print(i)

# Umnozak svako treceg dvoznamenkastog broja
umnozak = 1

brojevi = range(10, 100, 3)

for broj in brojevi:
    umnozak *= broj

print("Umnozak je:", umnozak)












