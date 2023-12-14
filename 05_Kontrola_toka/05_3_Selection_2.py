# Provjeri je li uneseni broj pozitivan, nula ili negativan

a = int(input("Unesi broj: "))

if a > 9:
    print("Broj ima vise od jedne znamenke")
elif a > 0:
    print("Broj ima jednu zamenku")
elif a == 0:
    print("Broj je nula")
else:
    print("Broj je negativan")
