# 2. Napisati program koji traži unos dva broja. Pronaći koji je od njih veći i ispisati ga.
# Podijeliti veci broj s manjim. Ako je manji broj 0, ispisati da je dijeljenje nemoguće.

# Zatrazit cemo unos 2 broja i spremiti ih u varijable a i b
a = int(input("Unesi prvi broj:"))
b = int(input("Unesi drugi broj:"))

# Krenimo s pretpostavkom da je a veci, b manji
veci = a
manji = b
# Ukoliko je ipak b veci, obrnemo
if b > a:
    veci = b
    manji = a

if a == b: ## ukoliko su jednaki, ispisat cemo da su jenaki
    print("Brojevi su jednaki")
else: # inace cemo ispisati veci
    print("Veci je", veci)

if manji == 0: # Ukoliko je manji broj jednak 0, ispat cemo da je dijeljenje nemoguce
    print("Dijeljenje je nemoguce")
else: # inace cemo ispisati rezultat dijeljenja
    print("Rezultat je:", veci/manji)    
