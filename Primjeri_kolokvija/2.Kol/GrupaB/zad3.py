while 1:
  unos = input("Unesite ime datoteke s ekstenzijom: ")
  tocka = unos.find(".")
  if tocka > -1:
    break

print('Ekstenzija je', unos[tocka+1:])

naziv = unos[:tocka]
print('Duljina naziva je', len(naziv))

