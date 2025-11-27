p1=int(input("Unesite prvi promjer: "))
p2=int(input("Unesite drugi promjer: "))
r1=p1/2
r2=p2/2

if p1 <= 0 or p2 <= 0:
	print("Pogresan unos")
else:
	if p1%p2 == 0 or p2%p1 == 0:
		print("Opseg prvog:", 2*r1*3.14)
		print("Opseg drugog:", 2*r2*3.14)
	else:
		print("Povrsina prvog:", r1**2*3.14)
		print("Povrsina drugog:", r2**2*3.14)	
