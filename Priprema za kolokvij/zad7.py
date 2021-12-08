unos = input("Unesite rijec")

unos_obrnuto = unos[::-1]

if unos == unos_obrnuto:
    print("Rijec je palindrom")
else:
    print("Rijec nije palindrom")
