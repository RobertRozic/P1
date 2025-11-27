# 4. Zatražiti od korisnika unos riječi i provjeriti je li ta riječ palindrom.

unos = input("Unesite rijec")

# Obrtanje rijeci, dohvacanje svakog znaka, ali sa zada, zbog toga -1
unos_obrnuto = unos[::-1]

# Provjera ukoliko je rijec palindrom
if unos == unos_obrnuto:
    print("Rijec je palindrom")
else:
    print("Rijec nije palindrom")
