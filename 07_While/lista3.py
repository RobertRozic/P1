niz1 = "danas"
niz2 = "sutra"

brojevi1 = [1, 2, 3, 4, 5]
brojevi2 = [6, 7, 8, 9, 10]

# spajanje
#print(niz1+niz2)
#print(brojevi1+brojevi2)

# umnozavanje
#print(niz1*3)
#print(brojevi1*3)x
'''
# indeksiranje
print("prvi", brojevi1[0])
print("treci", brojevi1[2])
print("trece slovo", niz1[2])
print("cetvrti broj", brojevi2[4-1])

#podniz
tekst = "programiranje"
print("Podniz", niz1[0:3])
print(tekst[3:7]) # dio
print(tekst[:7]) # od pocetka do indeksa 7 (ne ukljucuje 7)
print(tekst[7:]) # od 7 (ukljucuje) do kraja

# provjera
print("Dan u sutra", "dan" in "sutra")
print("dan" in "danasa")
print(1 in brojevi1)
print(12 in brojevi1)

print("Dan nije u sutra:", "dan" not in "sutra")
print("Broj 1 se ne nalazi u brojevi1:", 1 not in brojevi1)
'''

# Indeks sa zada
print("danas"[-1])
print("sutra"[-2])

# korak indeksa
print("sutra"[-2:-3:-1])
print("sutra"[::2])

# ime unazad
print("robert"[::-1])

# sto ce ispisati program
a='kolokvij' # lokvi
b='test'
if a[2:7] != 'olo':
		if b[3] == 't':
			b=str(2**2-3) # b = 1
elif b[::2] == 'ts':
		b=str(6%3)

print(b + a)















