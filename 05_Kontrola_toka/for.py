brojevi = [1, 2, 5, 17, 20]
print(brojevi)
print(type(brojevi))

tekst = "program"
# isto kao
# tekst = ["p", "r", "o", "g", "r", "a", "m"]

for i in brojevi:
    print(i)
    # 1 prolazak: i = 1
    # 2 prolazak: i = 2
    # 3 prolazak: i = 5
    # 4 prolazak: i = 17
    # 5 prolazak: i = 20
    print("test")

brojac = 0
print("Brojac na pocetku:", brojac)
for slovo in tekst:
    print(brojac)
    brojac = brojac + 1
    print(slovo)

print("Brojac na kraju:", brojac)

