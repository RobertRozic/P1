brojevi = []

unos = int(input("Unesi broj manji od 50:"))
# unesi broj sve dok ne uneses broj veci od 50
while unos < 50:
    brojevi.append(unos)
    unos = int(input("Unesi broj manji od 50:"))
    
print(brojevi)
