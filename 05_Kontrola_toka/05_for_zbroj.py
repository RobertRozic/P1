# Zbroj svih brojeva koji su spremljeni u listu.
brojevi = [1, 1, 2, 3, 5, 8, 13] # definiramo listu
zbroj = 0 # pocetnu vrijednost zbroja postavimo na 0
umnozak = 1
for broj in brojevi: # prolazimo kroz svaki broj u listi brojevi
    # zbroj = 0, broj = 1
    # zbroj = 1, broj = 1
    # zbroj = 2, broj = 2
    ###...
    # zbroj = 20, broj = 13
    #zbroj = zbroj + broj  # zbroj = 33
    zbroj += broj # skraceno
    #umnozak = umnozak * broj
    umnozak *= broj # skraceno
    

print("Zbroj je:", zbroj) # konacni ispis
print("Umnozak je:", umnozak)
    

