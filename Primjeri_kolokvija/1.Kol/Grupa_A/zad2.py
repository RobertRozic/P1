a=int(input("Unesi troznamenkasti broj:"))

if a<100 or a>999:
	print("Pogresan unos")
else:
	zadnja=a%10
	kub_zadnje=zadnja**3
	if kub_zadnje % 2 == 1:
		print("Kub zadnje znamenke je neparan")
	else:
		print("Kub zadnje znamenke je paran")
	if kub_zadnje % 6 == 0:
		print("Kub zadnje znamenke je djeljiv sa 6")
	else:
		print("Kub zadnje znamenke nije djeljiv sa 6")


#if a >= 100 and <=999:
#	...
#else:
#	print("Pogresan unos")	

#if a > 99 and < 1000:
#	...
#else:
#	print("Pogresan unos")	
