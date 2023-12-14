# Ispiši poruku ako je uneseni broj pozitivan ili 0, inače ispisi da je negativan.

a = int(input("Unesi broj:"))

if a >= 0:
    print("Broj je veci ili jednak nula!")
    if a == 0:
        print("broj je nula")
    else:
        print("broj je pozitivan")
else:
    print("broj je negativan")
