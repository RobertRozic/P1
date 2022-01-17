#def novaFunkcija():
   #print("Dobar dan!")
#   a = "Dobar dan!"
#   return a

# Ako funkcija vraca vrijednost
# mozemo je spremiti u varijablu
#tekst = novaFunkcija()
#print(tekst)

#def pozdrav(ime, prezime):
#    print("Dobar dan", ime, prezime)
    
# Pozicijski parametri
# Ovisno o redoslijedu kojim
# su definirani parametri
#pozdrav("Ivan", "Ivic")

# Naming parametri
# Ovisno o imenu parametra
#pozdrav(prezime = "Ivic", ime = "Ivan")

#def pozdravGod(ime, prezime, godine):
#    print("Dobar dan", ime, prezime, godine)

#pozdravGod("Ivan", godine=20, prezime="Ivic")

def apsolutna(broj):
    if broj >= 0:
        return broj
    else:
        return -broj

print(apsolutna(-5))
print(abs(-5))

najveci = max(10, 20, 50, 100, -200)
najmanji = min(10, 20, 50, 100, -200)
print(najveci, najmanji)

a = [5, 10, 15]

print(len(a))

print(ord("z"))
# velika slova od 65 do 90
# mala slova od 97 do 122

#print(min("abcdEfg"))
lista = []
a = "Robert"
print(a.upper())

voce = "jabuka, banana"
print(voce)
print(voce.replace("banana", "kruska"))