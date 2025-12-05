'''
Napišite program koji će ispisati
sve brojeve od 1 do 20 unazad,
a za svaki broj ispisati ako je djeljiv sa 3 ili sa 5.
'''
for i in range(20,0,-1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
