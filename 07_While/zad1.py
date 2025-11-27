# Zbroj brojeva do broja 10
brojevi = range(10)

zbroj = 0

for broj in brojevi:
    zbroj += broj

print("Zbroj je", zbroj)
print(f"Zbroj je {zbroj}")

# Pitajte korisnika unos broja
# i zbrojite sve brojeve do tog broja

# Unesi sve dok ne unese pozitivan broj

n = int(input("Unesi broj: "))

while n <= 0:
    print("Pogresan unos, unesite pozitivan broj")
    n = int(input("Unesi broj: "))

zbroj = 0

i = 1

while i < n:
    zbroj += i
    #i = i + 1
    i += 1

print("Zbroj", zbroj)
print("Kraj programa")







