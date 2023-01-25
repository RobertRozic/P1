'''
def pozdrav(ime):
    print("Dobar dan", ime)

def pozdraV(ime):
    print("Dobro jutro", ime)
    
pozdraV("Robert")



Funkcija kao parametre prima 2 broja
vraca njihov zbroj


def zbroj(a, b):
    rezultat = a + b
    return rezultat

rez = zbroj(3, 5)
print("Zbroj dva broja:", rez)


Apsolutna vrijednost
def apsolutna(broj):
    if broj >= 0:
        return broj
    else:
        return -broj

print(apsolutna(-100))
'''

def pozdrav2():
    print("Pozdrav!")

pozdrav2()

print(min(15,-9,56,123,0))

print("Ime Robert ima", len("Robert"), "slova.")

brojevi = []

brojevi.append(5)

rijec = 'jabuka, banana'
print(rijec.replace("banana", "naranca"))

recenica = 'Danas je cetvrtak'
print(recenica.find("srijeda"))

print(recenica.lower())
print(recenica.upper())

# za liste koristimo index
brojevi = [3, 2, 1]
print(brojevi.index(2))


    
