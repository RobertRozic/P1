# Operatori za rad nad listama
unos1 = "danas"
unos2 = "sutra"
lista1 = [1, 2]
lista2 = [2, 3]
print(unos1 * 2)

print("Cetvrto slovo:", unos1[3])

rijec = "programiranje"
# podstring od indeksa 2 do indeksa 5
# slovo na indeksu 2 se ukljucuje
# slovo na indeksu 5 se ne ukljucuje
print(rijec[2:5])

# od pocetka do indeksa 7
print(rijec[:7])

# od pocetka do kraja
print(rijec[:])

# svako drugo slovo
print(rijec[::2])


#dohvacanje zadnjeg znaka
print("Predzanje slovo", rijec[-2])

# ispisuje rijec naopako (sa zada)
print(rijec[::-1])

# provjera nalazi li se jedan string u drugom
print("dan" in "danas")
print("dan" not in "danas")



