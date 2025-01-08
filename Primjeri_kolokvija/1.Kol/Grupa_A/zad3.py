ime=input("Unesite vase ime:")
zbroj = 0
jednoznamenkasti=0

for i in range(7):
	broj = a=int(input("Unesite broj:"))
	if i<5:
		zbroj+=broj
	if broj > 0 and broj < 10:
		jednoznamenkasti += 1
		
if zbroj > 40:
	print(ime)
else:
	print(ime[::-1])
	
print("Broj jednoznamenkastih:", jednoznamenkasti)
