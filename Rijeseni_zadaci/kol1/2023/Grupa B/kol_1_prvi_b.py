'''
Napiši program koji definira artikal i njegovu
zalihu na skladištu.

Nakon toga od korisnika zatražiti unos prodane
količine tog artikla. (npr. zaliha 100, prodano 15 kava)

Ukoliko je uneseno da je prodano više od zalihe,
ispisati "Pogrešan unos!"
Inače Ispisati postotak prodane količine
(npr za 15/100 je 15%).

Ukoliko je ostalo manje od 10% artikla ispisati
"Pozovi narudžbu za [ime artikla]".
'''
artikal = "Kava" # Definiramo naziv artikla
zaliha = 100 # definiramo stanje na skladistu

# Od korisnika trazimo unos prodane kolicine
prodano = int(input("Unesi prodanu kolicinu artikla " + artikal))
#prodano = int(prodano)

# ako je prodano vise od zalihe, znaci da je unos pogresan
if prodano > zaliha:
    print("Pogresan unos!")
else: # inace se nastavlja program
    postotak = prodano/zaliha # racunamo prodani postotak
    print("Postotak prodane kolicine je: ", postotak * 100, '%')
    if postotak > 0.9: # ako je prodano vise od 90%
        print("Pozovi narudzbu za "+ artikal)

