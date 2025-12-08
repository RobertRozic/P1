# Koristeći while petlju i break iskaz
# od korisnika tražite unos podataka o 
# knjigama (naslov, broj stranica, godina)
# dok se ne unese 'x' ili 'X'
# Napišite funkciju koja naslov,
# broj stranica i godinu izdanja
# knjige te ih dodaje u odgovarajuće zasebne liste.
# Ispisati:
# - Prosječan broj stranica po knjizi
# - Naziv najstarije i najnovije knjige
naslovi = []
stranice = []
godine = []

def dodaj(naslov, brStr, godina):
    naslovi.append(naslov)
    stranice.append(brStr)
    godine.append(godina)

while True:
    naslov = input("Unesi naslov")
    if naslov.lower() == 'x':
        break
    brStr = input("Unesi broj stranica")
    if brStr.lower() == 'x':
        break
    brStr = int(brStr)
    godina = input("Unesi godinu izdanja")
    if godina.lower() == 'x':
        break
    godina = int(godina)
    dodaj(naslov, brStr, godina)

prosjek = sum(stranice) / len(stranice)
print("Prosjecan broj stranica je:", prosjek)

'''
najveca = max(godine)
najmanja= min(godine)

indexNajvece = 0
indexNajmanje = 0
for i in range(len(godine)):
    if najveca == godine[i]:
        indexNajvece = i
    if najmanja == godine[i]:
        indexNajmanje = i
'''

indexNajvece = godine.index(max(godine))
indexNajmanje = godine.index(min(godine))

print("Namladja knjiga", naslovi[indexNajvece])
print("Najstarija knjiga", naslovi[indexNajmanje])


