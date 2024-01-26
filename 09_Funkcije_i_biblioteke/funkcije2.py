# Funkcija koja vraca apsolutnu vrijednost broja
def apsolutna(broj):
    if broj < 0:
        return -broj
    elif broj == 0:
        return "Unijeli ste 0"
    else:
        return broj

rez = apsolutna(0)
rez2 = apsolutna(-5)

print(rez)
print(rez2)
