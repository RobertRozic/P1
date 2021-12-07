suma = 0
  
for i in range(10):
  broj = int(input("Unesi broj:"))
  suma = suma + broj
  #ili krace suma += broj

print("Zbroj je:", suma)
prosjek = suma/10
print("Prosjek:", prosjek)
