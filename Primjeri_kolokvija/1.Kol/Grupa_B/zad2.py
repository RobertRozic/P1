a=int(input("Unesi cetvroznamenkasti broj:"))

if a<1000 or a>9999:
	print("Pogresan unos")
else:
	zadnje_dvije=a%100
	if zadnje_dvije % 4 == 0:
		print("Broj koji cine zadnje dvije znamenke je djeljiv s 4")
	else:
		print("Broj koji cine zadnje dvije znamenke nije djeljiv s 4")

#if a >= 1000 and <=9999:
#	...
#else:
#	print("Pogresan unos")	

#if a > 999 and < 10000:
#	...
#else:
#	print("Pogresan unos")	
