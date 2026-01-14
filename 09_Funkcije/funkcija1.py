# Nema parametara
# Ne vraca vrijednost
def pozdrav():
    print("Dobar dan!")

# Funkciju moramo pozvati!
pozdrav()

# Ima jedan parametar ime
# Ne vraca vrijednost
def pozdrav_ime(ime):
    print("Dobar dan", ime, "!")

pozdrav_ime("Robert")

# Ima 2 parametra
# Ne vraca vrijednost
def pozdrav_ime_prezime(ime, prezime):
    print("Dobar dan", ime, prezime, "!")

a = pozdrav_ime_prezime("Robert", "Rozic")
print("Funkcija je vratila:", a)

# Funckija koja zbraja 2 proslijedjena broja
# Funkcija vraca vrijednost zbroja
def zbroji(a, b):
    zbroj = a + b
    #print("Zbroj je:", zbroj)
    return zbroj

a = zbroji(2, 5)
print("Funkcija je vratila:", a)

# Apsolutna vrijednost
def apsolutna(broj):
    if broj >= 0:
        return broj
    else:
        return -broj

rez = apsolutna(-11)
print(rez)

