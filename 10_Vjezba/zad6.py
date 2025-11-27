'''
Na početku programa od korisnika tražiti
unos 5 artikala s njihovim cijenama.
Artikle i njihove cijene spremati u 2 niza
- artikli (niz naziva artikla) i
cijene(niz floatova) pomoću funkcije.

Ispisati pozicija - naziv - cijena korisniku kao
cjenik artikala.
'''

#artikli = []
artikli = ['mlijeko', 'kruh', 'sok', 'kava', 'jaja']

#cijene = []
cijene = [2.1, 1.7, 2.5, 7.5, 5.2]

def unosArtikla(naziv, cijena):
    artikli.append(naziv)
    cijene.append(cijena)

'''   
for i in range(5):
    naziv = input("Unesi naziv artikla:")
    cijena = float(input("Unesi cijenu artikla:"))
    unosArtikla(naziv, cijena)
'''
print(artikli)
print(cijene)

print('-'*25)
print('|sifra|naziv|cijena|')
for index in range(len(artikli)):
    naziv = artikli[index]
    cijena = cijene[index]
    print(index, naziv, cijena)
print('-'*25)

'''
Napisati program za ispis računa:

Korisnik iz unesene baze artikala bira artikal
na poziciji i unosi kupljenu količinu.
Ponavljati unos artikla sve dok se ne unese “x”.

Program množi cijenu artikla s količinom
te sumu zapisuje u novi niz - racun.

Zbrojiti sve elemente u nizu račun i korisniku izbaciti ukupnu cijenu računa.
'''

racun = []

while True:
    sifra = input("Unesi sifru artikla:")
    if sifra.lower() == 'x':
        break
    sifra = int(sifra)
    print("Izabrali ste arikal ", artikli[sifra])
    cijena = cijene[sifra]
    print("Cijena je:", cijena)
    kolicina = int(input("Unesite kolicinu za kupovinu:"))
    suma = cijena * kolicina
    racun.append(suma)

print("Ukupan iznos racuna je:", round(sum(racun), 2))

