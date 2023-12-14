# Zadatak: Zbroj svih brojeva koji su spremljeni u listu.
brojevi = [2, 12, 25, 40, 11]

zbroj = 0
produkt = 1

for broj in brojevi:
    #zbroj = zbroj + broj # 0 + 2, 2 + 12, 14 + 25....
    zbroj += broj # skraceno
    #produkt = produkt * broj
    produkt *= broj # skraceno

print("Zbroj je:", zbroj)
print("Produkt je:", produkt)


