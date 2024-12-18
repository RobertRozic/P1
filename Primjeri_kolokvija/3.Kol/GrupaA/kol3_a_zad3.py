#Napisati program koji čita podatke o osobama iz datoteke osobe.txt iz 2. zadatka. 
#Program generira random broj između 1 i 30 te ispisuje ime i prezime osoba s tim sretnim brojem.
#Ispisati koliko ima takvih osoba i koji broj je izabran.
import random

datoteka = open("osobe.txt", "r")

linije = datoteka.readlines()

brojac = 0
broj = random.randint(1,30)

for linija in linije:
    osoba = linija.split(",")
    sretni_broj = int(osoba[2])
    if sretni_broj == broj:
        brojac += 1

print("Izabrani broj:", broj)
print(brojac, "osoba sa sretnim brojem.")

datoteka.close()
