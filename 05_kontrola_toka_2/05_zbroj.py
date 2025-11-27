# Zbroj svih brojeva koji su definirani u listi
brojevi = [1, 2, 3, 5, 9, 22] # definiranje liste brojeva
zbroj = 0 # pocetna vrijednost varijable zbroj
umnozak = 1 # pocetna vrijednost varijable umnozak

for broj in brojevi: # definiranje for petlje za svaki broj u brojevi
    # broj nam je 1, zbroj je 0
    # broj nam je 2, zbroj je 1
    # broj nam je 3, zbroj je 3
    # ...
    # broj nam je 22, zbroj 20
    #zbroj = zbroj + broj # u varijablu zbroj spremamo zbroj + broj
    zbroj += broj # skraceno
    #umnozak = umnozak * broj # u varijablu umnozak spremamo umnozak * broj
    umnozak *= broj

# ispis
print("Zbroj je", zbroj)
print("Umnozak je", umnozak)

    




