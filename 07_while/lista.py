# Lista
brojevi = [1, 2, 3, 5, 8, 13]

print(brojevi)
print(type(brojevi))

# Pristup elementu u listi
print("Prvi element, krece od nule:", brojevi[0])
print("Drugi element:", brojevi[1])

# unos 10 brojeva i spremanje u listu
n = 10
brojevi = [None] * n
print(brojevi)
for i in range(n):
    unos = int(input("Unesi broj:"))
    brojevi[i] = unos
print("Izgled brojeva nakon unosa:", brojevi)
print("Zadnji broj", brojevi[15])

