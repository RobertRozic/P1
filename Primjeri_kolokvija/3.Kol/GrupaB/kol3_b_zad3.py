#Napisati program koji čita podatke iz datoteke rezultati.txt iz 2. zadatka. 
#Program ispisuje ime i prezime osoba koje su položile ispit.
#Ispisati koliki postotak osoba je položilo ispit.
#Napomena: Za prolaz je potrebno 50 bodova.

datoteka = open("rezultati.txt", "r")
linije = datoteka.readlines()

print("Studenti koji su prosli su: ")
polozili = 0
for linija in linije:
  osoba = linija.split(',')
  bodovi = int(osoba[2])
  if bodovi > 49:
    print(osoba[1], osoba[0])
    polozili += 1

postotak = (polozili / len(linije)) * 100
print("Postotak polozenih", str(postotak) + "%" )

datoteka.close()
