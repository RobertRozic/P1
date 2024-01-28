# Ucitamo random modul
import random

# u varijablu broj spremimo random broj od 1 do 10
broj = random.randint(1, 10)
# ovo predstavlja broj koje je racunalo zamislilo

while True: # beskonacna petlja
	pokusaj = int(input("Unesi broj: "))
	if pokusaj == broj: # ako se broj podudara
		print("Pogodak!')
 		break # izlazak iz beskonacne petlje
	elif pokusaj < broj: # ako je poksuaj manji
		print("Unijeli ste broj koji je manji od zamisljenog")
	elif pokusaj > broj: # ako je pokusaj veci
		print("Unijeli ste broj koji je veci od zamisljenog")
