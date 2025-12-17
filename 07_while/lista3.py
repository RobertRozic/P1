rijec1 = "danas"
rijec2 = "sutra"

brojevi1 = [0, 1, 2]
brojevi2 = [3, 4, 5]

# Spajanje
print(rijec1 + rijec2)
print(brojevi1 + brojevi2)

# Umnozavanje
print(rijec1 * 3)
print(brojevi1 * 3)

# Indeksiranje
print(rijec1[0])
print(rijec1[1])
print(rijec1[2])

print(brojevi2[1])

# Podniz
# danas
print(rijec1[0:3])
print(rijec1[2:5])

# podniz od pocetka
print(rijec1[:3])
# podniz do kraja
print(rijec1[2:])

# dupliciranje
nova = rijec1[:]
print(nova)

# provjera postojanja u listi
print("dan" in "sutra")
print("dan" in "danas")
print(1 in [1, 2, 3])
print(5 in [1, 2, 3])

print("dan" not in "sutra")
print("dan" not in "danas")

# negativni indeksi
# prvo slovo sa zada
print(rijec1[-1])
# drugo slovo sa zada
print(rijec1[-2])

# od prvog do zadnjeg slova (bez zadnjeg)
print(rijec1[0:-1])

# svako drugo slovo
print(rijec1[::2])

# rijec unazad
print(rijec1[::-1])









