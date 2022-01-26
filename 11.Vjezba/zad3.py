'''
Zatražiti od korisnika unos broja te izgenerirati niz od toliko nasumičnih brojeva u intervalu [1, 500].
Zatim inicijalizirati novi niz u kojemu će biti svako 3. element iz prethodnog niza.
Nakon toga ispisati najveći i najmanji član novog niza.
'''
# Uradimo import biblioteke s random brojevima
import random

# Trazimo od korisnika unos broja
broj = int(input("Unesi broj:"))

# Definiramo praznu listu u koju cemo spremati nasumicne brojeve
nasumicni = []

# for petlja koja se izvrsava onoliko puta koliko je unio korisnik
for i in range(broj):
  # dohvacanje random broja
  el = random.randint(1, 500)
  # spremanje tog elementa u niz nasumicnih
  nasumicni.append(el)
  
# dohvacanje svako treceg elementa iz niza nasumicni
novi = nasumicni[::3] 

# Koristenjem ugradjenih funckija min i max
# dohvacamo najveci i najmanji broj u tom nizu
print("Najmanji broj je:", min(novi))
print("Najmanji broj je:", max(novi))
