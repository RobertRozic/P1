# Koristeći while petlju, zatražiti unos 5 različita slova
# Napisati funkciju za provjeru slova:
# - Jedno slovo (nije niz od vise slova)
# - Nije prethodno uneseno
# Funkciju koristiti za provjeru valjanosti unosa
# i spremiti valjana slova u niz
# Nakon unosa, generirati nasumičnu riječ
# od 3 slova koristeći ta slova

#Pomoc: koristiti random biblioteku i array indexe
import random

niz = []

def provjera(slovo):
    if len(slovo) != 1:
        return False
    if slovo in niz:
        return False
    return True
    #return len(slovo) == 1 and slovo not in niz

while True:
    if len(niz) == 5:
        break
    unos = input("Unesi slovo:")
    if provjera(unos):
        niz.append(unos)
    print("Provjera:", niz)

rijec = ''
for i in range(3):
    index = random.randint(0, len(niz)-1)
    rijec += niz[index]

print("Random rijec od 3 slova", rijec)

