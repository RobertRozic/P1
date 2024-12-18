'''
Napiši program koji od korisnika traži unos dvoznamenkastog ili cetvetoznamenkastog broja.
Ukoliko unese pogrešan broj, ispisati poruku "Pogrešan unos".

Program zatim dohvaća zadnju i predzadnju znamenku.
Ukoliko je zadnja znamenka veća ispisati kvadrat njihovog zbroja, ukoliko je predzanja veća ispisati njihov umnožak.
Ukoliko su znamenke jednake ispisati odgovarajuću poruku koja na kraju uključuje i uneseni broj.
'''

broj = int(input("Unesite dvoznamenkasti ili cetveroznamenkasti broj: "))

if (broj > 9 and broj < 100) or (broj > 999 and broj < 10000):
  zadnja = broj % 10
  predzadnja = broj // 10 % 10
  if zadnja > predzadnja:
    print("Kvadrat zbroja", (zadnja+predzadnja)**2)
  elif predzadnja > zadnja:
    print("Umnozak", zadnja*predzadnja)
  else:
    print("Zadnje dvije znamenke su jednake. Uneseni broj je", broj)
else:
  print("Pogresan unos")

